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

# Functions
def setup():
    settings = []
    buttons = []

    # Read the user config if it exists
    try:
        file = open("toolbar_config.txt", "r")
        lines = file.read()
        settings = re.findall(r"settings:{\s*(\w.*?)}", lines, re.DOTALL)[0].replace(" ", "")
        buttons = re.findall(r"buttons:{\s*(\w.*?)}", lines, re.DOTALL)[0]

        load_settings(settings)
        
        file.close()
    except IOError:
        print("No config found, using default settings")
        buttons = default_config.split("\n")
    except EOFError:
        print("There are no contents in the file")
        buttons = default_config.split("\n")
    except:
        print("ERR: configuration invalid, using defaults")

    if buttons == []:
        buttons = default_config.split("\n")

    load_buttons(buttons)
    
    # Apply configuration
    global style
    global root
    root.configure(bg=background_colour)
    style.configure("TButton", background=button_colour, foreground=text_colour, borderwidth=0, padding=(PADX, PADY))
    #style.configure("TFrame", background="black")
    style.map('TButton', background=[('active', highlight_colour)])
    root.mainloop()

def load_settings(lines):
        secure_varibles = ["alt_tab", "highlight_colour", "background_colour", "button_colour", "text_colour", "button_border", "PADX", "PADY", "stick"]
        settings = re.findall(r"(\w+) *= *([\w#'\",]+)", lines, re.DOTALL)
        print(settings)
        for line in settings:
            #for variable, value in line: # 2 is > 2 apparently 
            variable = line[0]
            value = line[1]
            if not variable in secure_varibles:
                print("WARN config: \"" + variable + "\" is unchangable or is invalid. Skipping")
            else:
                # yes, I know globals are bad and I should feel bad
                exec(str("globals()['" + variable + "']=" + value))

def load_buttons(lines):
    row = 1; col = 1; cols = 1
    global root

    for line in lines.split('\n'):
        button_config = re.findall("\w+ *: *[\w,']+", line)

        new_frame = ttk.Frame(root)
        new_frame.grid(row=row, sticky=stick)
        frames.append(new_frame)

        for button in button_config:
            # Create a frame for the button so that it can have a "border"
            border_frame = ttk.Frame(new_frame, borderwidth=button_border)
            border_frame.grid(row=row, column=col, sticky=stick)
            borders.append(border_frame)

            # Create the button
            display_string, button_hotkey = button.replace(" ", "").split(":")
            
            new_button = ttk.Button(border_frame, text=display_string, command=partial(press_hotkey, button_hotkey))
            new_button.grid(sticky="NSEW")
            buttons.append(new_button)
            col += 1

        row += 1
        col = 1

def press_hotkey(keys):
    exec( str("hotkey("+ alt_tab +")") )
    print( str("hotkey("+ keys +")") )
    exec( str("hotkey("+ keys +")") )

setup()
