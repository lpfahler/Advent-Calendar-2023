# Let it Glow Advent Calendar - Day 10
# Pulse the colors
# Lori Pfahler
# December 19, 2023

from utime import sleep
from machine import Pin, ADC
from neopixel import NeoPixel

# Define the strand pin number (22) and number of LEDs (15)
strand = NeoPixel(Pin(22), 15)

# Make two lists of the even and odd LED numbers
# This could be done by using modulo math - but I don't think it really saves much code
# use LED# % 2 == 0 (even) LED# % 2 != 0 (odd)
# modulo approach would be useful is string were very long
LEDs1 = [0, 2, 4, 6, 8, 10, 12, 14]
LEDs2 = [1, 3, 5, 7, 9, 11, 13]

try: 
    while True:
        # fade in
        for intensity in range(0, 250, 1):
            #  set even LEDs to red
            for i in LEDs1:
                strand[i] = (intensity, 0 , 0)
            # set odd LEDs to green
            for i in LEDs2:
                strand[i] = (0, intensity , 0)
                
            # Send the data to the ring
            strand.write()
            # sleep to see the color
            sleep(0.005)
        
        # fade out
        for intensity in range(255, 0, -1):
            #  set even LEDs to red
            for i in LEDs1:
                strand[i] = (intensity, 0 , 0)
            # set odd LEDs to green
            for i in LEDs2:
                strand[i] = (0, intensity , 0)
                
            # Send the data to the ring
            strand.write()
            # sleep to see the color
            sleep(0.005)

except KeyboardInterrupt:
    # turn off LEDs
    strand.fill((0, 0, 0))
    strand.write()

