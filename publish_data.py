#Basic imports
import sys
import math
import random
import os
import time
import redis
import string
import smbus
from datetime import datetime
from pytz import timezone
import pytz
#Sensors
from Adafruit_BME280 import *
import RPi.GPIO as GPIO


ip = '10.1.137.162'

#connect to the Redis server
r = redis.StrictRedis(host=ip, port=6379, db=0)

#open up a pubsub instance
pubsub = r.pubsub(ignore_subscribe_messages=True)

pubsub.subscribe('timestamp')
pubsub.subscribe('temperature')
pubsub.subscribe('pressure')
pubsub.subscribe('humidity')

debug_time = 0



# Multiplexer stuff

I2C_address = 0x76
I2C_bus_number = 1
I2C_ch_0 = 0b00000001
I2C_ch_1 = 0b00000010
I2C_ch_2 = 0b00000100
I2C_ch_3 = 0b00001000
I2C_ch_4 = 0b00010000
I2C_ch_5 = 0b00100000
I2C_ch_6 = 0b01000000
I2C_ch_7 = 0b10000000

def I2C_setup(i2c_channel_setup):
    bus = smbus.SMBus(I2C_bus_number)
    bus.write_byte(I2C_address,i2c_channel_setup)
    time.sleep(0.1)
    #print "TCA9548A I2C channel status:", bin(bus.read_byte(I2C_address))


channel = 1;

while True:

	if(channel == 1):
		channel = 0
	else:
		channel = 1	

	if(channel == 1):
		I2C_setup(I2C_ch_1)
	else:
		I2C_setup(I2C_ch_0)

	sensor = BME280(mode=BME280_OSAMPLE_8)
        dt = time.time()

        
        temperature = round(sensor.read_temperature(), 2)
        pressure = round(sensor.read_pressure(), 2)
        humidity = round(sensor.read_humidity(), 2)

        r.publish('timestamp', dt)
        r.publish('temperature', temperature) 
        r.publish('pressure', pressure) 
        r.publish('humidity', humidity) 

	if(channel == 1):
		print 'reading sensor 1...'#	else:
	else:
		print 'reading sensor 0...'

        print pubsub.get_message()
        print pubsub.get_message()
        print pubsub.get_message()
        print pubsub.get_message()

	debug_time+=1
	print debug_time


        time.sleep(2)
	



