import pyttsx3

def speak_text(voice):
  engine = pyttsx3.init()
  rate = engine.getProperty('rate')
  engine.setProperty('rate', rate + 1)
  engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')
  engine.say(voice)

  engine.runAndWait()
  engine.stop()