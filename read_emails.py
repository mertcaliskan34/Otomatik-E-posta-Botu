import marimo as mo
from gmail_api import init_gmail_service, get_email_messages, get_email_message_details

client_file = 'client_secret.json'
service = init_gmail_service(client_file)
messages = get_email_messages(service, max_results=5)