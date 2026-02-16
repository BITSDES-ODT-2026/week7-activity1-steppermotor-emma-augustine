from machine import Pin
import time

in1 = Pin(5,Pin.OUT)
in2 = Pin(18,Pin.OUT)
in3 = Pin(19,Pin.OUT)
in4 = Pin(22,Pin.OUT)

list = [[1,0,0,0] ,[0,1,0,0],[0,0,1,0],[0,0,0,1]]

while True:
    for i in range (500):
        for a in list:
            in1.value(a[0])
            in2.value(a[1])
            in3.value(a[2])
            in4.value(a[3])
            time.sleep_ms(0.05)
    for n in range (500):
        for b in list:
            in4.value(i[0])
            in3.value (i[1])
            in2.value(i[2])
            in1.value(i[3])
            time.sleep_ms(0.05)
      
