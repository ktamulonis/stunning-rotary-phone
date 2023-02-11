import subprocess
from flask import Flask, request, redirect, url_for, render_template
from speech_recognition import Recognizer, AudioData

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename

    # Convert the file to PCM WAV format
    output_filename = filename.split('.')[0] + '.wav'
    subprocess.call(['ffmpeg', '-i', filename, output_filename])

    # Load the audio file into the SpeechRecognition library
    recognizer = Recognizer()
    with open(output_filename, 'rb') as f:
        audio_data = AudioData(f.read(), recognizer.sample_rate, 2)

    # Recognize the speech in the audio file
    transcribed_text = recognizer.recognize_google(audio_data)

    return render_template('result.html', text=transcribed_text)

if __name__ == '__main__':
    app.run()

