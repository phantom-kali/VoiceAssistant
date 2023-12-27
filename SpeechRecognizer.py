import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.energy_threshold = 900

def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = recognizer.listen(source)
            info = recognizer.recognize_google(voice)
            print('Recognized:', info)
            return info.lower()

    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    result = get_info()
    print(result)
