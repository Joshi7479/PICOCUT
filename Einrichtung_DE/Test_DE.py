import time
import board
import digitalio

print("Herzlich willkommen, zu diesem Kurzen Test, ob du Pull-Down oder Pull-Up-Knöpfe hast!")
print("Bitte stecke einen Knopf an den GP 1!")

button1 = digitalio.DigitalInOut(board.GP1)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

print("Beobachte jetzt, was passiert. Drücke den Knopf NICHT! Wenn DOWN steht, hast du Pull-Down-Buttons und bei UP Pull-UP-Buttons.")
while True:
    if not button1.value == 1:
        print("DOWN")
    else:
        print("UP")
    time.sleep(3)
