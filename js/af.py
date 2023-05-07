




def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Silahkan katakan sesuatu...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='id-ID')
            print(f"Anda berkata: {text}")
        except:
            print("Maaf, saya tidak bisa mendengar Anda.")
            text = ""
        return text.lower()


def respond(text):
    if 'hai' in text:
        speak("Halo, apa yang bisa saya bantu?")
    elif 'wikipedia' in text:
        speak("Mencari informasi di Wikipedia...")
        text = text.replace("wikipedia", "")
        results = wikipedia.summary(text, sentences=3)
        speak("Menurut Wikipedia, ")
        speak(results)
    elif 'buka' in text:
        website = text.split(' ')[-1]
        speak(f"Membuka {website}...")
        webbrowser.open_new_tab(f"http://{website}.com")
    elif 'waktu' in text:
        now = datetime.datetime.now()
        speak(f"Sekarang jam {now.hour}:{now.minute}")
    elif 'stop' in text:
        speak("Baiklah, sampai jumpa!")
        exit()
    else:
        speak("Maaf, saya tidak bisa melakukannya.")

while True:
    text = listen()
    respond(text)