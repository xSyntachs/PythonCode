import keyboard
import youtube_dl
import pyautogui
import pyperclip
from plyer import notification
import os

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=10,
    )

def download_video():
    try:
        # Bewege die Maus zum Adressfeld des Browsers
        pyautogui.click(x=400, y=50)
        # Markiere die URL im Adressfeld
        pyautogui.hotkey('ctrl', 'a')
        # Kopiere die URL in die Zwischenablage
        pyautogui.hotkey('ctrl', 'c')
        # Lese die URL aus der Zwischenablage
        video_url = pyperclip.paste()
        video_info = youtube_dl.YoutubeDL().extract_info(
            url=video_url, download=False
        )
        filename = f"{video_info['title']}.mp3"
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename,
        }

        # Zeige Benachrichtigung an, dass der Download begonnen hat
        show_notification('Download gestartet', f"Der Download von {video_info['title']} hat begonnen.")

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        # Zeige Benachrichtigung an, dass der Download abgeschlossen ist
        show_notification('Download abgeschlossen', f"Der Download von {video_info['title']} ist abgeschlossen.")

        # Öffne den Ordner, in dem sich die heruntergeladene Datei befindet
        folder_path = os.path.dirname(os.path.abspath(filename))
        os.startfile(folder_path)

    except Exception as e:
        # Zeige Benachrichtigung an, dass ein Fehler aufgetreten ist
        show_notification('Fehler beim Download', f"Es ist ein Fehler aufgetreten: {str(e)}")

# Ersetze die Tastenkombination durch die gewünschte Tastenkombination
keyboard.add_hotkey("ctrl+alt+d", download_video)

# Das Skript läuft, bis es gestoppt wird
keyboard.wait()
