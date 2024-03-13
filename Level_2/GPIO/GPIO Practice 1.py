import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BCM)

##GPIO.setup (2,GPIO.OUT)
##GPIO.output (2,GPIO.HIGH)
##print ('ON')
##time.sleep (3)
##GPIO.output (2,GPIO.LOW)
##print ('OFF')

##GPIO.setup (2,GPIO.OUT)
##for loop in range (0,3,1):
##    GPIO.output (2,GPIO.HIGH)
##    print ('on')
##    time.sleep (1)
##    GPIO.output (2,GPIO.LOW)
##    print ('off')
##    time.sleep (1)

##GPIO.setup (2,GPIO.OUT)
##GPIO.setup (3,GPIO.OUT)
##t = 0.5
##tchange = 0.5
##while True:
##    GPIO.output (2,GPIO.HIGH)
##    GPIO.output (3,GPIO.HIGH)
##    print ('on',t)
##    time.sleep (t)
##    GPIO.output (2,GPIO.LOW)
##    GPIO.output (3,GPIO.LOW)
##    print ('off',t)
##    time.sleep (t)
##    t = t + tchange
##    if t == 2.5 or t == 0:
##        t = t - 2 * tchange
##        tchange = -tchange

##GPIO.setup (2,GPIO.OUT)
##GPIO.setup (3,GPIO.OUT)
##while True:
##    GPIO.output (2,GPIO.HIGH)
##    print ('on 2')
##    GPIO.output (3,GPIO.HIGH)
##    print ('on 3')
##    time.sleep (3)
##    GPIO.output (2,GPIO.LOW)
##    print ('off 2')
##    GPIO.output (3,GPIO.LOW)
##    print ('off 3')
##    time.sleep (3)



GPIO.cleanup ()
