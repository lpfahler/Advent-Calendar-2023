# Let it Glow Advent Calendar - Day 2
# Blink the Block LED - Activities 1-4 Sort of!
# Lori Pfahler
# December 3, 2023

from machine import Pin
from utime import sleep

# setup block LED
blockLED = Pin(17, Pin.OUT)

# blink away
while True:
    blockLED.toggle()
    sleep(0.5)