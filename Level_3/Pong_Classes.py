import pygame
import random
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')
class paddle:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        self.length = 100
        self.width = 25
        self.up = False
        self.down = False
        self.score = 0
    def draw (self):
        pygame.draw.rect (screen,(255,255,255),(self.x,self.y,self.width,self.length))
    def move (self):
        if self.up == True:
            self.y = self.y - 10
        elif self.down == True:
            self.y = self.y + 10
        if self.y >= 500:
            self.y = 500
        if self.y <= 0:
            self.y = 0
    #def win (self):
        
    def text (self,msg,x1,y1,msgcol):
        fontobj = pygame.font.SysFont ('Times New Roman',20)
        msgobj = fontobj.render (msg,False,msgcol)
        screen.blit (msgobj,(x1,y1))
    def points (self):
        if ball1.x >= 580:
            lpad.score = lpad.score + 1
            ball1.x = 300
            ball1.y = 300
            ball1.movey = -1 * ball1.movey
        if ball1.x <= 20:
            rpad.score = rpad.score + 1
            ball1.x = 300
            ball1.y = 300
            ball1.movey = -1 * ball1.movey
    
class ball:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        self.r = 20
        self.movex = 10
        self.movey = 10
    def draw (self):
        pygame.draw.circle (screen,(255,255,255),(self.x,self.y),self.r)
    def move (self):
        self.x = self.x + self.movex
        self.y = self.y + self.movey
        if self.y >= 580:
            self.movey = -1 * self.movey
        if self.y <= 20:
            self.movey = -1 * self.movey
    def collision (self):
        if lpad.y - 20 <= self.y - 20 <= lpad.y + 120 and lpad.x <= self.x - 20 <= lpad.x + 25:
            self.movex = -1 * self.movex
        if rpad.y - 20 <= self.y + 20 <= rpad.y + 120 and rpad.x <= self.x + 20 <= rpad.x + 25:
            self.movex = -1 * self.movex
clock = pygame.time.Clock ()
    
lpad = paddle (50,250)
rpad = paddle (525,250)
ball1 = ball (300,300)
while True:
    screen.fill ((0,0,0))
    clock.tick (30)
    lpad.draw ()
    rpad.draw ()
    ball1.draw ()
    lpad.points ()
    rpad.points ()
    ball1.collision ()
    lpad.text ('P1\'s Score:',100,25,(255,0,0))
    lpad.text (str(lpad.score),140,50,(255,0,0))
    rpad.text ('P2\'s Score:',400,25,(0,0,255))
    rpad.text (str(rpad.score),440,50,(0,0,255))
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
        if event.type == KEYDOWN:
            if event.key == K_w:
                lpad.up = True
            if event.key == K_s:
                lpad.down = True
            if event.key == K_UP:
                rpad.up = True
            if event.key == K_DOWN:
                rpad.down = True
        if event.type == KEYUP:
            if event.key == K_w:
                lpad.up = False
            if event.key == K_s:
                lpad.down = False
            if event.key == K_UP:
                rpad.up = False
            if event.key == K_DOWN:
                rpad.down = False
    lpad.move ()
    rpad.move ()
    ball1.move ()
    if lpad.score == 10:
        lpad.text ('Player 1 Wins!',250,100,(255,255,0))
        pygame.display.update ()
        break
    if rpad.score == 10:
        rpad.text ('Player 2 Wins!',250,100,(255,255,0))
        pygame.display.update ()
        break
    pygame.display.update ()
