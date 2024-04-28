import json

import speech_recognition
from commands import dict_commands

recognizer = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone()

with speech_recognition.Microphone() as source:
    print("Say something!")
    audio = recognizer.listen(source, 4, 4)

recognized_data = recognizer.recognize_vosk(audio, language="rus")
json_data = json.loads(recognized_data)
print(json_data["text"])
words = json_data["text"].split(" ")
for word in words:
    if word in dict_commands.keys():
        print(dict_commands[word])

