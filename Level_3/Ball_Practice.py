import random
import pygame
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
        self.colorchoice = random.randint (1,2)
        if self.colorchoice == 1:
            self.color = (255,0,0)
        else:
            self.color = (0,0,255)
        self.x = random.randint (0,600)
        self.y = random.randint (0,600)
        self.radius = random.randint (5,10)
        self.move = random.randint (1,5)
    def movement (self):
        if self.color == ((255,0,0)):
            self.x = self.x + self.move
        else:
            self.y = self.y + self.move
        if self.x >= 600 or self.x <= 0:
            self.move = -self.move
        elif self.y >= 600 or self.y <= 0:
            self.move = -self.move
    def draw (self):
        pygame.draw.circle (screen,self.color,(self.x,self.y),self.radius)

ballist = []
for loop in range (0,50,1):
    loopball = ball ()
    ballist.append (loopball)
clock = pygame.time.Clock ()
while True:
    screen.fill ((0,0,0))
    clock.tick (30)
    for loop in range (0,50,1):
        loopball = ballist [loop]
        loopball.movement ()
        loopball.draw ()
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
    pygame.display.update ()
