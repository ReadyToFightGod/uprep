import RPi.GPIO as GPIO
import time

chan_list = [10, 9, 11, 5, 6, 13, 19, 26]
comp_pin = 4
power_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(chan_list, GPIO.OUT)
GPIO.setup(power_pin, GPIO.OUT)
GPIO.setup(comp_pin, GPIO.IN)
GPIO.output(power_pin, 1)

def num2dac(a):
    bi_num = []
    for j in range(8):
        bi_num.append(a%2)
        a //= 2
    GPIO.output(chan_list, bi_num)

def bin_search():
    l = 0
    r = 256
    while r - l > 1:
        middle = (r + l) // 2
        num2dac(middle)
        time.sleep(0.001)
        if not GPIO.input(comp_pin):
            r = middle
        else:
            l = middle
    return l

try:
    while True:
        value = bin_search()
        volt = round(float(3.3 * value / 256), 2)
        print(value, ' = ', volt, 'V')
            
except KeyboardInterrupt:
    GPIO.output(chan_list, 0)
    GPIO.output(power_pin, 0)

finally:
    GPIO.output(chan_list, 0)
    GPIO.output(power_pin, 0)