import subprocess

a = subprocess.call(["/opt/vc/bin/tvservice", "-s"], shell=False)
print (a)

