#!/usr/bin/env python
# /etc/init.d/final.py
### BEGIN INIT INFO
# Provides:          final.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        string = str(subprocess.check_output(["/opt/vc/bin/tvservice", "-s"]))
        print(string)
        substring = "TV is off"

        if substring in string:
            print ("TV off erkannt")
            subprocess.call(["/opt/vc/bin/tvservice", "-p"], shell=False)
            subprocess.call(["sudo", "/bin/chvt", "6"], shell=False)
            subprocess.call(["sudo", "/bin/chvt", "7"], shell=False)

        GPIO.setup(25, GPIO.OUT, initial=1)
        GPIO.output(25, 0)  # this is our simulated button press
        time.sleep(0.2)  # hold button for 0.2 seconds
        GPIO.output(25, 1)  # release button
        GPIO.setup(25, GPIO.IN)  # set port back to input (re-enables buttons)

