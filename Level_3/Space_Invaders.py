import pygame
import random
import time
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')
image1 = pygame.image.load ('Alien1.png')
image1 = pygame.transform.scale (image1,(20,20))
image2 = pygame.image.load ('Alien2.png')
image2 = pygame.transform.scale (image2,(20,20))
image3 = pygame.image.load ('Alien4.png')
image3 = pygame.transform.scale (image3,(20,20))

shipimage = pygame.image.load ('Ship.png')
shipimage = pygame.transform.scale (shipimage,(50,50))

projimage = pygame.image.load ('Laser.png')
projimage = pygame.transform.scale (projimage,(10,10))

lifeimage = pygame.image.load ('Life.png')
lifeimage = pygame.transform.scale (lifeimage,(30,30))

x = 60
x1 = 40
x2 = 60
outy = 50
outy1 = 100
outy2 = 150

class ship ():
    def __init__ (self,x,y,image):
        self.x = x
        self.y = y
        self.right = False
        self.left = False
        self.image = image
    def display (self):
        screen.blit (self.image,(self.x,self.y))
    def conditions (self):
        if self.right == True:
            self.x = self.x + 3
        if self.left == True:
            self.x = self.x - 3
    def text (self,msg,x1,y1,msgcol):
        fontobj = pygame.font.SysFont ('Times New Roman',20)
        msgobj = fontobj.render (msg,False,msgcol)
        screen.blit (msgobj,(x1,y1))

alienrow1 = []
alienrow2 = []
alienrow3 = []
spaceship = ship (265,550,shipimage)
laserlist = []

class alien ():
    def __init__ (self,x,y,image):
        self.x = x
        self.max = self.x + 5
        self.min = self.x - 5
        self.y = y
        self.image = image
        self.range = 0
        while self.range == 0:
            self.range = random.randint (-3,3)
    def display (self):
        screen.blit (self.image,(self.x,self.y))
    def vibrate (self):
        self.x = self.x - self.range
        if self.x >= self.max or self.x <= self.min:
            self.range = -self.range
    def text (self,msg,x1,y1,msgcol):
        fontobj = pygame.font.SysFont ('Times New Roman',30)
        msgobj = fontobj.render (msg,False,msgcol)
        screen.blit (msgobj,(x1,y1))

clock = pygame.time.Clock ()

for loop in range (1,11,1):
    a1 = alien (x,outy,image1)
    alienrow1.append (a1)
    x = x + 50
for loop in range (1,11,1):
    a1 = alien (x1,outy1,image2)
    alienrow2.append (a1)
    x1 = x1 + 50
for loop in range (1,11,1):
    a1 = alien (x2,outy2,image3)
    alienrow3.append (a1)
    x2 = x2 + 50

class laser ():
    def __init__ (self,x,y,image):
        self.x = x
        self.y = y
        self.image = image
    def display (self):
        screen.blit (self.image,(self.x,self.y))
    def text (self,msg,x1,y1,msgcol):
        fontobj = pygame.font.SysFont ('Times New Roman',30)
        msgobj = fontobj.render (msg,False,msgcol)
        screen.blit (msgobj,(x1,y1))

shots = 1
points = 0
lives = 3
alienmove = False
var1 = True
alienmove1,alienmove2,alienmove3 = False,False,False
alienmovev21,alienmovev22,alienmovev23 = False,False,False
amove = False

