import RPi.GPIO as GPIO

#setmode in funct on and off
#setup in off
#move cathode from 3.3 V to gnd

r = 5
g = 6
b = 13
GPIO.setmode (GPIO.BCM)
def on (num):
    GPIO.setup (num,GPIO.OUT)
    GPIO.output (num,GPIO.HIGH)
def off (num):
    GPIO.setup (num,GPIO.OUT)
    GPIO.output (num,GPIO.LOW)
def redon ():
    on (r)
def redoff ():
    off (r)
def grnon ():
    on (g)
def grnoff ():
    off (g)
def blueon ():
    on (b)
def blueoff ():
    off (b)
def main ():
    while True:
        col = input ('Choose a color from red, green, and blue, a space, and whether it should be on/off - ')
        if col == 'red on':
            redon ()
        if col == 'green on':
            grnon ()
        if col == 'blue on':
            blueon ()
        if col == 'red off':
            redoff ()
        if col == 'green off':
            grnoff ()
        if col == 'blue off':
            blueoff ()
    return
main ()
