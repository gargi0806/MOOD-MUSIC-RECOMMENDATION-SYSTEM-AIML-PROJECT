from sentiment_model import analyze_sentiment
from sentiment_analysis import recommend_music_by_sentiment

user_text = input("Enter a message to analyze your mood:\n")

sentiment = analyze_sentiment(user_text)
print("\nSentiment detected:", sentiment)

songs = recommend_music_by_sentiment(sentiment)

print("\nRecommended songs:")
for s in songs:
    print("-", s)
