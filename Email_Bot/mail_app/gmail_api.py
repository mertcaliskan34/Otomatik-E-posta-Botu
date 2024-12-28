from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os
import base64
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from googleapiclient.errors import HttpError

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send'
]

def gmail_authenticate():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

def is_user_authenticated():
    return os.path.exists('token.pickle')

def decode_base64url(encoded_text):
    decoded_bytes = base64.urlsafe_b64decode(encoded_text + '==')
    return decoded_bytes.decode('utf-8')

def list_messages(service, user_id='me'):
    # Gönderilen e-postaları hariç tutmak için Gmail API sorgusu
    query = "-from:me"
    results = service.users().messages().list(userId=user_id, maxResults=10, q=query).execute()
    messages = results.get('messages', [])
    emails = []
    
    for message in messages:
        msg = service.users().messages().get(userId=user_id, id=message['id']).execute()
        payload = msg['payload']
        headers = payload['headers']
        email_data = {'id': message['id']}
        
        for header in headers:
            if header['name'] == 'From':
                email_data['from'] = header['value']
            if header['name'] == 'Subject':
                email_data['subject'] = header['value']
                
        # Durum (Okunmadı / Okundu)
        labels = msg['labelIds']
        email_data['status'] = 'Okunmadı' if 'UNREAD' in labels else 'Okundu'
        
        # Tarih
        internal_date = int(msg['internalDate']) / 1000  # ms to seconds
        email_data['date'] = datetime.utcfromtimestamp(internal_date).strftime('%d/%m/%Y')
        
        emails.append(email_data)
        
    return emails

def get_email_details(service, message_id, user_id='me'): 
    message = service.users().messages().get(userId=user_id, id=message_id).execute()
    payload = message.get('payload', {})
    headers = payload.get('headers', [])
    email_data = {'id': message_id}

    # E-posta başlıklarını al
    for header in headers:
        if header['name'] == 'From':
            email_data['from'] = header['value']
        if header['name'] == 'Subject':
            email_data['subject'] = header['value']
        if header['name'] == 'Date':
            email_data['date'] = header['value']

    # Gövdeyi al ve decode et
    parts = payload.get('parts', [])
    body = ''
    if parts:
        for part in parts:
            if part.get('mimeType') == 'text/plain':
                data = part.get('body', {}).get('data', '')
                if data:
                    # Base64URL decode işlemi
                    body = base64.urlsafe_b64decode(data).decode('utf-8')
    else:
        # Eğer 'parts' yoksa direkt payload body'yi al
        data = payload.get('body', {}).get('data', '')
        if data:
            body = base64.urlsafe_b64decode(data).decode('utf-8')

    email_data['body'] = body
    
    return email_data

def send_email(service, to, subject, body):
    message = MIMEMultipart()
    message['to'] = to
    message['subject'] = subject
    msg = MIMEText(body)
    message.attach(msg)

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')

    try:
        message = service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
        print(f'Message Id: {message["id"]}')
        return message
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None