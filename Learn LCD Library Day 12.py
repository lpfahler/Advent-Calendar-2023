# Let it Glow Advent Calendar - Day 12
# Learn the LCD Library - The Everything Script
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


# Our variables
mystring = "String variable" # String
myinteger = 44         # Integer
myfloat = 9.445589     # Float

# Just a function to sleep and then clear the LCD
# Saves lines after each example!
def clearLCD():
    sleep(3)
    lcd.clear()

##### Example Program Start #####

# This is how you show basic text
lcd.putstr("I am a string")
sleep(3)

# This is how you clear the display
# Do this before you send new data to be displayed
lcd.clear()

# This is how you move the cursor
# We moved it to the second row
# 1st number is column (X), 2nd number is row (Y)
# Numbers start at zero
# (0,0) is the 1st column, 1st row
lcd.move_to(0, 1)
lcd.putstr("Second row!")
clearLCD()

# This is how you show a variable
# Variables can be strings, integers or floats
# 'str' converts them to a string
# Here are three examples:
lcd.putstr(str(mystring)) # String
clearLCD()

lcd.putstr(str(myinteger)) # Integer
clearLCD()

lcd.putstr(str(myfloat)) # Float
clearLCD()

# This turns the backlight off
lcd.backlight_off()
clearLCD()

# This turns the backlight on
lcd.backlight_on()
clearLCD()

# This turns the standard cursor on
lcd.show_cursor()
clearLCD()

# This turns the standard cursor off
lcd.hide_cursor()
clearLCD()

# This turns the blinking cursor on
lcd.blink_cursor_on()
clearLCD()

# This turns the blinking cursor on
lcd.blink_cursor_off()
clearLCD()
