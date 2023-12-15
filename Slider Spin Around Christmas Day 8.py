# Let it Glow Advent Calendar - Day 8
# Slider Control of Spin Around Christmas Colors
# 
# Lori Pfahler
# December 15, 2023

from machine import Pin, ADC
from neopixel import NeoPixel
from utime import sleep

# Define the ring pin number 22 and number of LEDs = 12
ring = NeoPixel(Pin(22), 12)

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

# delay times
fastDelay = 0.03
slowDelay = 0.2
# slope for equation to link delayTime to potValue
slope = (slowDelay - fastDelay)/65535

try:
    while True:
        # Read the potentiometer value
        potValue = potentiometer.read_u16()
        # scale the potValue to the desired range of delay times
        delayTime = (slope * potValue) + fastDelay
        # print for debugging and observing potValue and delayTime
        print(f'{potValue}, {delayTime}', end = '\r')
        
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
            sleep(delayTime)
        
except KeyboardInterrupt:
    # turn off LEDs
    ring.fill((0, 0, 0))
    ring.write()


