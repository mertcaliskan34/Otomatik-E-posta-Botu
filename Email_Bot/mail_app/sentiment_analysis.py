from textblob import TextBlob
from mail_app.templatetags.custom_filters import clean_email_body

def analyze_sentiment(email_text):
    email_text = clean_email_body(email_text)
    analysis = TextBlob(email_text)
    polarity = analysis.sentiment.polarity

    # Determine sentiment label
    if polarity > 0.01:
        return "happy"
    elif polarity < -0.01:
        return "angry"
    else:
        return "neutral"