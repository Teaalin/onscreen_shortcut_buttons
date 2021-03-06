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

### Configuration of buttons/hotkeys:
Place and edit the toolbar_config.txt in the same folder as Toolbar.py (Or edit the Toolbar.py) to customise it.

If you are on Mac OS change the code or config line `alt_tab = "alt,tab"` to `alt_tab = "command,shift,tab"`

#### Button format in config:
```"buttons":["BUTTON_TEXT : keyboard_key BUTTON_TEXT : keyboard_key,keyboard_key", "BUTTON_TEXT keyboard_key,keyboard_key,keyboard_key"]```

Encapsulate each button row in double quotes `"`, and sepparate each row with a comma `,`

Do not put spaces between keyboard keys, have atleast one space between 'keyboard_key' and the next BUTTON_TEXT

See my toolbar_config for complete formatting including other custom settings

[See all possible keys](https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys)

## Caveats:
 - It relies on alt-tab to switch to the window that you want to use the shortcut on. I can't predict how it will behave if your alt-tab works differently. I plan to hunt alternative methods.
 - Impossible to move the window with only one column unless you configure the padding
 - Sometimes the buttons don't work or do something weird (likely because of alt-tab behaviour)
 - It's python, it's slow, but for this application it works enough
