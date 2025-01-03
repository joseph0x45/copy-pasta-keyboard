import board
import time
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

switchCopy = DigitalInOut(board.GP0)
switchCopy.direction = Direction.INPUT
switchCopy.pull = Pull.DOWN
switchPaste = DigitalInOut(board.GP1)
switchPaste.direction = Direction.INPUT
switchPaste.pull = Pull.DOWN

while True:
    if switchCopy.value:
        keyboard.send(Keycode.CONTROL, Keycode.C)
    elif switchPaste.value:
        keyboard.send(Keycode.CONTROL, Keycode.V)
    time.sleep(0.5)
