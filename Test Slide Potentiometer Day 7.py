









# Let it Glow Advent Calendar - Day 7
# Activity 1 - Read the Slide Pententiometer
# Lori Pfahler
# December 13, 2023

from utime import sleep
from machine import Pin, ADC

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

while True: 
    # Read the potentiometer value
    potValue = potentiometer.read_u16()
    # Use fstring to print to shell
    # Use '\r' to replace rather than fill the shell with lines
    print(f'{potValue:5d}', end = '\r') 
    # delay 
    sleep(0.3) 

