import RPi.GPIO as GPIO
import time
import sys
import os
import requests

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.IN)

global averagePower
global lastTime
global count

averagePower = 0
lastTime = 0

def countBlip(channel):
  global lastTime
  global averagePower  
  global count
  print "Blip"
  newTime = time.time()
  diff = newTime - lastTime
  lastTime = newTime
  power = 3600 / diff
  count = count + 1
  averagePower = (averagePower * (count - 1) + power) / count 

def logtoinflux(name, value) :
  payload = name + " value=" + str(value)
  print payload
  r = requests.post("http://influxdb:8086/write?db=el", data=payload)

GPIO.add_event_detect(11, GPIO.FALLING, callback=countBlip, bouncetime=200)

while True:
  count = 0
  time.sleep(20)
  updateText = "N:" + str(averagePower)
  if (averagePower < 12000):
    logtoinflux("effekt", averagePower)
  print updateText
  print GPIO.input(11)
  averagePower = 0
