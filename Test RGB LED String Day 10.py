# Let it Glow Advent Calendar - Day 10
# Test Addressable RGB LED Dot String - Flash Red and Green
# Lori Pfahler
# December 19, 2023

from utime import sleep
from machine import Pin, ADC
from neopixel import NeoPixel

# Define the strand pin number (22) and number of LEDs (15)
strand = NeoPixel(Pin(22), 15)

# Fill with red for 1 seconds
strand.fill((50,0,0))
strand.write()
sleep(1)

# Turn off
strand.fill((0,0,0))
strand.write()

# Make two lists of the even and odd LED numbers
LEDs1 = [0, 2, 4, 6, 8, 10, 12, 14]
LEDs2 = [1, 3, 5, 7, 9, 11, 13]

try: 
    while True:
        #  set even LEDs to red
        for i in LEDs1:
            strand[i] = (100, 0 , 0)
        # set odd LEDs to green
        for i in LEDs2:
            strand[i] = (0, 100 , 0)
            
        # Send the data to the ring
        strand.write()
        # sleep to see the color
        sleep(0.2)
        
        # set even LEDs to green
        for i in LEDs1:
            strand[i] = (0, 100 , 0)
        # set odd LEDs to red
        for i in LEDs2:
            strand[i] = (100, 0 , 0)

        # Send the data to the ring
        strand.write()
        # sleep to see the color
        sleep(0.2)

except KeyboardInterrupt:
    # turn off LEDs
    strand.fill((0, 0, 0))
    strand.write()
