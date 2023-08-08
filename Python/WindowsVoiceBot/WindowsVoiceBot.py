import speech_recognition as sr
import pyautogui as pt
import os
import webbrowser
import psutil
import subprocess
import pyttsx3
from PyP100 import PyP100
from time import sleep
import boto3
from pydub import AudioSegment
from pydub.playback import play
from contextlib import closing

class WindowsVoiceBot:
    def __init__(self):
        self.speech_recognizer = sr.Recognizer()
        self.aws_access_key_id = 'AKIASZERDXSCA4P3CJ5T'
        self.aws_secret_access_key = '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'
        self.region_name = 'eu-central-1'
        
        session = boto3.Session(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.region_name)
        self.polly = session.client("polly")
        self.transcribe = session.client("transcribe")

    def get_script_path(self):
        return os.path.dirname(os.path.abspath(__file__))

    def speechtotext(self):
        print("Spracheingabe gestartet. Sprich etwas!")
        while True:
            with sr.Microphone() as source:
                self.speech_recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = self.speech_recognizer.listen(source)

            try:
                # Erkenne die gesprochene Sprache und verwandle sie in Text
                text = self.speech_recognizer.recognize_google(audio, language='de-DE')
                return text

            except sr.UnknownValueError:
                print("Spracherkennung konnte das gesprochene Wort nicht verstehen.")

            except sr.RequestError as e:
                print("Es ist ein Fehler bei der Anfrage an die Spracherkennungsdienste aufgetreten; {0}".format(e))

    def opencmd(self):
        pt.hotkey('win')
        sleep(0.2)
        pt.typewrite('cmd')
        pt.hotkey('Enter')   
        
    def openValorant(self):
        script_path = self.get_script_path()
        self.opencmd()
        position = None
        while not position:
            position = pt.locateOnScreen(os.path.join(script_path, "cmd.jpg"), confidence=.6)
            if position:
                pt.typewrite(r'"C:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=valorant --launch-patchline=live')
                sleep(0.1)
                pt.hotkey('Enter')
                sleep(0.1)
                pt.typewrite('taskkill /f /im cmd.exe') 
                sleep(0.1)
                pt.hotkey('Enter')
    def openDiscord(self):
        script_path = self.get_script_path()
        self.opencmd()
        position = None
        while not position:
            position = pt.locateOnScreen(os.path.join(script_path, "cmd.jpg"), confidence=.6)
            if position:
                pt.typewrite(r'C:\Users\lrumk\AppData\Local\Discord\Update.exe --processStart Discord.exe')
                sleep(0.1)
                pt.hotkey('Enter')
                sleep(0.1)
                pt.typewrite('taskkill /f /im cmd.exe') 
                sleep(0.1)
                pt.hotkey('Enter')

    def openOpera(self):
        script_path = self.get_script_path()
        self.opencmd()
        position = None
        while not position:
            position = pt.locateOnScreen(os.path.join(script_path, "cmd.jpg"), confidence=.6)
            if position:
                pt.typewrite(r'"C:\Users\lrumk\AppData\Local\Programs\Opera GX\launcher.exe"')
                sleep(0.1)
                pt.hotkey('Enter')
                sleep(0.1)
                pt.typewrite('taskkill /f /im cmd.exe') 
                sleep(0.1)
                pt.hotkey('Enter')

    def StartServer(self):
        p100 = PyP100.P100("192.168.0.131", "lrumke5@gmail.com", "Tonino2105??!")
        p100.handshake()
        p100.login()
        p100.turnOn()
        self.speak_answer("Server wurde gestartet.")

    def StopServer(self):
        p100 = PyP100.P100("192.168.0.131", "lrumke5@gmail.com", "Tonino2105??!")
        p100.handshake()
        p100.login()
        p100.turnOff()
        self.speak_answer("Server wurde gestoppt.")

    def handle_additional_commands(self, text):
        if "schließe discord" in text.lower() or "beende discord" in text.lower():
            self.closeDiscord()
        elif "suche im web nach" in text.lower() or "suche nach" in text.lower():
            search_query = text.lower().replace("suche im web nach", "").replace("suche nach", "")
            self.searchWeb(search_query)
        elif "suche auf youtube nach" in text.lower():
            search_query = text.lower().replace("suche auf youtube nach", "")
            self.searchYoutube(search_query)
        elif "spiele musik" in text.lower() or "musik abspielen" in text.lower():
            self.playMusic()
        elif "minimiere fenster" in text.lower():
            self.minimizeWindow()
        elif "maximiere fenster" in text.lower():
            self.maximizeWindow()
        elif "sperr den bildschirm" in text.lower() or "bildschirm sperren" in text.lower():
            self.lockScreen()
        elif "erstelle notiz" in text.lower():
            self.createNote()
        elif "lese notiz vor" in text.lower() or "vorlesen" in text.lower():
            self.readNote()
        elif "beende programm" in text.lower() or "programm beenden" in text.lower():
            self.exitProgram()
        else:
            pass

    def closeDiscord(self):
        for proc in psutil.process_iter(['pid', 'name']):
            if "discord" in proc.info['name'].lower():
                pid = proc.info['pid']
                process = psutil.Process(pid)
                process.terminate()
                self.speak_answer("Discord wird geschlossen.")
                return

        self.speak_answer("Discord ist nicht geöffnet.")

    def searchWeb(self, query):
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
        self.speak_answer(f"Suche im Web nach: {query}")

    def searchYoutube(self, query):
        search_url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(search_url)
        self.speak_answer(f"Suche auf YouTube nach: {query}")

    def playMusic(self):
        self.speak_answer("Welches Lied möchtest du hören?")
        song_name = self.speechtotext()
        self.speak_answer(f"Suche auf YouTube nach: {song_name}")
        
        search_query = song_name.replace(" ", "+")  # Leerzeichen durch + ersetzen, um es für die URL geeignet zu machen
        search_url = f"https://www.youtube.com/results?search_query={search_query}"
        webbrowser.open(search_url)
        
        sleep(3)  # Kurz warten, um das Laden der Seite abzuschließen
        pt.moveTo(800, 320)  # Position des ersten Videos in den Suchergebnissen anpassen
        pt.click()

    def minimizeWindow(self):
        pt.hotkey('win', 'down')  # Minimiert das aktive Fenster

    def maximizeWindow(self):
        pt.hotkey('win', 'up')  # Maximiert das aktive Fenster

    def lockScreen(self):
        pt.hotkey('win', 'l')  # Sperrt den Bildschirm

    def createNote(self):
        file_path = "C:/Users/lrumk/Desktop/Notizen.txt"  # Passe den Pfad entsprechend an
        note_text = input("Gib den Text für die Notiz ein: ")
        with open(file_path, "a") as f:
            f.write(note_text + "\n")
        self.speak_answer("Notiz wurde erstellt.")

    def readNote(self):
        file_path = "C:/Users/lrumk/Desktop/Notizen.txt"  # Passe den Pfad entsprechend an
        with open(file_path, "r") as f:
            notes = f.readlines()
            if notes:
                self.speak_answer("Notizen:")
                for idx, note in enumerate(notes, 1):
                    self.speak_answer(f"{idx}. {note.strip()}")
            else:
                self.speak_answer("Keine Notizen vorhanden.")

    def exitProgram(self):
        self.speak_answer("Das Programm wird beendet.")
        exit()

    def speak_answer(self, answer):
        response = self.polly.synthesize_speech(
            Text=answer,
            OutputFormat="pcm",
            VoiceId="Daniel",
            Engine="neural"
        )
        if "AudioStream" in response:
            with closing(response["AudioStream"]) as stream:
                audio = AudioSegment.from_file(stream, format="raw", frame_rate=16000, channels=1, sample_width=2)
                play(audio)


if __name__ == "__main__":
    voice_bot = WindowsVoiceBot()
    while True:
        text = voice_bot.speechtotext()
        print(text)
        if "starte discord" in text.lower() or "öffne discord" in text.lower():
            voice_bot.openDiscord()
        elif "starte opera" in text.lower() or "öffne opera" in text.lower() or "starte browser" in text.lower() or "öffne browser" in text.lower():    
            voice_bot.openOpera()
        elif "starte shooter" in text.lower() or "starte valorant" in text.lower():
            voice_bot.openValorant()
        elif "starte server" in text.lower():
            voice_bot.StartServer()
        elif "stoppe server" in text.lower():
            voice_bot.StopServer()
        else:
            voice_bot.handle_additional_commands(text)
