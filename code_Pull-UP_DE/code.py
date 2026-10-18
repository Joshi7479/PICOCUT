import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

button1 = digitalio.DigitalInOut(board.GP1)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.GP2)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

button3 = digitalio.DigitalInOut(board.GP3)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP

button4 = digitalio.DigitalInOut(board.GP4)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.UP

button5 = digitalio.DigitalInOut(board.GP5)
button5.direction = digitalio.Direction.INPUT
button5.pull = digitalio.Pull.UP

button6 = digitalio.DigitalInOut(board.GP6)
button6.direction = digitalio.Direction.INPUT
button6.pull = digitalio.Pull.UP

button7 = digitalio.DigitalInOut(board.GP7)
button7.direction = digitalio.Direction.INPUT
button7.pull = digitalio.Pull.UP

button8 = digitalio.DigitalInOut(board.GP8)
button8.direction = digitalio.Direction.INPUT
button8.pull = digitalio.Pull.UP

button9 = digitalio.DigitalInOut(board.GP9)
button9.direction = digitalio.Direction.INPUT
button9.pull = digitalio.Pull.UP

button10 = digitalio.DigitalInOut(board.GP10)
button10.direction = digitalio.Direction.INPUT
button10.pull = digitalio.Pull.UP

button11 = digitalio.DigitalInOut(board.GP11)
button11.direction = digitalio.Direction.INPUT
button11.pull = digitalio.Pull.UP

button12 = digitalio.DigitalInOut(board.GP12)
button12.direction = digitalio.Direction.INPUT
button12.pull = digitalio.Pull.UP

button13 = digitalio.DigitalInOut(board.GP13)
button13.direction = digitalio.Direction.INPUT
button13.pull = digitalio.Pull.UP

button14 = digitalio.DigitalInOut(board.GP14)
button14.direction = digitalio.Direction.INPUT
button14.pull = digitalio.Pull.UP

button15 = digitalio.DigitalInOut(board.GP15)
button15.direction = digitalio.Direction.INPUT
button15.pull = digitalio.Pull.UP

button16 = digitalio.DigitalInOut(board.GP16)
button16.direction = digitalio.Direction.INPUT
button16.pull = digitalio.Pull.UP

button17 = digitalio.DigitalInOut(board.GP17)
button17.direction = digitalio.Direction.INPUT
button17.pull = digitalio.Pull.UP

button18 = digitalio.DigitalInOut(board.GP18)
button18.direction = digitalio.Direction.INPUT
button18.pull = digitalio.Pull.UP

button19 = digitalio.DigitalInOut(board.GP19)
button19.direction = digitalio.Direction.INPUT
button19.pull = digitalio.Pull.UP

button20 = digitalio.DigitalInOut(board.GP20)
button20.direction = digitalio.Direction.INPUT
button20.pull = digitalio.Pull.UP

button21 = digitalio.DigitalInOut(board.GP21)
button21.direction = digitalio.Direction.INPUT
button21.pull = digitalio.Pull.UP

button22 = digitalio.DigitalInOut(board.GP22)
button22.direction = digitalio.Direction.INPUT
button22.pull = digitalio.Pull.UP

with open("config.txt", "r", encoding="utf-8") as datei:
    zeilen = datei.readlines()
    anzahl_zeilen = sum(1 for zeile in datei)
    
    b1 = zeilen[5].strip()
    b2 = zeilen[6].strip()
    b3 = zeilen[7].strip()
    b4 = zeilen[8].strip()
    b5 = zeilen[9].strip()
    b6 = zeilen[10].strip()
    b7 = zeilen[11].strip()
    b8 = zeilen[12].strip()
    b9 = zeilen[13].strip()
    b10 = zeilen[14].strip()
    b11 = zeilen[15].strip()
    b12 = zeilen[16].strip()
    b13 = zeilen[17].strip()
    b14 = zeilen[18].strip()
    b15 = zeilen[19].strip()
    b16 = zeilen[20].strip()
    b17 = zeilen[21].strip()
    b18 = zeilen[22].strip()
    b19 = zeilen[23].strip()
    b20 = zeilen[24].strip()
    b21 = zeilen[25].strip()
    b22 = zeilen[26].strip()
    b23 = zeilen[27].strip()

while True:
    if not button1.value:
        layout.write(b2)
        time.sleep(0.3)
           
    if not button2.value:
        layout.write(b3)
        time.sleep(0.3)

    if not button3.value:
        layout.write(b4)
        time.sleep(0.3)

    if not button4.value:
        layout.write(b5)
        time.sleep(0.3)

    if not button5.value:
        layout.write(b6)
        time.sleep(0.3)

    if not button6.value:
        layout.write(b7)
        time.sleep(0.3)

    if not button7.value:
        layout.write(b8)
        time.sleep(0.3)

    if not button8.value:
        layout.write(b9)
        time.sleep(0.3)

    if not button9.value:
        layout.write(b10)
        time.sleep(0.3)

    if not button10.value:
        layout.write(b11)
        time.sleep(0.3)

    if not button11.value:
        layout.write(b12)
        time.sleep(0.3)

    if not button12.value:
        layout.write(b13)
        time.sleep(0.3)

    if not button13.value:
        layout.write(b14)
        time.sleep(0.3)

    if not button14.value:
        layout.write(b15)
        time.sleep(0.3)

    if not button15.value:
        layout.write(b16)
        time.sleep(0.3)

    if not button16.value:
        layout.write(b17)
        time.sleep(0.3)

    if not button17.value:
        layout.write(b18)
        time.sleep(0.3)

    if not button18.value:
        layout.write(b19)
        time.sleep(0.3)

    if not button19.value:
        layout.write(b20)
        time.sleep(0.3)

    if not button20.value:
        layout.write(b21)
        time.sleep(0.3)

    if not button21.value:
        layout.write(b22)
        time.sleep(0.3)

    if not button22.value:
        layout.write(b23)
        time.sleep(0.3)

    time.sleep(0.01)
