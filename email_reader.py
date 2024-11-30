import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
else:
    raise FileNotFoundError("token.json bulunamadı. Yetkilendirme işlemini yeniden yapın.")

service = build('gmail', 'v1', credentials=creds)

# Gelen e-postaları al
results = service.users().messages().list(userId='me', maxResults=5).execute()
messages = results.get('messages', [])

if not messages:
    print("Hiç e-posta yok!")
else:
    print("E-postalar:")
    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        print(f"Konu: {msg['snippet']}")