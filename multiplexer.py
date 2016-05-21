import smbus
import time
import RPi.GPIO as GPIO
from Adafruit_BME280 import *



# Multiplexer stuff

I2C_address = 0x70
I2C_bus_number = 1
I2C_ch_4 = 0b00000001
I2C_ch_5 = 0b00000010
I2C_ch_6 = 0b00000100
I2C_ch_7 = 0b00001000
I2C_ch_3 = 0b00010000
I2C_ch_2 = 0b00100000
I2C_ch_1 = 0b01000000
I2C_ch_0 = 0b10000000

mux_channel = [I2C_ch_0, I2C_ch_1, I2C_ch_2, I2C_ch_3, I2C_ch_4, I2C_ch_5, I2C_ch_6, I2C_ch_7]


def I2C_setup(i2c_channel_setup):
    bus = smbus.SMBus(I2C_bus_number)
    bus.write_byte(I2C_address,i2c_channel_setup)
    time.sleep(0.1)
#    print "TCA9548A I2C channel status:", bin(bus.read_byte(I2C_address))

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17,GPIO.OUT)
#GPIO.output(17,True)

for channel in range(0,7):
	I2C_setup(mux_channel[channel])
	sensor = BME280(mode=BME280_OSAMPLE_8)
	temperature = round(sensor.read_temperature(), 2)
	print "Channel " + str(channel) + ": " + str(temperature)

while True:
	print "Enter channel to read: "
	channel = input()
	I2C_setup(mux_channel[channel])
	sensor = BME280(mode=BME280_OSAMPLE_8)
	temperature = round(sensor.read_temperature(), 2)
	print temperature




#GPIO.output(17,False)
#time.sleep(1)
#GPIO.output(17,True)



