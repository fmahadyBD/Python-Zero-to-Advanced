import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(subject, body, to_email, attachment_path):
    # Set up the Outlook SMTP server
    smtp_server = 'smtp.office365.com'
    smtp_port = 587
    smtp_username = 'fmahadybd@outlook.com'
    smtp_password = '@Fahim22003285@'  # Replace with your actual password

    # Create the MIME object
    message = MIMEMultipart()
    message['From'] = smtp_username
    message['To'] = to_email
    message['Subject'] = subject

    # Attach body as plain text
    message.attach(MIMEText(body, 'plain'))

    # Attach the file
    with open(attachment_path, 'rb') as file:
        attachment = MIMEApplication(file.read())
        attachment.add_header('Content-Disposition', 'attachment', filename=attachment_path)
        message.attach(attachment)

    # Connect to the server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, message.as_string())

# Example usage
subject = 'Subject of the email'
body = 'Body of the email'
to_email = 'fmahadynotes@gmail.com'
attachment_path = r'C:\Users\Mahady Hasan Fahim\Desktop\New Text Document.txt'

send_email(subject, body, to_email, attachment_path)
