import time
import board
from rainbowio import colorwheel
import neopixel

# Set up NeoPixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

# first kind of rainbow spin
def rainbow_cycle(wait):
    # set to loop for 255 iterations
    for j in range(255):
        # set to loop for every LED
        for i in range(len(pixels)):
            rc_index = (i * 256 // len(pixels)) + j * 5
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

# second kind of rainbow spin
def rainbow(wait):
    for j in range(255):
        for i in range(len(pixels)):
            idx = i + j
            pixels[i] = colorwheel(idx & 255)
        pixels.show()
        time.sleep(wait)

while True:
    rainbow_cycle(0.01)  # speed controller
    rainbow(0.01)
