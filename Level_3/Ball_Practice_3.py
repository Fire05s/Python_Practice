import pygame
import random
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')
def text (msg,x1,y1,msgcol):
    fontobj = pygame.font.SysFont ('Times New Roman',30)
    msgobj = fontobj.render (msg,False,msgcol)
    screen.blit (msgobj,(x1,y1))

##class ball:
##    def __init__ (self,num):
##        self.n = num
##        if self.n % 2 == 1:
##            self.color = (255,0,0)
##        else:
##            self.color = (0,0,255)
##        self.r = 10
##        self.x = random.randint (0,600)
##        self.y = random.randint (0,600)
##        self.movex = 5
##        self.movey = 5
##    def display (self):
##        pygame.draw.circle (screen,(self.color),(self.x,self.y),self.r)
##        if self.color == (255,0,0):
##            self.x = self.x + self.movex
##        else:
##            self.y = self.y + self.movey
##        if self.x >= 600 or self.x <= 0:
##            self.movex = -self.movex
##        if self.y >= 600 or self.y <= 0:
##            self.movey = -self.movey
##blist = []
##for loop in range (1,21,1):
##    blist.append (ball (loop))
##clock = pygame.time.Clock ()

class ball:
    def __init__ (self,num):
        self.n = random.randint (1,2)
        self.col1 = (255,0,0)
        self.col2 = (0,0,255)
        self.r = 10
        self.x = random.randint (0,600)
        self.y = random.randint (0,600)
        self.movey = 5
    def display (self):
        pygame.draw.circle (screen,(self.col1),(self.x,self.y),self.r)
        if self.n == 1:
            self.col1 = self.col2
        else:
            self.col2 = self.col1
        #self.col1,self.col2 = self.col2,self.col1
        self.y = self.y + self.movey
        if self.y >= 600 or self.y <= 0:
            self.movey = -self.movey
blist = []
for loop in range (1,21,1):
    blist.append (ball (loop))
clock = pygame.time.Clock ()

while True:

    screen.fill ((0,0,0))
    clock.tick (60)
    for loop in range (0,20,1):
        blist [loop].display ()
    for loop in blist:
        loop.col1,loop.col2 = loop.col2,loop.col1
        
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
    pygame.display.update ()
