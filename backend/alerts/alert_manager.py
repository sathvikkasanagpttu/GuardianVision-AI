import os, smtplib
from email.message import EmailMessage

def send_email_alert(subject, body, image_path=None):
    required = ["SMTP_HOST", "ALERT_EMAIL", "ALERT_EMAIL_PASSWORD", "ALERT_RECIPIENT"]
    if not all(os.getenv(x) for x in required):
        return {"sent": False, "reason": "SMTP variables are not configured"}

    msg = EmailMessage()
    msg["Subject"], msg["From"], msg["To"] = subject, os.getenv("ALERT_EMAIL"), os.getenv("ALERT_RECIPIENT")
    msg.set_content(body)
    if image_path and os.path.exists(image_path):
        with open(image_path, "rb") as f:
            msg.add_attachment(f.read(), maintype="image", subtype="jpeg",
                               filename=os.path.basename(image_path))
    with smtplib.SMTP(os.getenv("SMTP_HOST"), int(os.getenv("SMTP_PORT", "587"))) as smtp:
        smtp.starttls()
        smtp.login(os.getenv("ALERT_EMAIL"), os.getenv("ALERT_EMAIL_PASSWORD"))
        smtp.send_message(msg)
    return {"sent": True}
