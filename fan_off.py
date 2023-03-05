import sys
sys.path.append('/storage/.kodi/addons/virtual.rpi-tools/lib')
import RPi.GPIO as GPIO
import time

fan_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_pin, GPIO.OUT)
GPIO.output(fan_pin, GPIO.LOW)