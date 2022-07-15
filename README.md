# Automatic-Speech2Text-Transcribe
Speech Recognition is a part of Natural Language Processing which is a subfield of Artificial Intelligence. In Speech Recognition, spoken words/sentences are translated into text by computer. It is also known as Speech to Text (STT).

I have designed  web app in flask that allows us to real time speech to text transcribe and also record our voice from the web browser and convert it to text and save the output  text in disk.

## Models
I have used two pretrained models to transcribe voice to text.
1. DeepSpeech
2. CMU Sphinx

## 1. DeepSpeech
DeepSpeech is an open source Speech-To-Text engine, using a model trained by machine learning techniques based on Baidu's Deep Speech research paper. Project DeepSpeech uses Google's TensorFlow to make the implementation easier.
DeepSpeech is a neural network architecture first published by a research team at Baidu. In 2017, Mozilla created an open source implementation of this paper - dubbed “Mozilla DeepSpeech”.
- - Visit  [Mozilladeepspeech. ]([https://www.pragnakalp.com/speech-recognition-speech-to-text-python-using-google-api-wit-ai-ibm-cmusphinx/#:~:text=3.-,CMUSPHINX,due%20to%20missing%20swig%20file](https://github.com/mozilla/DeepSpeech.) for more info.

## 2. CMU Sphinx
CMUSphinx is an open source speech recognition system for mobile and server applications. Supported languages: C, C++, C#, Python, Ruby, Java, Javascript.
<br> In SpeechRecognition library, there are different methods for recognizing speech from an audio source using various APIs. These APIs use different third party services to detect speech.
Below  are the methods of SpeechRecognition library:
- recognize_google() for Google Web Speech API: Using Google Web Speech API (this API comes by default upto some functionalities)
- recognize_google_cloud() for Google Cloud Speech API: Using Google Cloud Speech API.
- recognize_sphinx() for CMUSphinx: Using CMU Sphinx – requires installing PocketSphinx
- recognize_wit() for WIT.AI: Using speech recognition service provided by wit.ai
- IBM Speech to Text: SpeechRecognition’s method recgonize_ibm() didn’t work due to credential issue as IBM has udpated the credential system. So we didn’t use it. Instead we used IBM’s library for that.
- - Visit  [pragnakalp.](https://www.pragnakalp.com/speech-recognition-speech-to-text-python-using-google-api-wit-ai-ibm-cmusphinx/#:~:text=3.-,CMUSPHINX,due%20to%20missing%20swig%20file.) for more info.

## Real Time Speech to Text
recognize_google()  method of speech recognition has used for real time speech to text transcribe.

## 💻Technology Stack which i have used in project###
- Frontend : HTML, BOOTSTRAP, Recorder.js, AudioDisplay.js
- Backend : Flask

## Getting Started

### Prerequisites
Make sure you have Python, Flask installed on your system to run this project.

### Execution guide
1. Download/clone  the contents of the repository
2.  Create and activate a virtual envirnoment
3. Install the necessary prerequisites are by following command:-

```
pip3 install -r requirements.txt

```
 
4- Install DeepSpeech and Speechrecognition
```
pip3 install deepspeech==0.6.0

pip3 install SpeechRecognition
```

5- Download and unzip en-US deepspeech model, this will take a while
```
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.6.0/deepspeech-0.6.0-models.tar.gz

tar -xvzf deepspeech-0.6.0-models.tar.gz
```
6- Install Python interface to CMU Sphinxbase and Pocketsphinx libraries
```
pip3 install pocketsphinx
```
- If you getting any type error
- Make sure you have up-to-date versions of pip, setuptools and wheel
```
python -m pip install --upgrade pip setuptools wheel

pip3 install --upgrade pocketsphinx
```

- If you getting any error during installation  as below :-
```
ake: Entering directory '/opt/assistant-relay/node_modules/speaker/build'
  CC(target) Release/obj.target/output/deps/mpg123/src/output/alsa.o
../deps/mpg123/src/output/alsa.c:19:10: fatal error: alsa/asoundlib.h: No such file or directory
 #include <alsa/asoundlib.h>
          ^~~~~~~~~~~~~~~~~~
compilation terminated.
```
To solve this problem, Try to install below prerequisite.
```
sudo apt-get install libasound2-dev
```
Else try to install 
```
sudo apt-get install -y python python-dev python-pip build-essential swig git libpulse-dev
``` 
Then install Pocketsphinx library.

7. Type the following command inside the directory on your terminal
  ```
  python3 mainfile.py
  ```
  
4. Click http://127.0.0.1:5002 (Press CTRL+C to quit)

## Project Demo

