from textblob import TextBlob

def analyze_sentiment(text):
    # Convert text into TextBlob object
    blob = TextBlob(text)

    # Polarity score ranges from -1 to +1
    polarity = blob.sentiment.polarity

    # Classify based on polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"
