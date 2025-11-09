from transformers import pipeline

# Load pre-trained sentiment-analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """
    Returns sentiment label and score for the given text.
    """
    result = sentiment_pipeline(text)[0]
    label = result['label']  # 'POSITIVE' or 'NEGATIVE'
    score = result['score']
    # Convert to simpler categories
    if label == "POSITIVE" and score > 0.6:
        sentiment = "Positive"
    elif label == "NEGATIVE" and score > 0.6:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment, score
