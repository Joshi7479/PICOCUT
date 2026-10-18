import time
import board
import digitalio

print("Welcome to this short test, if you´re Buttons are Pull-Down or Pull-Up!")
print("Please connect a Button to GP1!")

button1 = digitalio.DigitalInOut(board.GP1)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

print("Dont touch the button! The text appearing on your display tells you, wich buttons you have!")
while True:
    if not button1.value == 1:
        print("Pull-DOWN-Button")
    else:
        print("Pull-UP-Button")
    time.sleep(3)