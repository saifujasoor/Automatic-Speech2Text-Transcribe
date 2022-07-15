import speech_recognition as sr
#function to take the audion and transcribe using recognize_sphinx()
def func(audio_file, transcript):
    r = sr.Recognizer()

    audioFile = sr.AudioFile(audio_file)

    with audioFile as source:
        audio = r.record(source)
    #recognize_sphinx() for CMUSphinx: Using CMU Sphinx – requires installing PocketSphinx        
    text = r.recognize_sphinx(audio)
    with open("Files/Transcript/output.txt", "w+") as f:
        f.write(text)
    return(text)