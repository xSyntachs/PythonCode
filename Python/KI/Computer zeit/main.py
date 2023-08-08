import time
import threading
import plyer
from pynput import keyboard, mouse
import tkinter as tk
from tkinter import simpledialog
import csv
from datetime import datetime

root = tk.Tk()
root.withdraw()
counter = 0
eat_counter = 0
last_activity = time.time()

def check_time():
    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min
    return current_hour, current_minute

def on_press(key):
    global last_activity
    last_activity = time.time()

def on_move(x, y):
    global last_activity
    last_activity = time.time()

def update_counter():
    global counter
    while True:
        if time.time() - last_activity < 120:
            counter += 1
        time.sleep(1)

def update_eat_counter():
    global eat_counter
    while True:
        if time.time() - last_activity < 120:
            eat_counter += 1
        time.sleep(1)

def get_calorie_recommendation():
    current_hour, current_minute = check_time()
    if 5 <= current_hour < 15:
        return "Es ist Frühstückszeit! Eine empfohlene Kalorienzufuhr beträgt 400-500 kcal."
    elif 15 <= current_hour < 19:
        return "Es ist Mittagszeit! Eine empfohlene Kalorienzufuhr beträgt 600-700 kcal."
    elif 19 <= current_hour < 24:
        return "Es ist Abendessenzeit! Eine empfohlene Kalorienzufuhr beträgt 500-600 kcal."
    else:
        return "Es ist keine Hauptmahlzeit. Versuche einen gesunden Snack mit etwa 200 kcal zu essen."

keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_move=on_move)
keyboard_listener.start()
mouse_listener.start()

counter_thread = threading.Thread(target=update_counter)
counter_thread.start()

eat_counter_thread = threading.Thread(target=update_eat_counter)
eat_counter_thread.start()

last_eat = simpledialog.askinteger("Letze Mahlzeit", "Vor wieviel Minuten hast du das letzte mal was gegessen?")
eat_counter = last_eat * 60

while True:
    current_hour, current_minute = check_time()

    if counter > 7199:
        plyer.notification.notify(title="Pause", message="Es ist zeit für eine Pause")
        counter = 0

    if eat_counter > 14400:
        recommendation = get_calorie_recommendation()
        plyer.notification.notify(title="Essen", message=f"Es ist Zeit etwas zu essen. {recommendation}")
        eat_counter = 0

    if current_hour == 15 and current_minute == 0:
        plyer.notification.notify(title="Pause", message="Es ist zeit für eine Pause")
