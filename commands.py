import win32com.client
from result import Fetcher

class Commander:
    def __init__(self):
        self.confirm = ["yes", "yeah", "yea", "hell yeah", "sure", "confirm", "do it"]
        self.cancel = ["no", "negative", "don't", "dont", "cancel", "hell no"]

    def tts(self, text):
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.speak(text)

    def respond(self, response):
        print(response)
        self.tts(response)

    def discover(self, text):
        if "what" and "name" in text:
            if "my" in text:
                self.respond("You haven't told me your name yet")
            else:
                self.respond("My name is python commander. How are you?")
        else:
            f = Fetcher("https://www.bing.com/search?q=" + text)
            result = f.lookup()
            self.respond(result)
