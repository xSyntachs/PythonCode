import os
import keyboard
import pyautogui
import pyperclip
from plyer import notification
from pytube import YouTube

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
        
        show_notification('Download gestartet', f"Download wird in Downloads gespeichert")
        link = pyperclip.paste()
        yt = YouTube(link)
        ys = yt.streams.get_highest_resolution()
        # Angabe des Zielverzeichnisses, in dem das Video gespeichert werden soll
        download_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
        ys.download(output_path=download_folder)

        # Den Ordner öffnen
        os.startfile(download_folder)

    except Exception as e:
        show_notification('Fehler beim Download', f"Es ist ein Fehler aufgetreten: {str(e)}")


keyboard.add_hotkey("ctrl+alt+d", download_video)

keyboard.wait()
