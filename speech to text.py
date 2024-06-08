import speech_recognition as sr

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`."""
    # Adjust for ambient noise and record audio
    with microphone as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for your speech...")
        audio_data = recognizer.listen(source)

    # Attempt to recognize the speech
    try:
        print("Recognizing your speech...")
        text = recognizer.recognize_google(audio_data)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand your speech.")
    except sr.RequestError:
        print("Could not request results; check your internet connection.")

if __name__ == "__main__":
    # Initialize recognizer and microphone
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Continuously listen and recognize speech
    while True:
        recognize_speech_from_mic(recognizer, microphone)
        print("\nReady for the next speech input...\n")
