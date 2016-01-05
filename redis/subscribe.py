#Basic imports
import sys
import math
import random
import os
import time
import datetime
import redis
import string

#connect to the Rasperry Pi Redis server
r = redis.StrictRedis(host='192.168.1.75', port=6379, db=0)

#open up a pubsub instance
pubsub = r.pubsub(ignore_subscribe_messages=True)

r.subscribe('temperature')

while True:
	print pubsub.get_message()
	time.sleep(60)



#print pubsub.get_message()
#print pubsub.get_message()

#print sensor_SHT15.read_temperature_C()
#print sensor_SHT15.read_humidity()
#print sensor_BMP.read_pressure()









