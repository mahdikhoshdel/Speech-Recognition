import pyaudio
import wave
import speech_recognition
from commands import Commander

running = True

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

r = speech_recognition.Recognizer()
cmd = Commander()

def initSpeech():
    print("Wait...")

    with speech_recognition.Microphone() as source:
        print("Say somthing !")
        play_audio("./audio/confident.wav")
        audio = r.listen(source=source)

    play_audio("./audio/case-closed.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand broh")

    print("Your command is:")
    print(command)
    if command in ["stop", "quit", "exit", "bye", "goodbye"]:
        global running
        running = False

    cmd.discover(command)

while running == True :
    initSpeech()

