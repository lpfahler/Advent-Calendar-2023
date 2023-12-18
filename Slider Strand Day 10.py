# Let it Glow Advent Calendar - Day 10
# Pulse the colors
# Lori Pfahler
# December 19, 2023

from utime import sleep
from machine import Pin, ADC
from neopixel import NeoPixel

# Define the strand pin number (22) and number of LEDs (15)
strand = NeoPixel(Pin(22), 15)

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

try: 
    while True:
        # Read the potentiometer value
        potValue = potentiometer.read_u16()
        # scale the potValue to the desired range of delay times
        currentLED = round((14 /65535) * potValue)
        # print for debugging and observing potValue and delayTime
        print(f'{potValue}, {currentLED}', end = '\r')
        # clear the all LEDs and then light the current one
        strand.fill((0, 0, 0))        
        strand[currentLED] = (0, 100 , 0)
        strand.write()
        sleep(0.1)
        
except KeyboardInterrupt:
    # turn off LEDs
    strand.fill((0, 0, 0))
    strand.write()


