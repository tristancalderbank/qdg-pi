# qdg-pi
Python script that runs on a Raspberry Pi and publishes data from an array of multiplexed BME280 sensors to a host computer via redis. This project uses the TCA9548A I2C multiplexer.

## Instructions:

1) First enable I2C on the pi by following this guide:

https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

2) Configure the timezone on the pi by running the following command:

```bash
sudo dpkg-reconfigure tzdata
```

3) Run pi-setup.py to install python dependencies and add cronjob for starting the publishing script if the pi reboots

4) Edit publish-data.py and change the ip_address variable to point to the host computer

## How It Works
The publishing script writes a single byte to the multiplexer I2C address to select which sensor to read. 

By using redis, a database server running on the host computer, the pi can create a "pubsub" channel to which it publishes data collected from the connected sensors. The host computer subscribes to this channel and saves the data into csv format.

