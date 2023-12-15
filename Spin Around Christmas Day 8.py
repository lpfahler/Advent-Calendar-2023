# Let it Glow Advent Calendar - Day 8
# Spin Around Christmas Colors
# 
# Lori Pfahler
# December 15, 2023

from machine import Pin
from neopixel import NeoPixel
from utime import sleep

# Define the ring pin number 22 and number of LEDs = 12
ring = NeoPixel(Pin(22), 12)

try:
    while True:

        for i in range(0, 12):
            # clear out last loop's LEDs
            ring.fill((0, 0, 0))
            # set to red
            ring[i] = (100, 0 , 0)
            # set to green
            if i < 6:
                ring[i + 6] = (0, 100, 0)
            else:
                ring[i - 6] = (0, 100, 0)
            # Send the data to the ring
            ring.write()
            # sleep 
            sleep(0.2)
        
except KeyboardInterrupt:
    # turn off LEDs
    ring.fill((0, 0, 0))
    ring.write()

