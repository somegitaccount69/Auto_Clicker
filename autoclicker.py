import os
import time
import threading
from tkinter import *
import tkinter as tk
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

clicking = False
running = True
mouse = Controller()


def inputs():
    TRANSFORMED_TOGGLE_KEY = variable.get().lower()
    global TOGGLE_KEY
    TOGGLE_KEY = KeyCode(char=f"{TRANSFORMED_TOGGLE_KEY}")

    global cps
    cps = int(cpsSelection.get().lower())

    global button
    lebutton = buttonSelection.get().lower()
    if lebutton == "left":
        button = Button.left
    else:
        button = Button.right

def clicker():
    while running:
        if clicking:
            if cps == 5:
                mouse.click(button, 1)
                time.sleep(0.2)

            elif cps == 10:
                mouse.click(button, 1)
                time.sleep(0.09)

            elif cps == 20:
                mouse.click(button, 1)
                time.sleep(0.045)

            elif cps == 50:
                mouse.click(button, 1)
                time.sleep(0.01)

            elif cps == 100:
                mouse.click(button, 1)
                time.sleep(0.00001)
            else:
                pass


def toggle_event(key):
    if key == TOGGLE_KEY:
        inputs()
        global clicking
        clicking = not clicking


def listenin():
    with Listener(on_press=toggle_event) as listener:
        listener.join()
        if not running:
            return


click_thread = threading.Thread(target=clicker)
click_thread.start()
listening_thread = threading.Thread(target=listenin)
listening_thread.start()

Window = tk.Tk()
Window.title("Auto Clicker :)")
Window.geometry("500x200")
Window.resizable(False, False)

Title = tk.Label(text="Auto Clicker", font=('Helvatical bold', 20))
Title.grid(row="0", padx="170")

frame = tk.Frame(bg="lightskyblue", width="450", height="440", borderwidth=3, relief="solid")
frame.grid()

toggleKeySelectLabel = tk.Label(frame, text="Toggle Key:", font=('Helvatical bold', 10), bg="lightskyblue")
toggleKeySelectLabel.grid(row=2, column=0)

OPTIONS = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P"
]

variable = StringVar(frame)
variable.set(OPTIONS[0])

startKeyDropDown = tk.OptionMenu(frame, variable, *OPTIONS)
startKeyDropDown.grid(row=2, column=1)

cpsDropDownLabel = tk.Label(frame, text="CPS:", font=('Helvatical bold', 10), bg="lightskyblue")
cpsDropDownLabel.grid(row=3, column=0)

OPTIONS_2 = [
    "5",
    "10",
    "20",
    "50",
    "100"
]

cpsSelection = StringVar(frame)
cpsSelection.set(OPTIONS_2[0])

cpsSelectDropDown = tk.OptionMenu(frame, cpsSelection, *OPTIONS_2)
cpsSelectDropDown.grid(row=3, column=1)

buttonDropDownLabel = tk.Label(frame, text="Button:", font=('Helvatical bold', 10), bg="lightskyblue")
buttonDropDownLabel.grid(row=4, column=0)

OPTIONS_3 = [
    "Left",
    "Right"
]

buttonSelection = StringVar(frame)
buttonSelection.set(OPTIONS_3[0])

buttonSelectDropDown = tk.OptionMenu(frame, buttonSelection, *OPTIONS_3)
buttonSelectDropDown.grid(row=4, column=1)

inputs()


def on_closing():
    os._exit(0)


Window.protocol("WM_DELETE_WINDOW", on_closing)
Window.mainloop()
