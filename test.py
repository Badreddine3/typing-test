import sys
import time
import random
import difflib

def typeTest():
    f = open('wl.txt', 'r')
    wordList = f.read().split("\n")
    #s='ahmed eat an apple'
    s = random.choice(wordList)
    print("Type '1' to begin.")
    x=input()
    print('======')
    if x == "1":
        t = 3
        print(t)
        while t:
            #mins, secs = divmod(t, 60)
            #timer = '{:02d}:{:02d}'.format(mins, secs)
            print(t, end="\r")
            time.sleep(1)
            t -= 1
            print(t)
    print(s)
    start=time.time()
    x=input()
    end=time.time()
    words = s.split(' ')
    ccount = len(s)
    wcount = len(words)
    typeTime=end-start
    typeTimeMin=typeTime/60
    accuracy = difflib.SequenceMatcher(None, s, x).ratio()
    print(f"Time = {typeTime}")
    print(f"CPM = {ccount/(typeTimeMin)} ")
    print(f"WPM = {wcount/(typeTimeMin)}")
    print(f"Accuracy = {accuracy}")



