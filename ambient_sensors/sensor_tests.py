# BMP180 Temperature sensor
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

while 1:
    print "\n"
    print datetime.now()
    print "Temperature (C)"
    print "---------------"
    print "BMP180: %.1f" % sensor_BMP.read_temperature()
    print "MCP9808: %.3f" % sensor_MCP.readTempC()
    print "SHT15: %.2f" % sensor_SHT15.read_temperature_C()
    print "MPL3115: %.4f" % MPL3115_read_temp()

    print "\nHumidity (%)"
    print "--------------"    
    print "SHT15: %.2f" % sensor_SHT15.read_humidity()

    print "\nPressure (Pa)"
    print "---------------"
    print "BMP180: %.0f" % sensor_BMP.read_pressure()
    print "MPL3115: %.2f" % MPL3115_read_pressure()
        
    time.sleep(15)
