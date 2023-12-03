# Let it Glow Advent Calendar - Day 2
# Blink the Block and Internal LED together - Activity 2 & 3 Sort of!
# Lori Pfahler
# December 3, 2023

from machine import Pin
from utime import sleep

# setup block LED - red
blockLED = Pin(17, Pin.OUT)

# setup internal LED - green
internalLED = Pin(25, Pin.OUT)

# blink LEDs together
while True:
    blockLED.toggle()
    internalLED.toggle()
    sleep(0.5)
