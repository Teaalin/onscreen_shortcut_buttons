# onscreen shortcut buttons
A customisable onscreen shortcut toolbar for creative applications

![screen-gif](./example.gif)

## Why?
I switched to linux about a month ago in celebration of Windows 11. I was hesitant to switch, but only my art setup held me back.
I missed my windows only onscreen toolbar today, then I remembered, oh duh, I'm learning to program. I can MAKE one.
cue python.

## Requirements:
- python 3
- maybe tk (google "install tkinter on Windows/Linux/Mac")

## How to use:
It can run with or without the config file, but you need the config to customise the setup.
it doesn't work well with only one column so try to have atleast 2 like the example config (see known issues below)
Separate each row onto a line in the text file and follow the following conventions:

### Configuration of buttons/hotkeys:
#### 1 keyboard key:
`BUTTON_TEXT "keyboard_button"`
#### 2 keyboard keys:
`BUTTON_TEXT "keyboard_button1","keyboard_button2"`
#### 3+ keyboard keys:
`BUTTON_TEXT "keyboard_button1","keyboard_button2","keyboard_button3",... and to infinity`

See https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys for all possible keys

#### Configuration example of 3 columns:
`BUTTON_TEXT "keyboard_button"    BUTTON_TEXT "keyboard_button"    BUTTON_TEXT "keyboard_button"`

Do NOT add extra spaces in the config. Do NOT use a tab instead of 4 spaces between the buttons or reduce these spaces.
The code relies on finding the spaces to seppartate the buttons (to be changed)

### known issues:
 - terrible, if not impossible to move the window with only one column
 - I have no idea what will happen if you have 3 columns in one row, then 2 in the next.
   so if you use 3 columns+, have a row with 3+ or a row with 1, nothing inbetween
 - terrible code :P
 - terrible config
 - I am a github noob (first public project)

##### Small caveat:
it relies on alt-tab to switch back to the window that you want to use the shortcut on. I can't predict the behaviour it will have if you have alt-tab assigned to something else. I plan to see if there's alternative methods, but I'm avoiding OS specific code so that this program should be compatible with Windows, Mac and the many unix based systems so long as you have
