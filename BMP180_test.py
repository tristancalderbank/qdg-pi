# BMP180 Temperature sensor
# Tristan Calderbank
# QDG Labs

import time
import Adafruit_BMP.BMP085 as BMP085
import Adafruit_MCP9808.MCP9808 as MCP9808
from sht1x.Sht1x import Sht1x as SHT1x

dataPin = 18
clkPin = 23

sensor_BMP = BMP085.BMP085()
sensor_MCP = MCP9808.MCP9808()
sensor_SHT15 = SHT1x(dataPin, clkPin, SHT1x.GPIO_BOARD)

sensor_MCP.begin()

while 1:
#    print "BMP180 Temp = %f" % sensor_BMP.read_temperature()
#    print "MCP9808 Temp = %f" % sensor_MCP.readTempC()

    temperature = sensor_SHT15.read_temperature_C()
    humidity = sht1x.read_humidity()
    dewPoint = sht1x.calculate_dew_point(temperature, humidity)

    print "temp = %f" % temperature
    print "humidity = %f" % humidity
    print "dew point = %f" % dewPoint
        
    time.sleep(2)
