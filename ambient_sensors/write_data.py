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
import Adafruit_BMP.BMP085 as BMP085
import Adafruit_MCP9808.MCP9808 as MCP9808
import RPi.GPIO as GPIO
from sht1x.Sht1x import Sht1x as SHT1x

#insert_to_db (inserts value to SQL database)

def insert_to_db(temperature, humidity, pressure):
    db = MySQLdb.connect("localhost", "root", "ubcqdg", "sensor_database")
    cursor = db.cursor()
    time_sensor = time.time()
    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO sensor_data_table(timestamp, temperature, humidity, pressure) VALUES ('%d', '%f', '%.2f', '%f' )" % (time_sensor, temperature, humidity, pressure)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

#main program
#uses

#data pins for SHT15

SHT15_dataPin = 12
SHT15_clkPin = 16
    
GPIO.setwarnings(False)

#BMP 9805 for pressure readings
sensor_BMP = BMP085.BMP085()

#SHT15 for temperature and humidity
sensor_SHT15 = SHT1x(SHT15_dataPin, SHT15_clkPin, SHT1x.GPIO_BOARD)

insert_to_db(sensor_SHT15.read_temperature_C(), sensor_SHT15.read_humidity(), sensor_BMP.read_pressure())
