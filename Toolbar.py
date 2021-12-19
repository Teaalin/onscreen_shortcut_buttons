#!/usr/bin/env python3

from functools import partial
from pyautogui import hotkey
from tkinter import ttk
from tkinter import *
import json
import re

# Customise here instead of having config files for a single portable Toolbar.py file
# ======================================
alt_tab = "'alt','tab'" # MAC OS: "'command','shift','tab'"

highlight_colour = "#00486e"
background_colour = "#282e33"
button_colour = "#33393f"
text_colour = "white"

default_buttons = [
    "UNDO : ctrlleft,z      REDO : ctrlleft,shift,z",
    "COPY : ctrlleft,c      PASTE : ctrlleft,v",
    "TRANSFORM : ctrlleft,t",
    "DESELECT : ctrlleft,shift,a"
]

# Button size padding (positvie # only)
button_padding = [3, 8]
# Between buttons (positvie # only)
button_spacing = [2, 2]

# ======================================
# End of user customisation

X = 0
Y = 1

# Initialize and configure the window
root = Tk()
root.title("Toolbar")
root.resizable(0,0)
root.attributes("-topmost", True)

style = ttk.Style()

# Functions
def setup():
    settings = {}
    buttons = []

    # Read the user config if it exists
    try:
        file = open("toolbar_config.json", "r")
        lines = file.read()
        settings = json.loads(lines)

        if "buttons" in settings:
            buttons = settings["buttons"]
            settings.pop("buttons")
        
        load_settings(settings)
        file.close()
    except IOError:
        print("No config found, using default settings")
    except EOFError:
        print("There are no contents in the file")
    except:
        print("ERR: configuration invalid, using defaults")

    if buttons == []:
        buttons = default_buttons

    load_buttons(buttons)
    apply_settings()
    

def load_settings(settings):
    secure_varibles = ["alt_tab", "highlight_colour", "background_colour", "button_colour", "text_colour", "button_padding", "button_spacing"]

    for variable in settings.keys():
        if variable in secure_varibles:
            # yes, I know globals are bad and I should feel bad
            globals()[variable] = settings[variable]
        else:
            print("WARN config: \"" + variable + "\" is unchangable or is invalid. Skipping")

def apply_settings():
    global style
    global root
    root.configure(bg=background_colour)
    style.configure("TFrame", background=background_colour)
    style.configure("TButton", background=button_colour, foreground=text_colour, borderwidth=0, padding=(button_padding[X], button_padding[Y]))
    style.map('TButton', background=[('active', highlight_colour)])
    root.mainloop()

def load_buttons(config):
    global root

    for line in config:
        new_frame = ttk.Frame(root)
        new_frame.pack(fill="both", expand=True)

        button_config = re.findall("[^\s:]+ *: *[^\s]+", line) #"\w+ *: *[\w,']+"

        for button in button_config:
            display_string, button_hotkey = button.replace(" ", "").split(":")

            # Create a button
            ttk.Button(new_frame, text=display_string, command=partial(press_hotkey, button_hotkey)
                      ).pack(side=LEFT, fill="both", expand=True, padx=button_spacing[X], pady=button_spacing[Y])

def press_hotkey(keys):
    exec( str("hotkey("+ format_hotkey(alt_tab) +")") )
    exec( str("hotkey("+ format_hotkey(keys) +")") )

def format_hotkey(hotkeys):
    temp = "'" + hotkeys.replace(",", "','") + "'"
    return temp

setup()
