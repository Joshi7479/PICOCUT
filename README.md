# PIOCCUT

Use your Raspberry Pi Pico as an Shortcut-Board / Makro-Board! / Nutze deinen Raspberry Pi Pico als Shortcut-Board / Makro-Board!
Use the interactive Setup in German and English to get everything ready with an GUI! Use the setup files in german and English to install it manually on a Raspberry Pi Pico.
For any other microcontrollers you can build your own fork based on this Project!
Want to try it first? https://wokwi.com/projects/478207020368504833 (That things get written to often is a bug of the simulation software!)
The GUI is the official supported way to install PICOCUT!

How does PICOCUT work?

PICOCUT itself has 2 1/2 key components:

1. The Setup Tool
2. The config File
3. The main python script (code.py) for the Raspberry Pi Pico

The basic Idea is, that the Pi tells the Computer: Hi, I am an USB-Keyboard.
If you then push a button (Buttons from Gp 1 - GP 22 are supported), the Pi tells the PC:
He wrote "{here he reads from the config file the string}"
The config File is just an txt, where the Strings for every buttons are written.
The Setup-Software does two things:
    a) Giving you the instructions for installing PICOCUT onto you`re Pi.
    b) Writes the config file for you (With the simple System: line in the document = GP + 6)

And now: Install it!

PICOCUT made by Joshi7479
