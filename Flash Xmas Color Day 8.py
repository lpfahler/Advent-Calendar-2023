# Let it Glow Advent Calendar - Day 8
# Flash Some Christmas Color
# 
# Lori Pfahler
# December 15, 2023

from machine import Pin
from neopixel import NeoPixel
from utime import sleep

# Define the ring pin number 22 and number of LEDs = 12
ring = NeoPixel(Pin(22), 12)

# Make two lists of the even and odd LED numbers
LEDs1 = [0, 2, 4, 6, 8, 10]
LEDs2 = [1, 3, 5, 7, 9, 11]

try:
    while True:
        #  set even LEDs to red
        for i in LEDs1:
            ring[i] = (10, 0 , 0)
        # set odd LEDs to green
        for i in LEDs2:
            ring[i] = (0, 10 , 0)
            
        # Send the data to the ring
        ring.write()
        # sleep to see the color
        sleep(0.2)
        
        # set even LEDs to green
        for i in LEDs1:
            ring[i] = (0, 10 , 0)
        # set odd LEDs to red
        for i in LEDs2:
            ring[i] = (10, 0 , 0)
            
        # Send the data to the ring
        ring.write()
        # sleep to see the color
        sleep(0.2)
        
except KeyboardInterrupt:
    # turn off LEDs
    ring.fill((0, 0, 0))
    ring.write()
