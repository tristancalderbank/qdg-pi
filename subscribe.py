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


master_table_IP = '192.168.1.65'
MOL_lab_IP = '10.42.0.43'

# gets a valid message

def get_message(pubsub):
    while True:
        temp = pubsub.get_message()
        if (temp is not None):
            return temp

def read_message(pubsub):

    timestamp = get_message(pubsub)
    if (timestamp['channel'] == 'timestamp'):
        timestamp = timestamp['data']
        print timestamp
        temperature = get_message(pubsub)['data']
        print temperature
        pressure = get_message(pubsub)['data']
        print pressure
        humidity = get_message(pubsub)['data']
        print humidity

        return timestamp, temperature, pressure, humidity


# file paths
master_table_directory = "/var/www/html/data/master-table/"
MOL_lab_directory = "/var/www/html/data/MOL-lab/"

# connect to the Rasperry Pi Redis server
redis_master_table = redis.StrictRedis(host=master_table_IP, port=6379, db=0)
redis_MOL_lab = redis.StrictRedis(host=MOL_lab_IP, port=6379, db=0)

# open up a pubsub instance
pubsub_master_table = redis_master_table.pubsub(ignore_subscribe_messages=True)
pubsub_MOL_lab = redis_MOL_lab.pubsub(ignore_subscribe_messages=True)

pubsub_master_table.subscribe('timestamp')
pubsub_master_table.subscribe('temperature')
pubsub_master_table.subscribe('pressure')
pubsub_master_table.subscribe('humidity')

pubsub_MOL_lab.subscribe('timestamp')
pubsub_MOL_lab.subscribe('temperature')
pubsub_MOL_lab.subscribe('pressure')
pubsub_MOL_lab.subscribe('humidity')

# main loop

while True:

# make sure we get the messages in the right order
    

        timestamp, temperature, pressure, humidity = read_message(pubsub_master_table)

        if(timestamp != None):
            # open file for writing
            file_name = (time.strftime("%Y-%m-%d")) + ".csv"
            
            if not os.path.exists(master_table_directory):
                    os.makedirs(master_table_directory)

            file_path = master_table_directory + file_name

            data_file = open(file_path, "ab")
            file_writer = csv.writer(data_file)
            file_writer.writerow([timestamp, temperature, pressure, humidity]) 
            data_file.close()

        timestamp, temperature, pressure, humidity = read_message(pubsub_MOL_lab)

        if(timestamp != None):
            # open file for writing
            file_name = (time.strftime("%Y-%m-%d")) + ".csv"
            
            if not os.path.exists(MOL_lab_directory):
                    os.makedirs(MOL_lab_directory)

            file_path = MOL_lab_directory + file_name

            data_file = open(file_path, "ab")
            file_writer = csv.writer(data_file)
            file_writer.writerow([timestamp, temperature, pressure, humidity]) 
            data_file.close()


