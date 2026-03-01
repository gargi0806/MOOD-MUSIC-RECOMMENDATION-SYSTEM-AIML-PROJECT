def recommend_music_by_sentiment(sentiment):

    positive_songs = [
        "Happy - Pharrell Williams",
        "On Top of the World - Imagine Dragons",
        "Good Life - OneRepublic",
    ]

    negative_songs = [
        "Someone Like You - Adele",
        "Fix You - Coldplay",
        "Let Her Go - Passenger",
    ]

    neutral_songs = [
        "Lovely - Billie Eilish",
        "Night Changes - One Direction",
        "Photograph - Ed Sheeran",
    ]

    if sentiment == "positive":
        return positive_songs

    elif sentiment == "negative":
        return negative_songs

    else:
        return neutral_songs
