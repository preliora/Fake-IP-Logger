import random as r
import time

ip = str(r.randrange(100, 999)) + '.' + str(r.randrange(100, 999)) + '.' + str(r.randrange(1, 9)) + '.' + str(r.randrange(1, 9))

print('Cracking IP address...')
time.sleep(1)
print("Your ip is " + ip)
time.sleep(1000)
