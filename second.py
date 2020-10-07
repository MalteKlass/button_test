import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:

        subprocess.call(["/opt/vc/bin/tvservice", "-p"], shell=False)
        subprocess.call(["sudo", "/bin/chvt", "6"], shell=False)
        subprocess.call(["sudo", "/bin/chvt", "7"], shell=False)
        time.sleep(1)

