import subprocess
import time

a = subprocess.check_output(["/opt/vc/bin/tvservice", "-s"], shell=False)
print ("Erster Status ist:" + a)
time.sleep(5)
subprocess.call(["/opt/vc/bin/tvservice", "-p"], shell=False)
subprocess.call(["sudo", "/bin/chvt", "6"], shell=False)
subprocess.call(["sudo", "/bin/chvt", "7"], shell=False)
b = subprocess.check_output(["/opt/vc/bin/tvservice", "-s"], shell=False)
print ("Zweiter Status ist:" + b)
time.sleep(5)
subprocess.call(["/opt/vc/bin/tvservice", "-o"], shell=False)
c = subprocess.check_output(["/opt/vc/bin/tvservice", "-s"], shell=False)
print ("Dritter Status ist:" + c)



