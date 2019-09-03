#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep, strftime, time
import time
import sys
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)

#define the pin that goes to the circuit
pin_to_circuit = 12

def rc_time (pin_to_circuit):
    count = 0

    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(pin_to_circuit, GPIO.IN)
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1
    return count

lightVal = rc_time(pin_to_circuit)
lightThresh = 1000

def led_control():
    if lightVal >= lightThresh:
        GPIO.output(16,GPIO.HIGH)
    if lightVal <= lightThresh:
        GPIO.output(16,GPIO.LOW)

def write_data():
     with open("sensorlog", "a") as log:
          log.write("{0}: Light Value={1}, LED={2}\n".format(strftime("%Y-%m-%d %H:%M:%S "), lightVal, GPIO.input(16)))

def write_temp():
     with open("templdr", "w") as log:
          log.write('"{0}: Light Value={1}, LED={2}"\n'.format(strftime("%Y-%m-%d %H:%M:%S "), lightVal, GPIO.input(16)))

def disco_post():
    os.system('/usr/bin/python3 /home/pi/bin/discohook.py "CoupDeforce reporting Light & LED Values:\n"' + open('templdr').read())

try:
    # Main loop
    while True:
        led_control()
        write_data()
        write_temp()
        disco_post()
        break
