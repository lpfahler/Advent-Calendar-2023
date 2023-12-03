# Let it Glow Advent Calendar - Day 2
# Blink the Block and Internal LED Alternating
# Activity 2 & 3 Sort of!
# Lori Pfahler
# December 3, 2023

from machine import Pin
from utime import sleep

# setup block LED - red
blockLED = Pin(17, Pin.OUT)

# setup internal LED - green
internalLED = Pin(25, Pin.OUT)

# blink LEDs alternating
while True:
    blockLED.on()
    sleep(0.5)
    blockLED.off()
    internalLED.on()
    sleep(0.5)
    internalLED.off()

