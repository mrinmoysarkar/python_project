import RPi.GPIO as GPIO
import time


def led(state):

    GPIO.setmode(GPIO.BCM)

    LED_PIN = 25 
    GPIO.setup(LED_PIN, GPIO.OUT)
    
    if state:
        GPIO.output(LED_PIN, True)
        print "TURNING LED ON"
    else:
        GPIO.output(LED_PIN, False)
        print "TURNING LED OFF"
