#!/usr/bin/env python3

import re
import tkinter
from functools import partial
from pyautogui import hotkey
from tkinter import ttk

import random

# Customise here instead of having config files for a single portable Toolbar.py file
# ======================================
alt_tab = "'alt','tab'" # MAC OS: "'command','shift','tab'"

highlight_colour = "#00486e"
background_colour = "#282e33"
button_colour = "#33393f"
text_colour = "white"

default_config = 'undo "ctrlleft","z"    redo "ctrlleft","shift","z"\n'\
                 'copy "ctrlleft","c"    paste "ctrlleft","v"\n'\
                 'transform "ctrlleft","t"\n'\
                 'deselect "ctrlleft","shift","a"'

button_border = 1
# Padding on the left and right of the button
PADX = 10
# Padding on the top and buttom of the button
PADY = 8
# Stickies the buttons to left and right sides, change to "" if you don't want stretched buttons
stick = "EW" # set with variations of "NSEW" or ""
# ======================================
# End of user customisation

frames = []
borders = []
buttons = []

# Initialize and configure the window
root = tkinter.Tk()
root.title("Toolbar")
root.resizable(0,0)
root.attributes("-topmost", True)

style = ttk.Style()
style.configure("TFrame", background="black") #temporary for debugging

# TODO:
#   make the config better
#       - merge the configs together
#       - remove spacing requirements and use regex
#       - save last screen position

# Functions
def setup():
    alt_tab, highlight_colour, background_colour, button_colour, text_colour, PADX, PADY, stick, root, style

    # Read the user config if it exists
    try:
        file = open("user_config.txt", "r")
        lines = file.readlines()

        if len(lines) < 1:
            raise EOFError

        secure_varibles = ["alt_tab", "highlight_colour", "background_colour", "button_colour", "text_colour", "button_border", "PADX", "PADY", "stick"]
        settings = re.findall(r"(\w+) *= *([\w#'\",]+)", str(lines))

        for variable, value in settings:
            if not variable in secure_varibles:
                print("WARN config: \"" + variable + "\" is unchangable or is invalid. Skipping")
            else:
                # yes, I know globals are bad and I should feel bad
                exec(str("globals()['" + variable + "']=" + value))
                #exec(str(variable + "=" + value)) #variable + "=" + value)
            
        file.close()
    except IOError:
        print("No user config found, using default settings")
    except EOFError:
        print("There are no contents in the file")

    # Apply configuration
    root.configure(bg=background_colour)
    style.configure("TButton", background=button_colour, foreground=text_colour, borderwidth=0, padding=(PADX, PADY))
    style.configure("TFrame", background="black")
    style.map('TButton', background=[('active', highlight_colour)])

def main():
    lines = []

    try:
        file = open("toolbar_config.txt", "r")
        lines = file.readlines()
        file.close()
    except IOError:
        print("No toolbar config found, using default buttons")
        lines = default_config.split("\n")
    
    load_config(lines)

def load_config(lines):
    row = 1; col = 1; cols = 1
    global root

    for line in lines:
        button_config = line.split("    ")

        new_frame = ttk.Frame(root)#, border=button_border)
        new_frame.grid(row=row, sticky=stick)
        frames.append(new_frame)

        for button in button_config:
            # Create a frame for the button so that it can have a "border"
            border_frame = ttk.Frame(new_frame, borderwidth=button_border)
            border_frame.grid(row=row, column=col, sticky=stick)
            borders.append(border_frame)

            # Create the button
            display_string, button_hotkey = button.split(" ")
            new_button = ttk.Button(border_frame, text=display_string, command=partial(press_hotkey, button_hotkey))
            new_button.grid(sticky="NSEW")
            buttons.append(new_button)
            col += 1

        row += 1
        col = 1
    root.mainloop()

def press_hotkey(keys):
    exec( str("hotkey("+ alt_tab +")") )
    exec( str("hotkey("+ keys +")") )

setup()
main()
