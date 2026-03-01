import os
import random
import pygame

pygame.mixer.init()  # Initialize mixer globally

# ------------------------------
# PLAY MUSIC BASED ON EMOTION
# ------------------------------
def play_music(emotion_or_song):
    """
    Play a song based on emotion or a specific song path/name.
    Returns the actual song name being played.
    """
    try:
        # If emotion_or_song is a full path (clicked song), play directly
        if os.path.isfile(emotion_or_song):
            song_path = emotion_or_song
            selected_song = os.path.basename(song_path)
        else:
            # Treat as emotion folder
            base_path = "music"
            emotion_folder = os.path.join(base_path, str(emotion_or_song).lower())
            if not os.path.exists(emotion_folder):
                print("❌ Emotion folder not found!")
                return None

            songs = [f for f in os.listdir(emotion_folder) if f.endswith(".mp3")]
            if not songs:
                print("❌ No MP3 files found!")
                return None

            selected_song = random.choice(songs)
            song_path = os.path.join(emotion_folder, selected_song)

        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        print(f"🎵 Now Playing: {selected_song}")
        return selected_song

    except Exception as e:
        print("❌ Offline Music Error:", e)
        return None


# ------------------------------
# PLAY A SPECIFIC SONG BY NAME
# ------------------------------
def play_music_for_name(song_name):
    """
    Play a specific song by name. Searches all emotion folders.
    Returns the actual song name.
    """
    try:
        base_path = "music"
        found = False

        for folder in os.listdir(base_path):
            folder_path = os.path.join(base_path, folder)
            if os.path.isdir(folder_path):
                song_path = os.path.join(folder_path, song_name)
                if os.path.exists(song_path):
                    pygame.mixer.music.load(song_path)
                    pygame.mixer.music.play()
                    print(f"🎵 Now Playing: {song_name}")
                    found = True
                    return song_name

        if not found:
            print("❌ Song not found!")
            return None

    except Exception as e:
        print("❌ Error playing song:", e)
        return None
# ------------------------------
# MUSIC CONTROLS
# ------------------------------
def stop_music():
    pygame.mixer.music.stop()
    print("⏹ Music stopped")


def pause_music():
    pygame.mixer.music.pause()
    print("⏸ Music paused")


def resume_music():
    pygame.mixer.music.unpause()
    print("▶ Music resumed")
