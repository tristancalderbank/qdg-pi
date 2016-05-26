# QDG Pi Project
# Quantum Degenerate Gases Lab (Madison Research Group)
# publish_data.py
# date: May 25, 2016
# author: tristan calderbank
# contact: tristan@alumni.ubc.ca
# purpose: This python script first connects to the redis server,
#          creates a 'pubsub' instance, subscribes to the appropriate
#          channels, and begins reading the sensors connected to the Pi.
#          It then publishes the data to the channels on the pubsub
#          instance to be recieved by the data collection computer.

from time import strftime
import redis
import smbus
from Adafruit_BME280 import *
import RPi.GPIO as GPIO

# configuration
room_name = "master"
server_ip = '10.1.137.253'
server_port = 6379
max_number_of_sensors = 8
digits_to_round_to = 2

# multiplexer 
I2C_address = 0x70
I2C_bus_number = 1
I2C_ch_4 = 0b00000001
I2C_ch_5 = 0b00000010
I2C_ch_6 = 0b00000100
I2C_ch_7 = 0b00001000
I2C_ch_3 = 0b00010000
I2C_ch_2 = 0b00100000
I2C_ch_1 = 0b01000000
I2C_ch_0 = 0b10000000

mux_channel = [I2C_ch_0, I2C_ch_1, I2C_ch_2, I2C_ch_3, I2C_ch_4, I2C_ch_5, I2C_ch_6, I2C_ch_7]

def set_mux_channel(i2c_channel_setup):
    bus = smbus.SMBus(I2C_bus_number)
    bus.write_byte(I2C_address,i2c_channel_setup)
    time.sleep(0.1)
#   print "TCA9548A I2C channel status:", bin(bus.read_byte(I2C_address))

def read_sensors(number_of_sensors):
	sensor_data = []
	for channel in range(0,number_of_sensors):

		try:
			set_mux_channel(mux_channel[channel])
			sensor = BME280(mode=BME280_OSAMPLE_8)
			temperature = round(sensor.read_temperature(), digits_to_round_to)
			pressure = round(sensor.read_pressure(), digits_to_round_to)
			humidity = round(sensor.read_humidity(), digits_to_round_to)
			sensor_data.append((temperature,pressure,humidity))

		except IOError: 
			print "Failed to read sensor channel " + str(channel)
			sensor_data.append("no_data")
	
	return sensor_data


def connect_to_server(server_ip,server_port):
	r = redis.StrictRedis(host=server_ip, port=server_port, db=0)
	connected = False
	while connected == False:
		try:
			server_connection = redis.StrictRedis(host=server_ip, port=server_port, db=0)
			server_connection.ping()
			connected = True
			print "Successfully connected to redis-server at " + server_ip +"."
		except redis.exceptions.ConnectionError:
			print "Couldn't connect to redis server at " + server_ip + ", trying again in 5 seconds..."
			time.sleep(5)

	return server_connection

def check_if_connected(server_connection, server_ip, server_port):
	try:
		server_connection.ping()
		print "Still connected to server at " + server_ip + "."	
	except redis.exceptions.ConnectionError:
		print "Server at " + server_ip + " was disconnected, trying again..."
		server_connection = connect_to_server(server_ip, server_port)

	return server_connection


# connect to the Redis server
server_connection = connect_to_server(server_ip, server_port)

# main loop
while True:
	sensor_data = read_sensors(max_number_of_sensors)
	timestamp = strftime("%Y-%m-%d %H:%M:%S")
	print timestamp
	sensor_data.insert(0, timestamp)

	server_connection = check_if_connected(server_connection, server_ip, server_port)	
	server_connection.publish(room_name, sensor_data)
	time.sleep(1)


