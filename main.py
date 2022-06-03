import sys
import time
import random
s='ahmed eat an apple'
x=input()
if x == "start":
    t = 3
    print(t)
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        print(t)
print(s)
start=time.time()
x=input()
end=time.time()
print(end-start)



