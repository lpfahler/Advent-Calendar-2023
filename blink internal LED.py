# Let it Glow Advent Calendar
# Toggle the internal LED on and off
# Lori Pfahler
# December 1, 2023

from machine import Pin
from utime import sleep

# setup onboard LED
onboardLED = Pin(25, Pin.OUT)

# blink away
while True:
    onboardLED.toggle()
    sleep(0.5)
    