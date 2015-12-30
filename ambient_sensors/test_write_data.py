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
from smbus import SMBus
from mpl3115a2 import *

#insert_to_db (inserts value to SQL database)

def insert_to_db(temp_BMP180, temp_MCP9808, temp_SHT15, temp_MPL3115, humid_SHT15, pressure_BMP180, pressure_MPL3115):
    db = MySQLdb.connect("localhost", "root", "ubcqdg", "sensor_database")
    cursor = db.cursor()
    time_sensor = time.time()
    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO sensor_tests(timestamp, temp_BMP180, temp_MCP9808, temp_SHT15, temp_MPL3115, humid_SHT15, pressure_BMP180, pressure_MPL3115) VALUES ('%d', '%f', '%f', '%f', '%f', '%.3f', '%f', '%f')" % (time_sensor, temp_BMP180, temp_MCP9808, temp_SHT15, temp_MPL3115, humid_SHT15, pressure_BMP180, pressure_MPL3115)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "failed to write to db"

    db.close()

#main program
#data pins 
SHT15_dataPin = 12
SHT15_clkPin = 16

#create sensor onjects
sensor_BMP = BMP085.BMP085()
sensor_MCP = MCP9808.MCP9808()
sensor_SHT15 = SHT1x(SHT15_dataPin, SHT15_clkPin, SHT1x.GPIO_BOARD)

#initialize

MPL3115_setup()
#print MPL3115_read_temp()
#print MPL3115_read_pressure()

GPIO.setwarnings(False)

sensor_MCP.begin()

print sensor_BMP.read_temperature()
print sensor_MCP.readTempC()
print sensor_SHT15.read_temperature_C()
print MPL3115_read_temp()
print sensor_SHT15.read_humidity()
print sensor_BMP.read_pressure()
print MPL3115_read_pressure()


insert_to_db(sensor_BMP.read_temperature(), sensor_MCP.readTempC(), sensor_SHT15.read_temperature_C(), MPL3115_read_temp(), sensor_SHT15.read_humidity(), sensor_BMP.read_pressure(), MPL3115_read_pressure())
