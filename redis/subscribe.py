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


<<<<<<< HEAD

# file paths
data_folder_name = "TempData"
=======
>>>>>>> 61581a2c0c442eb54e89366a7224f512cc3e64e5



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
#try:

while True:

# make sure we get the messages in the right order

<<<<<<< HEAD
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

        # open file for writing
        directory_name = "/home/tristiano/Desktop/" + data_folder_name + "/" + timestamp[0:4] + "/"           + timestamp[5:7] + "/"

        file_name = timestamp[8:10] + ".csv"
        
        if not os.path.exists(directory_name):
                os.makedirs(directory_name)

        file_path = directory_name + file_name

        data_file = open(file_path, "ab")
        file_writer = csv.writer(data_file)

        file_writer.writerow([timestamp, temperature, pressure, humidity]) 
        data_file.close()

#except:
    #data_file.close()
=======
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

# open file for writing
	    data_file = open("/home/steam/Desktop/DATA.csv", "ab")
	    file_writer = csv.writer(data_file)
            file_writer.writerow([timestamp, temperature, pressure, humidity]) 
	    data_file.close()

except:
    data_file.close()
>>>>>>> 61581a2c0c442eb54e89366a7224f512cc3e64e5




