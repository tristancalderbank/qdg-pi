#Basic imports
import sys
import math
import random
import os
import time
import datetime
import redis
import string

#Sensors
import Adafruit_BMP.BMP085 as BMP085
import RPi.GPIO as GPIO
from sht1x.Sht1x import Sht1x as SHT1x

#data pins for SHT15

SHT15_dataPin = 12
SHT15_clkPin = 16
    
GPIO.setwarnings(False)

#BMP 9805 for pressure readings
sensor_BMP = BMP085.BMP085()

#SHT15 for temperature and humidity
sensor_SHT15 = SHT1x(SHT15_dataPin, SHT15_clkPin, SHT1x.GPIO_BOARD)



#connect to the Redis server
r = redis.StrictRedis(host='localhost', port=6379, db=0)

#open up a pubsub instance
pubsub = r.pubsub(ignore_subscribe_messages=True)

pubsub.subscribe('timestamp')
pubsub.subscribe('temperature')
pubsub.subscribe('pressure')
pubsub.subscribe('humidity')


while True:

        dt = datetime.datetime.now()
        dt = dt.replace(microsecond=0) 
        temperature = round(sensor_SHT15.read_temperature_C(), 2)
        pressure = sensor_BMP.read_pressure()
        humidity = round(sensor_SHT15.read_humidity(), 2)

	r.publish('timestamp', dt)
	r.publish('temperature', temperature) 
	r.publish('pressure', pressure) 
	r.publish('humidity', humidity) 

	print pubsub.get_message()
	print pubsub.get_message()
	print pubsub.get_message()
	print pubsub.get_message()

	time.sleep(5)










