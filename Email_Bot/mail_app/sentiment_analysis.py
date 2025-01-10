from textblob import TextBlob
from mail_app.templatetags.custom_filters import clean_email_body
from deep_translator import GoogleTranslator

def analyze_sentiment(email_text):
    # Clean the email body
    email_text = clean_email_body(email_text)
    
    # Translate the email text to English
    translated_text = GoogleTranslator(source='auto', target='en').translate(email_text)
    
    # Perform sentiment analysis on the translated text
    analysis = TextBlob(translated_text)
    polarity = analysis.sentiment.polarity

    # Determine sentiment label
    if polarity > 0.30:
        return "very happy"
    elif polarity > 0.10:
        return "happy"
    elif polarity < -0.10:
        return "angry"
    elif polarity < -0.30:
        return "very angry"
    else:
        return "neutral"