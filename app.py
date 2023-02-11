from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio_file = request.files['audio_file']
    recognizer = sr.Recognizer()
    audio = sr.AudioFile(audio_file)

    with audio as source:
        audio_data = recognizer.record(source)

    text = recognizer.recognize_google(audio_data)

    return render_template('transcribe.html', text=text)

if __name__ == '__main__':
    app.run()

