from deepface import DeepFace

def detect_emotion_from_frame(frame):
    """
    Detect dominant emotion from a given webcam frame.
    No new webcam is opened, no OpenCV window is shown.
    :param frame: OpenCV frame from existing camera
    :return: dominant emotion as string
    """
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        
        # DeepFace sometimes returns list, sometimes dict
        if isinstance(result, list):
            emotion = result[0].get("dominant_emotion", "neutral")
        else:
            emotion = result.get("dominant_emotion", "neutral")
        
        return emotion

    except Exception as e:
        print("❌ DeepFace error:", e)
        return "neutral"
