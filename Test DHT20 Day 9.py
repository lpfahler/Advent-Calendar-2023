# Let it Glow Advent Calendar - Day 9
# Test DHT20 Pressure and Humidity Sensor
# Lori Pfahler
# December 17, 2023


from machine import Pin, I2C
from utime import sleep
from dht20 import DHT20


# Set up I2C
i2c1 = I2C(0, sda = Pin(16), scl = Pin(17))

# Set up DHT20 device with I2C address
dht20 = DHT20(0x38, i2c1)

# Some extra sleep to allow sensor to intitialize
# probably not needed?
sleep(2)

# print title line
print('Enviroment Data:')

while True:
    # Grab data from the sensor dictionary
    measurements = dht20.measurements
    # use some variables to make it easier to read code
    temp_C = measurements['t']
    temp_F = (temp_C * 1.8) + 32
    humid = measurements['rh']
    
    if measurements['crc_ok']:        
        # Print the data all on one line with replacement
        print(f"Temperature: {temp_F:3.1f}°F, {temp_C:3.1f}°C | Humidity: {humid:3.1f}%", end = '\r')        
    
    # Wait 1 seconds
    sleep(1)
