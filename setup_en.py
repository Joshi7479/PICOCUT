#!/usr/bin/python3
import time
import sys
setup = True
print("= = =   =    = =     = =   = =   =     =  = = = =")
print("=    =  =  =       =     =       =     =     =   ")
print("= = =   =  =       =     =       =     =     =   ")
print("=       =    = =     = =   = =     = =       =   ")
print("Welcome to the PICOCUT-Setup-Tool. Only GP Pins 1-22 are supported!")
print("There will be Support for Pull-Down Buttons in the Future, but its not ready yet!")
print("WARNING: For the this Version of the Setup-Tool, there has to be an config.txt in the same Folder!")
h = Input("My config file is in the right folder!")



while setup:
    with open ("config.txt", "r",encoding="utf-8") as config:
        zeilen = config.readlines()

    
    a = int(input("At which Port is your Button? (This Project was developed for Raspberry pi Pico.\nFor other microcontrollers you can easily adapt this software!\nOnly Pins 1-22 are supported.\nThe Pinouts are the same for all Pico Models:\nhttps://www.elektronik-kompendium.de/sites/raspberry-pi/2611051.htm)\nGP Nr."))
    if a < 1:
        print("Only Pins 1-22 are supported!")
        time.sleep(0.5)
        sys.exit()
    if a > 22:
        print("Only Pins 1-22 are supported!")
        time.sleep(0.5)
        sys.exit()
    a = int(a+5)
    b = input("and what should the button do? ")
    
    zeilen[a] = b
    with open ("config.txt", "w", encoding="utf-8") as config:
        config.writelines(zeilen)
    c = int(input("Configure another button?\n(0 = No; 1 = Yes) "))
    if c == 1:
        print("Okay")
        time.sleep(2)
    else:
        print("Bye!")
        print("= = =   =    = =     = =   = =   =     =  = = = =")
        print("=    =  =  =       =     =       =     =     =   ")
        print("= = =   =  =       =     =       =     =     =   ")
        print("=       =    = =     = =   = =     = =       =   ")
        print("Made by Joshi7479 in Python")
        print("Visit this Project on Github: github.com/Joshi7479/PICOCUT")
        print("Questions? Send them to Joshi7479@proton.me")
        print("Feel free to make you´r own Fork! Everything is opensource!")
        time.sleep(0.5)
        setup = False

time.sleep(0.5)
