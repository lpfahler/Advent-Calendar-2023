# Let it Glow Advent Calendar - Day 6
# Light Passing Activity 5
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
    while True:
        
        # First LED fades in
        for i in range(255):        
            GRBled1.fill((i,0,0))
            GRBled1.write()        
            sleep(0.005)
        
        #Turn off the first LED
        GRBled1.fill((0,0,0))
        GRBled1.write()
        
        # Second LED fades out (using reversed)
        for i in reversed (range(255)):       
            GRBled2.fill((i,0,0))
            GRBled2.write()       
            sleep(0.005)

except KeyboardInterrupt:
    # turn them off
    GRBled1.fill((0,0,0))
    GRBled1.write()
    GRBled2.fill((0,0,0))       
    GRBled2.write() 