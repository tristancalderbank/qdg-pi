# Adafruit Sensors
# Tristan Calderbank
# QDG Labs

import time
from datetime import datetime
import Adafruit_BMP.BMP085 as BMP085
import Adafruit_MCP9808.MCP9808 as MCP9808
import RPi.GPIO as GPIO
from sht1x.Sht1x import Sht1x as SHT1x
from smbus import SMBus
from mpl3115a2 import *
from Adafruit_BME280 import *
import os
import csv

#data pins 
SHT15_dataPin = 12
SHT15_clkPin = 16

#create sensor onjects
sensor_BMP = BMP085.BMP085()
#sensor_MCP = MCP9808.MCP9808()
sensor_SHT15 = SHT1x(SHT15_dataPin, SHT15_clkPin, SHT1x.GPIO_BOARD)

#initialize

#MPL3115_setup()
#print MPL3115_read_temp()
#print MPL3115_read_pressure()

GPIO.setwarnings(False)

   
sensor = BME280(mode=BME280_OSAMPLE_8)

#sensor_MCP.begin()

while 1:


    degrees = sensor.read_temperature()
    pascals = sensor.read_pressure()
    hectopascals = pascals / 100
    humidity = sensor.read_humidity()


    print "\n"
    print datetime.now()
    print "Temperature (C)"
    print "---------------"
    print "BME280: %.2f" % degrees
#    print "MCP9808: %.3f" % sensor_MCP.readTempC()
    print "SHT15: %.2f" % sensor_SHT15.read_temperature_C()
#    print "MPL3115: %.4f" % MPL3115_read_temp()

    print "\nHumidity (%)"
    print "--------------"    
    print "SHT15: %.2f" % sensor_SHT15.read_humidity()
    print "BME280: %.2F" % humidity

    print "\nPressure (Pa)"
    print "---------------"
    print "BMP280: %.0f" % pascals
#    print "MPL3115: %.2f" % MPL3115_read_pressure()

    

    # open file for writing
    directory_name = "/home/pi/Desktop/"

    file_name = "sensors.csv"
            
    if not os.path.exists(directory_name):
                    os.makedirs(directory_name)

    file_path = directory_name + file_name

    data_file = open(file_path, "ab")
    file_writer = csv.writer(data_file)

    file_writer.writerow([datetime.now(), sensor_SHT15.read_temperature_C() , degrees, sensor_SHT15.read_humidity(), humidity, pascals]) 
    data_file.close()











        
    time.sleep(60)
