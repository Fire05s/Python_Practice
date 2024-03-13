import pygame
import random,time

#import

pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')
def text (msg,x1,y1,msgcol):
    fontobj = pygame.font.SysFont ('Times New Roman',30)
    msgobj = fontobj.render (msg,False,msgcol)
    screen.blit (msgobj,(x1,y1))
white = (255,255,255)
black = (0,0,0)
gray = (50,50,50)
sun = pygame.image.load ('sun.png')
sun = pygame.transform.scale (sun,(50,50))
idlechar = pygame.image.load ('idlechar.png')
idlechar = pygame.transform.scale (idlechar,(480,236))
rightwalklist = []
for loop in range (1,11,1):
    img = pygame.image.load ('Walk ('+str(loop)+').png')
    img = pygame.transform.scale (img,(480,236))
    rightwalklist.append (img)
leftwalklist = []
for loop in range (1,11,1):
    img = pygame.image.load ('Walk ('+str(loop)+').png')
    img = pygame.transform.scale (img,(480,236))
    img = pygame.transform.flip (img,True,False)
    leftwalklist.append (img)
def background ():
    screen.fill (white)
    pygame.draw.rect (screen,gray,(100,100,200,200),3)
    pygame.draw.circle (screen,gray,(150,200),15,3)
    pygame.draw.line (screen,gray,(150,185),(150,215),3)
    pygame.draw.polygon (screen,gray,((100,100),(200,0),(300,100)),3)
    screen.blit (sun,(50,50))
def motorb ():
    pygame.draw.rect (screen,gray,(400,100,100,20),3)
    text ('Motor On',435,103,gray)
    pygame.draw.rect (screen,gray,(400,150,100,20),3)
    text ('Motor Off',435,153,gray)

#changef,stop

xpos = 150
ypos = 300
mx = 0
my = 0
screen.blit (idlechar,(xpos,ypos))
pygame.display.update ()
time.sleep (0.1)
GPIO.setup (17,GPIO.OUT)
GPIO.output (17,GPIO.LOW)
while True:
    background ()
    screen.blit (idlechar,(xpos,ypos))
    motorb ()
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print ('right arrow pressed')
                for loop1 in rightwalklist:
                    background ()
                    screen.blit (loop1,(xpos,ypos))
                    pygame.display.update ()
                    time.sleep (0.5)
                    xpos = xpos + 10
            if event.key == pygame.K_LEFT:
                print ('left arrow pressed')
                for loop2 in leftwalklist:
                    background ()
                    screen.blit (loop2,(xpos,ypos))
                    pygame.display.update ()
                    time.sleep (0.5)
                    xpos = xpos - 10
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mx,my) = (event.pos)
            if event.button == 1:
                if 400 <= mx <= 500 and 100 <= my <= 120:
                    moton ():
                if 400 <= mx <= 500 and 150 <= my <= 170:
                    motoff ()
    if xpos == 200:
        GPIO.output (17,GPIO.HIGH)
    
    pygame.display.update ()
