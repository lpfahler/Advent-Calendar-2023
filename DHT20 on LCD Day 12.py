# Let it Glow Advent Calendar - Day 12
# Display Temp and Humidity on LCD with
# LED Strand Color indicating temp
# Lori Pfahler
# December 23, 2023

from utime import sleep
from machine import Pin, I2C
from neopixel import NeoPixel
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from dht20 import DHT20

# Define the strand pin number (22) and number of LEDs (15)
strand = NeoPixel(Pin(22), 15)

tempColors ={
    'Red'   : (255,   0,   0), # Hot
    'Green' : (  0, 255,   0), # Perfect temps
    'Blue'  : (  0,   0, 255), # Cold
    'White' : (255, 255, 255), # Below Freezing
}

# Set up LCD I2C for LCD
lcdi2c = I2C(1, sda= Pin(14), scl=Pin(15), freq=400000)
lcd = I2cLcd(i2c = lcdi2c, i2c_addr = 0x27, num_lines = 2, num_columns = 16)

# Set up I2C for DHT20
i2c1 = I2C(0, sda = Pin(16), scl = Pin(17))

# Set up DHT20 device with I2C address
dht20 = DHT20(0x38, i2c1)

# Write static text
lcd.putstr("Temp:")

lcd.move_to(0, 1) # Move to second row
lcd.putstr("Humidity:")


while True:
    
    # Grab data from the sensor dictionary
    measurements = dht20.measurements
    
    # use some variables to make it easier to read code
    temp_C = measurements['t']
    temp_F = (temp_C * 1.8) + 32
    humid = measurements['rh']

    if temp_F > 80:
        strand.fill(tempColors['Red'])        
        strand.write()
    elif temp_F > 70:
        strand.fill(tempColors['Green'])        
        strand.write()
    elif temp_F > 32:
        strand.fill(tempColors['Blue'])        
        strand.write()
    else:
        strand.fill(tempColors['White'])        
        strand.write()

    # Show temp data on the first row
    lcd.move_to(10, 0) # 10th column, 1st row
    lcd.putstr(str(round(temp_F, 1)) + 'F')
    
    # Show humidity data on the second row
    lcd.move_to(10, 1) # 10th column, 2nd row
    lcd.putstr(str(round(humid, 1)) + '%')
    
    sleep(5)
