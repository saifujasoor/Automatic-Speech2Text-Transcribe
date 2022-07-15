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
<br> Visit Mozilla DeepSpeech github for more info.

## 2. CMU Sphinx
CMUSphinx is an open source speech recognition system for mobile and server applications. Supported languages: C, C++, C#, Python, Ruby, Java, Javascript.
<br> In SpeechRecognition library, there are different methods for recognizing speech from an audio source using various APIs. These APIs use different third party services to detect speech.
Below  are the methods of SpeechRecognition library:
- recognize_google() for Google Web Speech API: Using Google Web Speech API (this API comes by default upto some functionalities)
- recognize_google_cloud() for Google Cloud Speech API: Using Google Cloud Speech API.
- recognize_sphinx() for CMUSphinx: Using CMU Sphinx – requires installing PocketSphinx
- recognize_wit() for WIT.AI: Using speech recognition service provided by wit.ai
- IBM Speech to Text: SpeechRecognition’s method recgonize_ibm() didn’t work due to credential issue as IBM has udpated the credential system. So we didn’t use it. Instead we used IBM’s library for that.
<br> Visit www.pragnakalp.com for more info.

## Real Time Speech to Text
recognize_google()  method of speech recognition has used for real time speech to text transcribe.

## 💻Technology Stack which i have used in project###
- Frontend : HTML, BOOTSTRAP, Recorder.js, AudioDisplay.js
- Backend : Flask


