#!/usr/bin/python3
from gpiozero import CPUTemperature
from time import sleep, strftime, time
import sys
import os

cpu = CPUTemperature()

def write_data(temp):
        with open("sensorlog", "a") as log:
                log.write("{0}: CPU TempC={1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

def write_temp(temp):
        with open("tempcpu", "w") as log:
                log.write('"{0}: CPU TempC={1}"\n'.format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

def disco_post():
    os.system('/usr/bin/python3 /home/pi/bin/discohook.py "CoupDeforce reporting CPU Temperature:\n"' + open('tempcpu').read())

while True:
     temp = cpu.temperature
     write_data(temp)
     write_temp(temp)
     disco_post()
     break
