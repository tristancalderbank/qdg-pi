import RPi.GPIO as GPIO
import time
PIR = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN, GPIO.PUD_DOWN)


print GPIO.input(PIR)

while 1:
    pirState = GPIO.input(PIR)
    if (pirState == True):
        print "hey!"
    else:
        print "hmm"

    time.sleep(1)

