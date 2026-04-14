import os
import csv
import smtplib
from email.message import EmailMessage
from datetime import datetime
import argparse

# Load .env variables manually to avoid external dependencies
env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

# Configuration
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASS = os.environ.get("SMTP_PASS")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTBOX_DIR = os.path.join(BASE_DIR, "outreach_outbox")
TARGETS_FILE = os.path.join(OUTBOX_DIR, "targets.csv")
LOG_FILE = os.path.join(OUTBOX_DIR, "outreach_log.csv")

def load_sent_log():
    sent_emails = set()
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('status') == 'SENT':
                    sent_emails.add(row.get('email'))
    return sent_emails

def append_log(email, status, message=""):
    file_exists = os.path.exists(LOG_FILE)
    with open(LOG_FILE, mode='a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['timestamp', 'email', 'status', 'message'])
        writer.writerow([datetime.utcnow().isoformat(), email, status, message])

def send_email(to_email, subject, body, dry_run=False):
    if dry_run:
        print(f"[DRY RUN] Would send to: {to_email} | Subject: {subject}")
        return True, "Dry run success"
        
    if not all([SMTP_USER, SMTP_PASS]):
        return False, "SMTP credentials missing"

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = SMTP_USER
    msg['To'] = to_email

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
        server.quit()
        return True, "Success"
    except Exception as e:
        return False, str(e)

def main():
    parser = argparse.ArgumentParser(description="QBO Stack Advisor Outreach Execution")
    parser.add_argument('--dry-run', action='store_true', help="Run without sending emails")
    parser.add_argument('--max-sends', type=int, default=50, help="Maximum emails to send in one run")
    args = parser.parse_args()

    if not os.path.exists(TARGETS_FILE):
        print(f"Error: Targets file not found at {TARGETS_FILE}")
        return

    sent_emails = load_sent_log()
    send_count = 0

    with open(TARGETS_FILE, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if send_count >= args.max_sends:
                print("Max send limit reached. Exiting.")
                break

            email = row.get('email', '').strip()
            name = row.get('name', '').strip()
            company = row.get('company', '').strip()
            subject = row.get('subject', '').strip()
            template_file = row.get('template', '').strip()

            if not email or not name or not template_file:
                print(f"Skipping row missing required fields: {row}")
                append_log(email, "SKIPPED", "Missing required fields")
                continue

            if email in sent_emails:
                print(f"Skipping already contacted email: {email}")
                continue

            template_path = os.path.join(OUTBOX_DIR, template_file)
            if not os.path.exists(template_path):
                print(f"Template not found: {template_path}")
                append_log(email, "FAILED", f"Template not found: {template_file}")
                continue

            with open(template_path, 'r', encoding='utf-8') as tf:
                body = tf.read()

            # Inject variables
            body = body.replace('{name}', name).replace('{company}', company)
            
            # Check SMTP before attempting
            if not args.dry_run and not all([SMTP_USER, SMTP_PASS]):
                print("Halting: SMTP authentication credentials missing.")
                break

            success, error_msg = send_email(email, subject, body, dry_run=args.dry_run)
            
            if success:
                print(f"Sent to {email}")
                append_log(email, "SENT" if not args.dry_run else "DRY_RUN", "Success")
                send_count += 1
            else:
                print(f"Failed to send to {email}: {error_msg}")
                append_log(email, "FAILED", error_msg)

if __name__ == "__main__":
    main()