import RPi.GPIO as P
import time 

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
troyka = 17
comp = 4

P.setmode(P.BCM)
P.setup(dac, P.OUT)
P.setup(troyka, P.OUT, initial = P.HIGH)
P.setup(comp, P.IN)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def num2dac(value):
    P.output(dac, decimal2binary(value))

def adc():
    for value in range(256):            
        num2dac(value)
        time.sleep(0.005)
        compValue = P.input(comp)
        if compValue == 0:   
            return value

try:
    while True:
            val = adc()
            print("ADC value = {:^3}, input voltage = {:.2f}".format(val, val / levels * 3.3))
finally:
    dac = [0, 0, 0, 0, 0, 0, 0, 0]
    comp = [0]
    troyka = [0]
    P.cleanup()
    