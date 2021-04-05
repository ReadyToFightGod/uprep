import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt
import time
import math

chan_list = [10, 9, 11, 5, 6, 13, 19, 26]
GPIO.setmode(GPIO.BCM)
GPIO.setup(chan_list, GPIO.OUT)

def dec2bin(value):
    N, p , n = 7, 0, []
    if value >= 256:
        value %= 256
    while N > 0:
        p = int(value/2**N)
        if p == 1:
            n.append(1)
            value -= 2**N
        else:
            n.append(0) 
        N -= 1
    n.append(value)
    return n

def num2dac(a):
    global chan_list
    bi_num = dec2bin(a)
    k = 7
    for e in chan_list:
        if bi_num[k] == 1:
            GPIO.output(e, 1)
            k -= 1
        else:
            GPIO.output(e, 0)
            k -= 1

try:
    tIme, frequency, samplingFrequency = 0, 0, 0
    while tIme != -1 or frequency != -1 or samplingFrequency != -1:
        tIme = int(input("Enter time (-1 to exit): ", ))
        frequency = int(input("Enter frequency (-1 to exit): ", ))
        samplingFrequency = int(input("Enter sampling frequency (-1 to exit): ", ))
        t = np.arange(0, tIme, 1/samplingFrequency)
        amp = np.sin(t*2*3.14*frequency)
        for i in range(len(amp)):
            amp[i] = math.floor(127.5*(amp[i]+1))
        plt.plot(t, amp)
        plt.title("SIN")
        plt.xlabel("time")
        plt.ylabel("amp sin(time)")
        plt.show()
        for i in range(len(amp)):
#            bi_num = [int(bin(amp[i])[2:].zfill(9)[_]) for _ in range(1,9)]
            num2dac(amp[i])
            time.sleep(1/samplingFrequency)

except KeyboardInterrupt:
    GPIO.output(chan_list, 0)

finally:
    GPIO.output(chan_list, 0)