import pyttsx3

class SpeechEngine:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 160)
        self.last_spoken = None

    def speak(self, gesture):
        if gesture != self.last_spoken:
            print(f"[SPEAKING] {gesture}")
            self.engine.say(gesture)
            self.engine.runAndWait()
            self.last_spoken = gesture
