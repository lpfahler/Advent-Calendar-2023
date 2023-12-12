# Let it Glow Advent Calendar - Day 7
# Activity 4 - Control the Flash Rate with Potentiometer
# 
# Lori Pfahler
# December 13, 2023

from utime import sleep
from machine import Pin, ADC
from neopixel import NeoPixel
from random import randint

# Define GRBled1 pin number (22) and number of LEDs (1)
GRBled1 = NeoPixel(Pin(22), 1)
# Define GRBled2 pin number (21) and number of LEDs (1)
GRBled2 = NeoPixel(Pin(21), 1)

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

try:
    while True:      
        # Read the potentiometer value
        flash = potentiometer.read_u16() / 65000
        
        # Generate random GRB values for LED 1
        g1 = randint(0,255)
        r1 = randint(0,255)
        b1 = randint(0,255)

        # Generate random GRB values for LED 2
        g2 = randint(0,255)
        r2 = randint(0,255)
        b2 = randint(0,255)
        
        # Light the LED with the random GRB values
        GRBled1.fill((g1, r1, b1))
        GRBled1.write()
        GRBled2.fill((g2, r2, b2))
        GRBled2.write()
        
        # Delay based on slider position
        sleep(flash)


except KeyboardInterrupt:
    # turn LEDs off
    GRBled1.fill((0,0,0))
    GRBled1.write()
    GRBled2.fill((0,0,0))       
    GRBled2.write()  