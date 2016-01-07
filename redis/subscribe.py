#Basic imports
import sys
import math
import random
import os
import time
import datetime
import redis
import string
import csv


file_writer = csv.writer(open("/home/tristiano/Desktop/DATA.csv", "wb"))

file_writer.writerow(["Time", "Temperature", "Pressure", "Humidity"])




#connect to the Rasperry Pi Redis server
r = redis.StrictRedis(host='192.168.1.75', port=6379, db=0)

#open up a pubsub instance
pubsub = r.pubsub(ignore_subscribe_messages=True)


pubsub.subscribe('timestamp')
pubsub.subscribe('temperature')
pubsub.subscribe('pressure')
pubsub.subscribe('humidity')



while True:
	temp = pubsub.get_message()
	if (temp is not None):
		print temp['data']














