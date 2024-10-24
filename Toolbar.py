#!/usr/bin/env python3

from functools import partial
from pyautogui import hotkey
import tkinter as tk
import json
import re
import os

# Customise here instead of having config files for a single portable Toolbar.py file
# ======================================
alt_tab = "alt,tab"  # MAC OS: "'command','shift','tab'"

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

# Button size padding (positive # only)
button_padding = [3, 8]
# Between buttons (positive # only)
button_spacing = [2, 2]

# Directory where icon files are stored
icon_directory = "icons"  # You can change this path to wherever your icons are stored.

# ======================================
# End of user customisation

X = 0
Y = 1

# Initialize and configure the window
root = tk.Tk()
root.title("Toolbar")
root.resizable(True, True)
root.attributes("-topmost", True)
root.minsize(160, 100)

# List to store icon references so they are not garbage collected
icon_images = []

# Functions
def setup():
    settings = {}
    buttons = []

    # Read the user config if it exists
    try:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "toolbar_config.JSON"), "r") as file:
            settings = json.load(file)

        if "buttons" in settings:
            buttons = settings["buttons"]
            settings.pop("buttons")

        load_settings(settings)
    except (IOError, EOFError):
        print("No config found, using default settings")
    except json.JSONDecodeError:
        print("ERR: configuration invalid, using defaults")

    if not buttons:
        buttons = default_buttons

    load_buttons(buttons)
    apply_settings()

def load_settings(settings):
    secure_variables = ["alt_tab", "highlight_colour", "background_colour", "button_colour", "text_colour", "button_padding", "button_spacing"]

    for variable in settings.keys():
        if variable in secure_variables:
            globals()[variable] = settings[variable]
        else:
            print(f"WARN config: \"{variable}\" is unchangable or is invalid. Skipping")

def apply_settings():
    global root
    root.configure(bg=background_colour)

    # Update button styles manually as tk.Button does not use ttk.Style
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button):
            widget.configure(bg=button_colour, fg=text_colour, bd=0)
            widget.bind("<Enter>", lambda e: e.widget.configure(bg=highlight_colour))
            widget.bind("<Leave>", lambda e: e.widget.configure(bg=button_colour))

    root.mainloop()

def load_buttons(config):
    global root, icon_images

    for line in config:
        new_frame = tk.Frame(root, bg=background_colour)
        new_frame.pack(fill="both", expand=True)

        button_config = re.findall(r"[^\s:]+ *: *[^\s]+", line)  # "\w+ *: *[\w,']+"

        for button in button_config:
            display_string, button_hotkey = button.replace(" ", "").split(":")

            # Check if the display string is uppercase and if a corresponding .png file exists
            icon_path = os.path.join(icon_directory, f"{display_string.lower()}.png")
            if display_string.isupper() and os.path.exists(icon_path):
                try:
                    # Load the image and create a button with the icon
                    icon_image = tk.PhotoImage(file=icon_path)
                    icon_images.append(icon_image)  # Store a reference to prevent garbage collection
                    tk.Button(new_frame, image=icon_image, command=partial(press_hotkey, button_hotkey),
                              bg=button_colour, bd=0, highlightthickness=0, padx=button_padding[X], pady=button_padding[Y]
                             ).pack(side=tk.LEFT, fill="both", expand=True,
                                    padx=button_spacing[X], pady=button_spacing[Y])
                except Exception as e:
                    print(f"Error loading image for {display_string}: {e}")
                    # If there's an error loading the icon, fallback to text
                    create_text_button(new_frame, display_string, button_hotkey)
            else:
                # If no icon is found or button text is not all caps, create a text button
                create_text_button(new_frame, display_string, button_hotkey)

def create_text_button(frame, display_string, button_hotkey):
    """Creates a text button if no image is available."""
    tk.Button(frame, text=display_string, command=partial(press_hotkey, button_hotkey),
              bg=button_colour, fg=text_colour, bd=0, highlightthickness=0, padx=button_padding[X], pady=button_padding[Y]
             ).pack(side=tk.LEFT, fill="both", expand=True,
                    padx=button_spacing[X], pady=button_spacing[Y])


def press_hotkey(keys):
    exec(str("hotkey(" + format_hotkey(alt_tab) + ")"))
    exec(str("hotkey(" + format_hotkey(keys) + ")"))

def format_hotkey(hotkeys):
    return "'" + hotkeys.replace(",", "','") + "'"

setup()
