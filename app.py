from flask import Flask, render_template, request, jsonify, Response
from sentiment_model import analyze_sentiment
from sentiment_analysis import recommend_music_by_sentiment
from music_recommender import play_music, stop_music, pause_music, resume_music, play_music_for_name
from face_emotion import detect_emotion_from_frame
from deepface import DeepFace
import cv2

app = Flask(__name__)

# ------------------------------
# CAMERA SETUP (ONLY ONE INSTANCE)
# ------------------------------
camera = cv2.VideoCapture(0)

# ------------------------------
# ROUTES
# ------------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotion")
def emotion_page():
    return render_template("emotion.html")


@app.route("/detect-emotion", methods=["POST"])
def detect_emotion_api():
    # Capture a single frame from the existing camera
    success, frame = camera.read()
    if not success:
        return jsonify({"error": "Could not read frame"}), 500

    # Detect emotion from this frame
    emotion = detect_emotion_from_frame(frame)

    # Play music based on detected emotion and get song name
    song_name = play_music(emotion)

    return jsonify({"emotion": emotion, "song": song_name})


@app.route("/sentiment")
def sentiment_page():
    return render_template("sentiment.html")

@app.route("/analyze-sentiment", methods=["POST"])
def analyze_sentiment_api():
    text = request.form.get("text")
    sentiment = analyze_sentiment(text)
    songs = recommend_music_by_sentiment(sentiment)
    return jsonify({"sentiment": sentiment, "songs": songs})

# ------------------------------
# MUSIC CONTROL ROUTES
# ------------------------------
@app.route("/stop-music", methods=["POST"])
def stop_music_api():
    stop_music()
    return "stopped"

@app.route("/pause-music", methods=["POST"])
def pause_music_api():
    pause_music()
    return "paused"

@app.route("/resume-music", methods=["POST"])
def resume_music_api():
    resume_music()
    return "resumed"

@app.route("/play-song", methods=["POST"])
def play_song_api():
    song_name = request.form.get("song")
    if not song_name:
        return "No song selected", 400

    played_song = play_music_for_name(song_name)
    return jsonify({"song": played_song})

# ------------------------------
# VIDEO STREAMING WEBCAM
# ------------------------------
def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        # Detect emotion live (optional)
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']

        # Write emotion on frame
        cv2.putText(frame, emotion, (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

        # Encode frame
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# ------------------------------
# MAIN
# ------------------------------

if __name__ == "__main__":
    app.run(debug=True)
