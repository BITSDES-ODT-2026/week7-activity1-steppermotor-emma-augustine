from machine import Pin
import time

IN1 = Pin(5,Pin.OUT)
IN2 = Pin(18,Pin.OUT)
IN3 = Pin(19,Pin.OUT)
IN4 = Pin(22,Pin.OUT)

list = [[1,0,0,0] ,[0,1,0,0],[0,0,1,0],[0,0,0,1]]

while True:
    for i in list:
        IN1= [list[0]]
        IN2= [list[1]]
        IN3= [list[2]]
        IN4= [list[3]]
        time.sleep_ms(5)
