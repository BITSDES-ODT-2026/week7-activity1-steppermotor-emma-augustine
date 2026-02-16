from machine import Pin
import time

IN1 = Pin((5),Pin.OUT)
IN2 = Pin((18),Pin.OUT)
IN3 = Pin((19),Pin.OUT)
IN3 = Pin((22),Pin.OUT)

#half step 

while True:
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)
    time.sleep(0.5)
    
    IN1.value(1)
    IN2.value(1)
    IN3.value(0)
    IN4.value(0)
    time.sleep(0.5)
    
    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(0)
    time.sleep(0.5)
    
    IN1.value(0)
    IN2.value(1)
    IN3.value(1)
    IN4.value(0)
    time.sleep(0.5)
    
    IN1.value(0)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)
    time.sleep(0.5)
    
    IN1.value(0)
    IN2.value(0)
    IN3.value(1)
    IN4.value(1)
    time.sleep(0.5)
    
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)
    time.sleep(0.5)
    

