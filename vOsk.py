import vosk
import pyaudio
import json

model = vosk.Model("vosk-model-en")
rec = vosk.KaldiRecognizer(model, 16000)

def recognize_audio(data):
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        text = result.get("text", "")
        return text

def recognize_data():
    p = pyaudio.PyAudio()

    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=4000,
    )

    print("######################################################################")
    print("listening... Press Ctrl+C to exit.")
    print("######################################################################")

    try:
        while True:
            data = stream.read(4000)
            user_input = recognize_audio(data)

            if user_input and user_input.strip():#str(user_input) != "None":
                print("Recognized:", user_input)

    except KeyboardInterrupt:
        exit(1)
    finally:
        print("Program terminated.")
        stream.stop_stream()
        stream.close()
        p.terminate()

recognize_data()
