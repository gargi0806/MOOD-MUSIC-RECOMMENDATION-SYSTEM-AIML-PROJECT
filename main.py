from face_emotion import detect_emotion
from music_recommender import play_music

# SENTIMENT FEATURES
from sentiment_model import analyze_sentiment
from sentiment_analysis import recommend_music_by_sentiment
def choose_mode():
    print("\n===============================")
    print("      MOOD MUSIC SYSTEM")
    print("===============================")
    print("1. Emotion Detection (Webcam)")
    print("2. Sentiment Analysis (Text Input)")
    return input("Choose 1 or 2: ").strip()
def choose_music_source():
    # NOW ONLY OFFLINE MUSIC
    return "1"   # Always offline
def run_emotion_mode():
    emotion = detect_emotion()
    print(f"\n😊 Detected Emotion: {emotion}")

    print("\n🎵 Offline Mode Selected")
    play_music(emotion)
def run_sentiment_mode():
    user_text = input("\n📝 Type something to analyze your mood: ")

    sentiment = analyze_sentiment(user_text)
    print(f"\n💬 Detected Sentiment: {sentiment}")

    print("\n🎵 Offline Mode Selected")
    songs = recommend_music_by_sentiment(sentiment)

    print("\n🎶 Recommended Songs:")
    for s in songs:
        print("•", s)
def main():
    mode = choose_mode()

    if mode == "1":
        run_emotion_mode()

    elif mode == "2":
        run_sentiment_mode()

    else:
        print("\n❌ Invalid option. Restart the program.")
if __name__ == "__main__":
    main()
