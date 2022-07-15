import flask
from subprocess import run, PIPE

import speech_recognition as sr
from flask import logging, Flask, render_template, flash, redirect
from subprocess import run, PIPE
import os
from flask import request, abort, render_template
from flask import send_file, send_from_directory
import video_structuring as vy
import librosa
import deep_speech as deep_speech
import cmu_sphinx as cmu_sphinx
import audioop
from flask_cors import CORS
import wave
from werkzeug.utils import secure_filename

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

#app = Flask(__name__)
app.secret_key = "VatsalParsaniya"

# Return home page
@app.route('/')
def index():
    flash(" Welcome to Solution")
    return render_template('index.html')


#recognize_google() for Google Web Speech API: Using Google Web Speech API (this API comes by default upto some functionalities)
@app.route('/audio', methods=['POST'])
def audio():
    r = sr.Recognizer()
    with open('upload/audio.wav', 'wb') as f:
        f.write(request.data)
  
    with sr.AudioFile('upload/audio.wav') as source:
        audio_data = r.record(source)
        # Speech recognition using Google Speech Recognitiontry: recog = r.recognize_google(audio, language = 'en-US')
        text = r.recognize_google(audio_data, language='en-IN', show_all=True)
        print(text)
        return_text = " Did you say : <br> "
        try:
            for num, texts in enumerate(text['alternative']):
                return_text += str(num+1) +") " + texts['transcript']  + " <br> "
        except:
            return_text = " Sorry!!!! Voice not Detected "
        
    return str(return_text)


# Speech to Text
def combine(method, name):
    path = "Files/"
    video =  name
    audio, transcript = vy.home(path, video)
    res = ""
    #Calling Models
    if method=='deepspeech':
        res = deep_speech.func(audio, transcript)
    elif method=='cmu':
        res = cmu_sphinx.func(audio, transcript)
    return(res)

@app.route('/Speech_to_text/')
def index1():
    return render_template('index1.html')
    

@app.route('/generate_transcript', methods=['POST'])
def home():
    #print(request.get_data())
    print('form',request.form)
    file=request.files['file']
    model=request.form['method']
    print(model)
    #get the input audio
    if request.method == "POST":
        with open('audio.wav', 'wb') as f:
            #print(file.read())
            f.write(file.read())
        print('file uploaded successfully')
        f.close()

#file not found
    if 'file' not in request.files:
        print('file',request.files)
        abort(400)

    elif 'method' not in request.form:
        print('method',request.form)
        abort(400)

    print(request.files)
    file_request = request.files['file']
    content_type_file = file_request.content_type

    print(file_request)
    print(request.form['method'])

    if "video" in content_type_file:
        print("video")
    elif "audio" in content_type_file:
        print("audio")
    else:
        abort(403)

    """

    filename = secure_filename(file_request.filename)
    file_request.save(os.path.join('Files/Video', filename))
    print("saved file successfully")
    """
    video_name = 'audio.wav'
    audioFile = wave.open(video_name, 'r')
    n_frames = audioFile.getnframes()
    audioData = audioFile.readframes(n_frames)
    originalRate = audioFile.getframerate()
    af = wave.open('audioData.wav', 'w')
    af.setnchannels(1)
    #get the audio and convert in frames 
    af.setparams((1, 2, 16000, 0, 'NONE', 'Uncompressed'))
    converted = audioop.ratecv(audioData, 2, 1, originalRate, 16000, None)
    af.writeframes(converted[0])
    af.close()
    audioFile.close()
    video_name='audioData.wav'
    #audioFile.close()

    #w=wave.open(video_name,'r')

    print('channels',audioFile.getnchannels())

    #print(video_name)

    return(combine(model, video_name))
@app.route('/download_transcript', methods=['GET'])
def download():
    return send_file(os.path.join('Files/Transcript/output.txt'), attachment_filename="output.txt", as_attachment=True)


#vvoice2text

#return route
@app.route('/vvoice2text/static/js/WebAudioRecorderWav.min.js')
def send_report():
    return send_from_directory('static','js/WebAudioRecorderWav.min.js')

@app.route("/vvoice2text/", methods=["GET", "POST"])
def index2():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
                #transcribe using google web speech API
            transcript = recognizer.recognize_google(data, key=None)

    return render_template('index2.html', transcript=transcript)

@app.route('/vvoice2text/static/s2t1.png')
def send_image():
    return send_from_directory('static','s2t1.png')

	
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002', threaded=True)
    
