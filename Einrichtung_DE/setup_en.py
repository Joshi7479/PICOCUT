#!/usr/bin/python3
import time
import sys
import os
setup = True
print("= = =   =    = =     = =   = =   =     =  = = = =")
print("=    =  =  =       =     =       =     =     =   ")
print("= = =   =  =       =     =       =     =     =   ")
print("=       =    = =     = =   = =     = =       =   ")
print("Herzlich willkommen beim PICOCUT-Setup-Tool.")
print("!Aktuell werden von diesem Projekt NUR PULL-UP Knöpfe unterstüzt!")
print("ACHTUNG! Im Gegensatz zum Setup-Tool in der Java Variante, muss für dieses eine config File im selben Ordner liegen!")
h = Input("Meine config.txt liegt im selben Ordner.")

while setup:
    with open ("config.txt", "r",encoding="utf-8") as f:
        zeilen = f.readlines()
    
    a = int(input("An welchem GP hängt dein Knopf? (Dieses Projekt wurde für den RaspberryPi Pico erstellt.\nFür andere Microcontroller kannst du die Software gerne umschreiben!\nVon dieser Software werden nur die Pins von 1 - 22 angesteuert.\nDie Pinnbelegung aller Pico Modelle ist gleich:\nhttps://www.elektronik-kompendium.de/sites/raspberry-pi/2611051.htm)\nGP Nr."))
    if a < 1:
        print("Es werden nur die Pins 1-22 unterstüzt!")
        time.sleep(0.5)
        sys.exit()
    if a > 22:
        print("Es werden nur die Pins 1-22 unterstüzt!")
        time.sleep(0.5)
        sys.exit()
    a = int(a+5)
    b = input("und was soll der Knopf tuen? ")
    
    zeilen[a] = b
    with open ("config.txt", "w", encoding="utf-8") as f:
        f.writelines(zeilen)
    c = int(input("Noch einen Button konfigurieren?\n(0 = Nein; 1 = Ja) "))
    if c == 1:
        print("Okay")
        time.sleep(2)
    else:
        print("Auf Wiedersehen")
        print("= = =   =    = =     = =   = =   =     =  = = = =")
        print("=    =  =  =       =     =       =     =     =   ")
        print("= = =   =  =       =     =       =     =     =   ")
        print("=       =    = =     = =   = =     = =       =   ")
        print("Geschrieben in Python von Joshi7479")
        print("Besuche dieses Projekt auch auf Github: github.com/Joshi7479/PICOCUT")
        print("Fragen? Schicke sie mir gerne an Joshi7479@proton.me")
        print("Erstelle auch gerne deine eigene Version basierend auf diesem Projekt!")
        time.sleep(0.5)
        setup = False
        
        
    
