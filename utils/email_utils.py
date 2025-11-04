from email.mime.text import MIMEText
from googleapiclient.discovery import build
import base64

def send_gmail_html(creds, to, subject, html_body):
    """Envía un correo en formato HTML usando la API de Gmail"""
    service = build('gmail', 'v1', credentials=creds)
    message = MIMEText(html_body, 'html')
    message['to'] = to
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    message = {'raw': raw}
    service.users().messages().send(userId='me', body=message).execute()
