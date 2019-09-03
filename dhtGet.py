#!/usr/bin/python3
import sys
import os
import subprocess
import Adafruit_DHT
from time import sleep, strftime, time

humidity, temperature = Adafruit_DHT.read_retry(11,4)


def write_data():
    with open("sensorlog", "a") as log:
        log.write("{0}: tempC={1} hum%={2}\n".format(strftime("%Y-%m-%d %H:%M:%S "), temperature, humidity))

def write_temp():
    with open("tempdht", "w") as log:
        log.write('"{0}: tempC={1} hum%={2}"\n'.format(strftime("%Y-%m-%d %H:%M:%S "), temperature, humidity))


def disco_post():
    os.system('/usr/bin/python3 /home/pi/bin/discohook.py "CoupDeforce reporting DHT Values:\n"' + open('tempdht').read())

while True:
        write_data()
        write_temp()
        disco_post()
        break
