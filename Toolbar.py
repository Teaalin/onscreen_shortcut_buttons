#!/usr/bin/env python3

import tkinter
from tkinter import ttk
from pyautogui import hotkey
from functools import partial

# ===== User Variables =====
# Customise these! These will (optionally) load from a config when I set that up
alt_tab = "'alt','tab'"

active_colour = "#00486e"
background_colour = "#282e33"
button_colour = "#33393f"
text_colour = "white"
# ==========================

PADDING = 5 # padding doesn't work and I don't know why :D
buttons = []

default_config = 'UNDO "ctrlleft","z"    REDO "ctrlleft","shift","z"\n'\
                 'COPY "ctrlleft","c"    PASTE "ctrlleft","v"\n'\
                 'TRANSFORM "ctrlleft","t"\n'\
                 'DESELECT "ctrlleft","shift","a"'

# Initialize and configure the window
root = tkinter.Tk()
root.title("Toolbar")

root.resizable(0,0)
root.configure(bg=background_colour)
root.attributes("-topmost", True)

style = ttk.Style()
style.configure("TButton", background=button_colour, foreground=text_colour, borderwidth=0)
style.map('TButton', background=[('active', active_colour)])

# Functions
def main():
    lines = []
    
    try:
        file = open("toolbar_config.txt", "r")
        lines = file.readlines()
        file.close()
    except IOError:
        print("No config found, using default buttons")
        lines = default_config.split("\n")
    
    load_config(lines)

def load_config(lines):
    row = 1; col = 1; cols = 1
    max_col = count_columns(lines)
    global root

    for line in lines:
        button_config = line.split("    ")
        cols = len(button_config)
        
        for button in button_config:
            display_string, button_hotkey = button.split(" ")
            new_button = ttk.Button(root, text=display_string, command=partial(press_hotkey, button_hotkey))
            new_button.grid(row=row, column=col,ipadx=PADDING,ipady=PADDING, columnspan=int(max_col/cols), sticky="EW")
            buttons.append(new_button)
            col += 1
        row += 1
        col = 1
    root.mainloop()

def count_columns(lines):
    col = 0
    max_col = 1
    for line in lines:
        for button in line.split("    "):
            col += 1
            if col > max_col:
                max_col = col
        col = 0
    return max_col

def press_hotkey(keys):
    exec( str("hotkey("+ alt_tab +")") )
    exec( str("hotkey("+ keys +")") )

main()
