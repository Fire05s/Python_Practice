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
class ball:
    def __init__ (self):
        self.size = random.randint (5,15)
        self.red = random.randint (0,255)
        self.green = random.randint (0,255)
        self.blue = random.randint (0,255)
        self.color = ((self.red,self.green,self.blue))
        self.x = random.randint (0,600)
        self.y = random.randint (0,600)
        self.speed = random.randint (1,5)
    def update (self):
        pygame.draw.circle (screen,(self.color),(self.x,self.y),self.size)
        self.x = self.x + self.speed
        if self.x >= 600:
            self.speed = -self.speed
        if self.x <= 0:
            self.speed = -self.speed

ballist = []
for loop in range (0,10,1):
    loopball = ball ()
    ballist.append (loopball)
clock = pygame.time.Clock ()
while True:
    screen.fill ((0,0,0))
    clock.tick (60)
    for loop in range (0,10,1):
        loopball = ballist [loop]
        loopball.update ()
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
    pygame.display.update ()
