#Libraries
import RPi.GPIO as GPIO
import time
from firebase import firebase
import datetime
import os

os.system('fswebcam /home/pi/security5.png')
os.system('sshpass -p qdI1YO4D scp -r /home/pi/security5.png root@51.38.188.239:/root/')

firebase = firebase.FirebaseApplication('https://raspberrypi-9bcd7.firebaseio.com/', None)
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
	    if dist<=25:
               os.system('fswebcam /home/pi/security5.png')
               os.system('sshpass -p qdI1YO4D scp -r /home/pi/security5.png root@51.38.188.239:/root/') 
               date = datetime.datetime.now()	
               times =str(date)		
	       data = {"date": times}
	       firebase.put('/aymen/',"person", data)
		
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

