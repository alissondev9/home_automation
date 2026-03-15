import speech_recognition as sr

def ouvir_voz():
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic, duration=1)
        print(">>> Ouvindo...")
        audio = rec.listen(mic)
    
    try:
        texto = rec.recognize_google(audio, language='pt-BR')
        return texto.lower()
    except:
        return ""