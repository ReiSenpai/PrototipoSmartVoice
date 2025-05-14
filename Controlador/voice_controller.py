import speech_recognition as sr

class VoiceController:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
        try:
            return self.recognizer.recognize_google(audio, language="es-PE")
        except:
            return None
