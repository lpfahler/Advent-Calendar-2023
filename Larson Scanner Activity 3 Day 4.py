# Let it Glow Advent Calendar - Day 4
# Larson Scanner - Activity 3
# As seen Knight Rider and BattleStar Galactica
# Lori Pfahler
# December 7, 2023

from machine import Pin
from utime import sleep

# Set up LED pins
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# make a list of the LED objects
seg_list = [seg1, seg2, seg3, seg4, seg5]

# use try and except to end program with <ctrl><c>
try: 
    while True:
        # Forwards through the list
        for LED in seg_list:        
            LED.on()
            sleep(0.05)
            LED.off()       
        # Backwards through the list
        for LED in reversed(seg_list):        
            LED.on()
            sleep(0.05)
            LED.off()
except KeyboardInterrupt:
    # Turn all LEDs off
    for LED in seg_list:
        LED.value(0)
