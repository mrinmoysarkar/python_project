def speak(data):
    from gtts import gTTS
    import os
    tts = gTTS(text=data, lang='en')
    tts.save("hello.mp3")
    os.system("cvlc --play-and-exit hello.mp3")
