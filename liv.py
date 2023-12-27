import speech_recognition as sr
import pyaudio
import json

def recognize_audio(recognizer, audio_data):
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return ""

def recognize_data():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("######################################################################")
    print("listening... Press Ctrl+C to exit.")
    print("######################################################################")

    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            while True:
                audio_data = recognizer.listen(source, timeout=None)
                user_input = recognize_audio(recognizer, audio_data)

                if user_input and user_input.strip():
                    print("Recognized:", user_input)

    except KeyboardInterrupt:
        exit(1)
    finally:
        print("Program terminated.")

if __name__ == "__main__":
    recognize_data()

