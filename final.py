import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        GPIO.setup(25, GPIO.OUT, initial=1)
        GPIO.output(25, 0)  # this is our simulated button press
        time.sleep(0.2)  # hold button for 0.2 seconds
        GPIO.output(25, 1)  # release button
        GPIO.setup(25, GPIO.IN)  # set port back to input (re-enables buttons)

