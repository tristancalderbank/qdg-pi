#Sensor Logger
#QDG Labs
#
#write_data.py
#Takes temperature, humidity, and pressure
#and writes it to an SQL database hosted
#on a nginx server on the raspberry pi
#

#Basic imports
import sys
import math
import random
import os
import time
import datetime

#Mysql imports
import MySQLdb

#Sensors
import RPi.GPIO as GPIO


#insert_to_db (inserts value to SQL database)

def insert_to_db():
    db = MySQLdb.connect("localhost", "root", "ubcqdg", "sensor_database")
    cursor = db.cursor()
    time_sensor = time.time()
    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO motion_sensor(timestamp) VALUES ('%d')" % (time_sensor)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "failed to write to db"

    db.close()

PIR = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN, GPIO.PUD_DOWN)

while 1:
    pirState = GPIO.input(PIR)
    if(pirState == True):
        insert_to_db()
        time.sleep(15)