while var1 == True:
    screen.fill ((50,50,50))
    clock.tick (30)
    spaceship.display ()
    spaceship.conditions ()
    if lives == 3:
        screen.blit (lifeimage,(0,515))
        screen.blit (lifeimage,(35,515))
        screen.blit (lifeimage,(70,515))
    elif lives == 2:
        screen.blit (lifeimage,(0,515))
        screen.blit (lifeimage,(35,515))
    elif lives == 1:
        screen.blit (lifeimage,(0,515))
    elif lives == 0:
        spaceship.text ('Game Over!',240,300,(255,0,0))
        var1 = False

    spaceship.text ('Points: '+str(points),490,580,(0,255,255))

    for loop1 in alienrow1:
        loop1.vibrate ()
        loop1.display ()
    for loop2 in alienrow2:
        loop2.vibrate ()
        loop2.display ()
    for loop3 in alienrow3:
        loop3.vibrate ()
        loop3.display ()

    if shots % 6 == 0:
        shots = 1
        randomrow = random.randint (1,3)
        if randomrow == 1:
            randomalien = random.choice (alienrow1)
            ra1 = randomalien.y
            alienmove1 = True
        elif randomrow == 2:
            randomalien = random.choice (alienrow2)
            ra2 = randomalien.y
            alienmove1 = True
        elif randomrow == 3:
            randomalien = random.choice (alienrow3)
            ra3 = randomalien.y
            alienmove1 = True

    if alienmove1 == True:
        randomalien.y = randomalien.y + 1
    for outrandloop in alienrow1:
            if outrandloop.y != 50:
                outrandloop.y = outrandloop.y + 5
                if spaceship.x <= outrandloop.x <= spaceship.x + 50 and spaceship.y <= outrandloop.y <= spaceship.y + 50:
                    lives = lives - 1
                    alienrow1.remove (outrandloop)
                    break
                if outrandloop.y >= 620:
                    outrandloop.y = -20
                    #if outrandloop.y == ra1:
                        #break

    for outrandloop in alienrow2:
            if outrandloop.y != 100:
                outrandloop.y = outrandloop.y + 5
                if spaceship.x <= outrandloop.x <= spaceship.x + 50 and spaceship.y <= outrandloop.y <= spaceship.y + 50:
                    lives = lives - 1
                    alienrow2.remove (outrandloop)
                    break
                if outrandloop.y >= 620:
                    outrandloop.y = -20
                    #if outrandloop.y == ra2:
                        #break

    for outrandloop in alienrow3:
            if outrandloop.y != 150:
                outrandloop.y = outrandloop.y + 5
                if spaceship.x <= outrandloop.x <= spaceship.x + 50 and spaceship.y <= outrandloop.y <= spaceship.y + 50:
                    lives = lives - 1
                    alienrow3.remove (outrandloop)
                    break
                if outrandloop.y >= 620:
                    outrandloop.y = -20
                    #if outrandloop.y == ra3:
                        #break

    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT and spaceship.left == False:
                spaceship.right = True
                spaceship.left = False
            if event.key == K_LEFT and spaceship.right == False:
                spaceship.left = True
                spaceship.right = False
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                spaceship.right = False
                spaceship.left = False
            if event.key == K_LEFT:
                spaceship.left = False
                spaceship.right = False
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            (clickx,clicky) = event.pos
            amove = True
        if event.type == MOUSEBUTTONUP and event.button == 1:
            amove = False
    if amove == True:
        shots = shots + 1
        if shots % 5 == 0:
            laserlist.append (laser (spaceship.x + 20,spaceship.y,projimage))
    if amove == False:
        alienmove1 = False
    for loop4 in laserlist:
        loop4.y = loop4.y - 5
        loop4.display ()
        if loop4.y >= 620:
            laserlist.remove (loop4)
        for hitloop in alienrow1:
            if hitloop.x <= loop4.x <= hitloop.x + 20 and hitloop.y <= loop4.y <= hitloop.y + 20:
                laserlist.remove (loop4)
                alienrow1.remove (hitloop)
                points = points + 1
        for hitloop in alienrow2:
            if hitloop.x <= loop4.x <= hitloop.x + 20 and hitloop.y <= loop4.y <= hitloop.y + 20:
                laserlist.remove (loop4)
                alienrow2.remove (hitloop)
                points = points + 1
        for hitloop in alienrow3:
            if hitloop.x <= loop4.x <= hitloop.x + 20 and hitloop.y <= loop4.y <= hitloop.y + 20:
                laserlist.remove (loop4)
                alienrow3.remove (hitloop)
                points = points + 1
    pygame.display.update ()
