# Let it Glow Advent Calendar - Day 6
# Test Addressable GRB LEDs
# Activity 1 - Testing both LEDs
# Added try and except to end program and turn off the LEDs
# Lori Pfahler
# December 11, 2023

# Imports
from utime import sleep
from machine import Pin
from neopixel import NeoPixel

# Define GRBled1 pin number (22) and number of LEDs (1)
GRBled1 = NeoPixel(Pin(22), 1)
# Define GRBled2 pin number (21) and number of LEDs (1)
GRBled2 = NeoPixel(Pin(21), 1)

try:
    # Fill the led1 with blue (GRB)
    GRBled1.fill((0,0,255))
    # Write the data to the LED
    GRBled1.write()

    # Fill the led2 with green (GRB)
    GRBled2.fill((255,0,0))       
    # Write the data to the LED
    GRBled2.write()
    
    # wait till <ctrl> <c> is pressed to turn off LEDs
    while True:
        pass
    
except KeyboardInterrupt:
    # turn them off
    GRBled1.fill((0,0,0))
    GRBled1.write()
    GRBled2.fill((0,0,0))       
    GRBled2.write()
