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

#Sensors
import Adafruit_BMP.BMP085 as BMP085
import RPi.GPIO as GPIO
from sht1x.Sht1x import Sht1x as SHT1x

#data pins for SHT15

SHT15_dataPin = 12
SHT15_clkPin = 16
    
#GPIO.setwarnings(False)

#BMP 9805 for pressure readings
sensor_BMP = BMP085.BMP085()

#SHT15 for temperature and humidity
sensor_SHT15 = SHT1x(SHT15_dataPin, SHT15_clkPin, SHT1x.GPIO_BOARD)

print sensor_SHT15.read_temperature_C()
print sensor_SHT15.read_humidity()
print sensor_BMP.read_pressure())
