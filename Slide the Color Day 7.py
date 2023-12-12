# Let it Glow Advent Calendar - Day 7
# Activity 2 - Slide the Color
# 
# Lori Pfahler
# December 13, 2023

from utime import sleep
from machine import Pin, ADC
from neopixel import NeoPixel

# Define GRBled1 pin number (22) and number of LEDs (1)
GRBled1 = NeoPixel(Pin(22), 1)
# Define GRBled2 pin number (21) and number of LEDs (1)
GRBled2 = NeoPixel(Pin(21), 1)

# Define a few basic GRB color variables
red = 0,255,0
amber = 255,175,150
green = 255,0,0

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

try:
    while True:
        # Read the potentiometer
        potValue = potentiometer.read_u16()  
        print(f'{potValue:5d}', end = '\r')
        sleep(0.1)
        # If potValue is less than or equal to 20000 - set LEDs to red
        if potValue <= 20000:          
            GRBled1.fill((red))
            GRBled1.write()
            GRBled2.fill((red))
            GRBled2.write()
        # If potValue is between 20000 and 40000 - set LEDs to amber
        elif 20000 < potValue < 40000: 
            GRBled1.fill((amber))
            GRBled1.write()
            GRBled2.fill((amber))
            GRBled2.write()
        # If potValue is greater than or equal to 40000   - set LEDs to green
        elif potValue >= 40000: 
            GRBled1.fill((green))
            GRBled1.write()
            GRBled2.fill((green))
            GRBled2.write()

except KeyboardInterrupt:
    # turn LEDs off
    GRBled1.fill((0,0,0))
    GRBled1.write()
    GRBled2.fill((0,0,0))       
    GRBled2.write()    
