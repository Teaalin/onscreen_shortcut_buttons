# onscreen shortcut buttons
A customisable onscreen shortcut toolbar for creative applications

![screen-gif](./example.gif)

## Why?
I switched to linux about a month ago in celebration of Windows 11. I was hesitant to switch, but only my art setup held me back.
I missed my windows only onscreen toolbar today, then I remembered, oh duh, I'm learning to program. I can MAKE one.
cue python.

## How to use:
It can run with or without the config file, but you need the config to customise the setup.
it doesn't work well with only one column so try to have atleast 2 like the example config (see known issues below)

## Configuration of buttons/hotkeys:
#### 1 keyboard key:
`BUTTON_TEXT "keyboard_button"`
#### 2 keyboard keys:
`BUTTON_TEXT "keyboard_button1","keyboard_button2"`
#### 2+ keyboard keys:
`BUTTON_TEXT "keyboard_button1","keyboard_button2","keyboard_button3",... and to infinity`

See https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys for all possible keys

#### Configuration example of 3 columns:
`BUTTON_TEXT "keyboard_button"    BUTTON_TEXT "keyboard_button"    BUTTON_TEXT "keyboard_button"`

Do NOT add extra spaces in the config. Do NOT use a tab instead of 4 spaces between the buttons or reduce these spaces.
The code relies on finding the spaces to seppartate the buttons (to be changed)

#### known issues:
 - terrible, if not impossible to move the window with only one column
 - terrible code :P
 - terrible config
 - I am a github noob (first public project)
