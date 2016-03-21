#Basic imports
import sys
import math
import random
import os
import time
import redis
import string
from datetime import datetime
from pytz import timezone
import pytz
#Sensors
from Adafruit_BME280 import *

sensor = BME280(mode=BME280_OSAMPLE_8)

ip = '10.1.137.203'

#connect to the Redis server
r = redis.StrictRedis(host=ip, port=6379, db=0)

#open up a pubsub instance
pubsub = r.pubsub(ignore_subscribe_messages=True)

pubsub.subscribe('timestamp')
pubsub.subscribe('temperature')
pubsub.subscribe('pressure')
pubsub.subscribe('humidity')

debug_time = 0

while True:

        dt = time.time()
        
        temperature = round(sensor.read_temperature(), 2)
        pressure = round(sensor.read_pressure(), 2)
        humidity = round(sensor.read_humidity(), 2)

        r.publish('timestamp', dt)
        r.publish('temperature', temperature) 
        r.publish('pressure', pressure) 
        r.publish('humidity', humidity) 

        print pubsub.get_message()
        print pubsub.get_message()
        print pubsub.get_message()
        print pubsub.get_message()

	debug_time+=1
	print debug_time

        time.sleep(10)







