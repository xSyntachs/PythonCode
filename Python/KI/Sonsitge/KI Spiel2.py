import speech_recognition as sr

def speech_to_text():
    # Initialisiere den Spracherkennungs-Recognizer
    recognizer = sr.Recognizer()

    # Versuche, das Mikrofon zu öffnen
    with sr.Microphone() as source:
        print("Sage etwas...")
        recognizer.adjust_for_ambient_noise(source)  # Stellt das Mikrofon auf Umgebungsgeräusche ein
        audio = recognizer.listen(source)  # Hört auf die Audioeingabe

    try:
        # Verwende Google Speech Recognition, um die Sprache in Text umzuwandeln
        text = recognizer.recognize_google(audio, language='de-DE')  # Für Deutsch ändere 'de-DE' zu 'en-US' für Englisch
        print("Erkannter Text:")
        print(text)
    except sr.UnknownValueError:
        print("Die Spracherkennung konnte die Eingabe nicht verstehen.")
    except sr.RequestError as e:
        print("Ein Fehler ist aufgetreten; {0}".format(e))

while True:
    speech_to_text()
