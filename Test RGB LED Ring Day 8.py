# Let it Glow Advent Calendar - Day 8
# Setup the RGB LED Ring and Make Some Christmas Color
# Activities 1-4 Sort of!
# Lori Pfahler
# December 15, 2023

from machine import Pin
from neopixel import NeoPixel
from utime import sleep

# Define the ring pin number 22 and number of LEDs = 12
ring = NeoPixel(Pin(22), 12)

try:
    while True:
        # Fill the LEDs with Christmas colors - first red
        ring.fill((10, 0, 0))
        # Send the data to the ring
        ring.write()
        # sleep to see the color
        sleep(0.25)

        # Fill the LEDs with Christmas colors - next green 
        ring.fill((0, 10 ,0))
        # Send the data to the ring
        ring.write()
        sleep(0.25)

except KeyboardInterrupt:
    # turn off LEDs
    ring.fill((0, 0, 0))
    ring.write()