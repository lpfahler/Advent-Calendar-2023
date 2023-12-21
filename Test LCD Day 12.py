# Let it Glow Advent Calendar - Day 12
# Test LCD
# Lori Pfahler
# December 23, 2023

from utime import sleep
from machine import Pin, I2C
from neopixel import NeoPixel
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# Define the strand pin number (22) and number of LEDs (15)
strand = NeoPixel(Pin(22), 15)

# Set up LCD I2C
lcdi2c = I2C(1, sda= Pin(14), scl=Pin(15), freq=400000)
lcd = I2cLcd(i2c = lcdi2c, i2c_addr = 0x27, num_lines = 2, num_columns = 16)

# Show a string on the LCD
lcd.putstr("Hello, World!")

print("*********************************")
print("Display is now showing characters")
print("*********************************")


