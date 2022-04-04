import RPi.GPIO as GPIO

import time

def dec2bin(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def num2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac,signal)

def adc():
    value = 7
    num = 0
    for i in range(8):
        num +=2**value
        signal = num2dac(num)
        voltage = num / 256 * 3.3
        time.sleep(0.01)
        comparatorV = GPIO.input(comp)
        if comparatorV == 0:
            num -=2**value
        value -= 1
    print("ADC value={:^3}->{}, input viltage = {:.2f}".format(num,voltage,voltage))
    return num

GPIO.setmode(GPIO.BCM)

clean =[0,0,0,0,0,0,0,0]
dac = [26,19,13,6,5,11,9,10]
comp = 4
troyka = 17
GPIO.setup(troyka,GPIO.OUT,initial = 1)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(comp,GPIO.IN)

try:
    while(1):
        adc()
finally:
    GPIO.output(dac,clean)
    GPIO.cleanup()
