from machine import Pin
import time

IN1 = Pin((5),Pin.OUT)
IN2 = Pin((18),Pin.OUT)
IN3 = Pin((19),Pin.OUT)
IN4 = Pin((22),Pin.OUT)

list = [[1,0,0,0] ,[0,1,0,0],[0,0,1,0],[0,0,0,1]]

while True:
    for i in list:
        IN1= [i[0]]
        IN2= [i[1]]
        IN3= [i[2]]
        IN4= [i[3]]
        time.sleep_ms(5)
      
