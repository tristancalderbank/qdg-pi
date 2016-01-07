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


# gets a valid message

def get_message():
    while True:
        temp = pubsub.get_message()
        if (temp is not None):
            return temp


# open file for writing
data_file = open("/home/tristiano/Desktop/DATA.csv", "ab")
file_writer = csv.writer(data_file)




# connect to the Rasperry Pi Redis server
r = redis.StrictRedis(host='192.168.1.75', port=6379, db=0)

# open up a pubsub instance
pubsub = r.pubsub(ignore_subscribe_messages=True)


pubsub.subscribe('timestamp')
pubsub.subscribe('temperature')
pubsub.subscribe('pressure')
pubsub.subscribe('humidity')


# main loop
#-----------
try:

    while True:

# make sure we get the messages in the right order

        timestamp = get_message()
        if (timestamp['channel'] == 'timestamp'):
            timestamp = timestamp['data']
            print timestamp
            temperature = get_message()['data']
            print temperature
            pressure = get_message()['data']
            print pressure
            humidity = get_message()['data']
            print humidity

            file_writer.writerow([timestamp, temperature, pressure, humidity]) 

except:
    data_file.close()




