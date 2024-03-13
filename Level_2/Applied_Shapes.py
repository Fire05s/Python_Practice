import pygame
import random
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')
var1 = 10
var2 = -10
white = (255,255,255)
col1 = (255,0,0)
col2 = (0,255,0)
col3 = (0,0,255)
col4 = (255,255,0)
list1 = [col1,col3]
x = 0
y = 0
x1 = 600
y1 = 0
r = 10
clock = pygame.time.Clock ()
##hwx = 0
##hwy = 100
##hwmovement = 10

var3 = 100
list2 = []
for loop in range (0,100,1):
    x = random.randint (0,600)
    y = random.randint (0,600)
    list2.append ([x,y])

while True:
    screen.fill ((0,0,0))
##    pygame.draw.rect (screen,(white),(x,y,50,50))
##    clock.tick (50)
##    x = x + var1
##    if x == 600 and y == 600:
##        x = 0
##        y = 0
##        white = random.choice (list1)
##    elif x == 600:
##        x = 0
##        y = y + var2
##        white = random.choice (list1)

##    pygame.draw.rect (screen,(white),(x,y,50,50))
##    pygame.draw.rect (screen,(white),(x1,y1,50,50))
##    clock.tick (20)
##    x = x + var1
##    y = y + var1
##    x1 = x1 - var1
##    y1 = y1 + var1
##    white = random.choice (list1)
##    if x == 600 and y == 600:
##        x = 0
##        y = 0
##    if x1 == 0 and y1 == 600:
##        x1 = 600
##        y1 = 0

##    pygame.draw.circle (screen,(white),(300,300),r)
##    clock.tick (20)
##    r = r + var1
##    if r == 300:
##        var1 = -10
##        white = random.choice (list1)
##    if r == 10:
##        var1 = 10

##                                      HW

##    pygame.draw.rect (screen,(255,255,255),(hwx,hwy,300,150))
##    pygame.draw.circle (screen,(255,255,255),(hwx+70,280),50)
##    pygame.draw.circle (screen,(255,255,255),(hwx+230,280),50)
##    clock.tick (20)
##    hwx = hwx + hwmovement
##    if hwx == 300:
##        hwmovement = -10
##    if hwx == 0:
##        hwmovement = 10

##

##    for loop in range (0,600,100):
##        pygame.draw.rect (screen,(col1),(loop,0,100,100))
##        clock.tick (60)
##        col1,col3 = col3,col1

##    pygame.draw.circle (screen,(255,255,255),(x,300),50)
##    pygame.draw.circle (screen,(255,255,0),(x1,300),50)
##    clock.tick (20)
##    x = x + var1
##    x1 = x1 - var1
##    if x + 50 == x1 - 50:
##        var1 = -10
##    if x - 50 == 0:
##        var1 = 10

    for loop1 in list2:
        pygame.draw.circle (screen,(white),(loop1[0],loop1[1]),3)
        loop1[1] = loop1[1] + 10
        white,col4 = col4,white
        if loop1[1] >= 600:
            loop1[1] = 0
    clock.tick (40)
    white,col4 = col4,white
    
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
    pygame.display.update ()
