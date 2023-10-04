### Sending Email
## Importing...
import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(subject, message):
    # Adding Host
    host = "smtp.gmail.com"
    port = 465

    # Credentials
    username = os.getenv("USERNAME_1")
    password = os.getenv("PASSWORD")
    receiver = "yasiratiqmohammed@gmail.com"

    # Create a MIMEText object to represent the message
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = receiver
    msg['Subject'] = subject

    # Attach the message body
    msg.attach(MIMEText(message, 'plain'))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg.as_string())

send_mail("Test subject", "Test email.")
