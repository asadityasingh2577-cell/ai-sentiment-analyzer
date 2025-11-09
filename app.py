from flask import Flask, render_template, request
from model import analyze_sentiment
from db import insert_review, get_all_reviews
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment_result = None
    if request.method == "POST":
        text = request.form.get("review_text")
        if text:
            sentiment, score = analyze_sentiment(text)
            insert_review(text, sentiment, float(score))
            sentiment_result = {"text": text, "sentiment": sentiment, "score": score}

    # Fetch all reviews for display
    all_reviews = get_all_reviews()
    df = pd.DataFrame(all_reviews)
    if not df.empty:
        sentiment_counts = df['sentiment'].value_counts().to_dict()
    else:
        sentiment_counts = {}
    return render_template("index.html", result=sentiment_result, counts=sentiment_counts)

if __name__ == "__main__":
    app.run(debug=True)
