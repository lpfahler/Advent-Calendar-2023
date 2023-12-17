# Let it Glow Advent Calendar - Day 9
# Ring and Temperature Sensor Weather Station
# Lori Pfahler
# December 17, 2023

from machine import Pin, I2C
from utime import sleep
from dht20 import DHT20
from neopixel import NeoPixel

# Set up I2C
i2c1 = I2C(0, sda = Pin(16), scl = Pin(17))

# Set up DHT20 device with I2C address
dht20 = DHT20(0x38, i2c1)
# Some extra sleep to allow sensor to intitialize - probably not needed
sleep(1)

# Define the ring on pin number 22 and number of LEDs = 12
ring = NeoPixel(Pin(22), 12)

# Temperature is the key, LED index is first item in "value" list
# RGB code is second item in the value list
LEDdict = {
  66: [0, (0, 0, 100)], # too cold, blue
  67: [1, (0, 0, 100)], 
  68: [2, (0, 0, 100)], 
  69: [3, (0, 0, 100)], 
  70: [4, (0, 100, 0)], # nice temp, green
  71: [5, (0, 100, 0)],
  72: [6, (0, 100, 0)], # Top-middle LED (index 6 / LED #7) for 68°F
  73: [7, (0, 100, 0)],
  74: [8, (0, 100, 0)],
  75: [9, (100, 0, 0)], # too hot, red
  76: [10,(100, 0, 0)],
  77: [11,(100, 0, 0)], 
}

# print title line
print("Lori's Weather Station Data:")

try:   
    while True:
        # Grab data from the sensor dictionary
        measurements = dht20.measurements
        # use some variables to make it easier to read code
        temp_C = measurements['t']
        temp_F = (temp_C * 1.8) + 32
        tempLookup = round(temp_F)
        humid = measurements['rh']
        
        if measurements['crc_ok']:
            
            if tempLookup not in LEDdict:                
                print(f"Temperature: {temp_F:3.1f}°F, {temp_C:3.1f}°C | Humidity: {humid:3.1f}% | Temp Out of Range", end = '\r')        
                # Clear the ring
                ring.fill((0,0,0))
                ring.write()
                
            else:
                print(f"Temperature: {temp_F:3.1f}°F, {temp_C:3.1f}°C | Humidity: {humid:3.1f}% | Temp In Range    ", end = '\r')        
                # Use our temperature variable with our dictionary
                # To convert it from the temperature to the LED index
                LEDindex = LEDdict[tempLookup][0]
                
                # Clear the ring
                ring.fill((0,0,0))
                # Light the index LED
                ring[LEDindex] = LEDdict[tempLookup][1] 
                ring.write()
            
        # Wait 2 seconds
        sleep(2)

except KeyboardInterrupt:
    # Clear the ring
    ring.fill((0,0,0))    
    ring.write()
