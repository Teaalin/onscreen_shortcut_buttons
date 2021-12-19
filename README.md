# Onscreen Shortcut Buttons
A customisable onscreen shortcut toolbar for creative applications

![screen-gif](./example.gif)

## Why?
I switched to linux but I miss my windows onscreen toolbar, then I remembered, oh duh, I'm learning to program. I can MAKE one. 

cue python.

## Requirements:
- [python 3](https://www.python.org/downloads/)
- [tkinter](https://tkdocs.com/tutorial/install.html")

## Usage:
run `python3 Toolbar.py` in a [terminal](https://pythonbasics.org/execute-python-scripts/).

If you are on Mac OS change the code or config line `alt_tab = "alt,tab"` to `alt_tab = "command,shift,tab"`

Place and edit the toolbar_config.txt in the same folder as Toolbar.py (Or edit the Toolbar.py) to customise it.

Separate each desired row onto a line in the file and follow the following conventions:

### Configuration of buttons/hotkeys:
#### Example buttons:
```["BUTTON_TEXT : keyboard_key BUTTON_TEXT : keyboard_key,keyboard_key", "BUTTON_TEXT keyboard_key,keyboard_key,keyboard_key"```

Do not put spaces between keyboard keys, have atleast one space between 'keyboard_button' and the next BUTTON_TEXT

[See all possible keys](https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys)

## Caveats:
 - It relies on alt-tab to switch to the window that you want to use the shortcut on. I can't predict how it will behave if your alt-tab works differently. I plan to hunt alternative methods.
 - Impossible to move the window with only one column unless you configure the padding
 - Sometimes the buttons don't work or do something weird (likely because of alt-tab behaviour)
