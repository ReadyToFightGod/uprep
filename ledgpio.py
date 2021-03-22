import RPi.GPIO as GPIO
import time

chan_list = [24, 25, 8, 7, 12, 16, 20, 21]
GPIO.setmode(GPIO.BCM)

def lightUp(ledNumber, period):
    global chan_list
    num = chan_list[ledNumber]
    GPIO.setup(num, GPIO.OUT)
    while True:
        GPIO.output(num, 1)
        time.sleep(period)
        GPIO.output(num, 0)
        time.sleep(period)
        break

def blink(ledNumber, blinkCount, blinkPeriod):
    global chan_list
    num = chan_list[ledNumber]
    GPIO.setup(num, GPIO.OUT)
    for i in range(blinkCount):
        GPIO.output(num, 1)
        time.sleep(blinkPeriod)
        GPIO.output(num, 0)
        time.sleep(blinkPeriod)

def runningLight(count, period):
    global chan_list
    for i in range(count):
        for e in chan_list:
            GPIO.setup(e, GPIO.OUT)
            GPIO.output(e, 1)
            time.sleep(period)
            GPIO.output(e, 0)

def runningDark(count, period):
    global chan_list
    GPIO.setup(chan_list, GPIO.OUT)
    GPIO.output(chan_list, 1)
    for i in range(count):
        for e in chan_list:
            GPIO.output(e, 0)
            time.sleep(period)
            GPIO.output(e, 1)
    GPIO.output(chan_list, 0)

def decToBinList(decNumber):
    N = 7
    p = 0
    n = []
    if decNumber >= 256:
        decNumber %= 256 
    while N > 0:
        p = int(decNumber/2**N)
        if p == 1:
            n.append(1)
            decNumber -= 2**N
        else:
            n.append(0)
        N -= 1
    n.append(decNumber)
    return n

def lightNumber(number):
    global chan_list
    GPIO.setup(chan_list, GPIO.OUT)
    bi_num = decToBinList(number)
    i = 7
    for e in chan_list:
        if bi_num[i] == 1:
            GPIO.output(e, 1)
            i -= 1
        else:
            GPIO.output(e, 0)
            i -= 1
    time.sleep(5)
    GPIO.output(chan_list, 0)

def runningPattern(pattern, direction):
    global chan_list
    GPIO.setup(chan_list, GPIO.OUT)
    j = 0
    while True:
        bi_num = decToBinList(pattern<<j%8)
        if direction == -1:
            i = 7
            for e in chan_list:
                if bi_num[i] == 1:
                    GPIO.output(e, 1)
                    time.sleep(0.5)
                    i -= 1
                else:
                    GPIO.output(e, 0)
                    i -= 1   
        #elif direction == 1:
            #i = 7
            #for e in chan_list:
                #if bi_num[i] == 1:
                    #GPIO.output(e, 1)
                    #time.sleep(0.5)
                    #i -= 1
                #else:
                    #GPIO.output(e, 0)
                    #i -= 1
        else:
            print(False)
        GPIO.output(chan_list, 0)
        j += 1
        i = 7

#a = lightUp(6, 5)
#b = blink(3, 5, 1)
#c = runningLight(3, 1)
#d = runningDark(3, 1)
#print(decToBinList(8))
#e = lightNumber(3)
#f = runningPattern(3, -1)
