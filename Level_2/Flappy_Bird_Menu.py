import pygame
import random
from Flappy_Bird_Function import *
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')
def text (msg,x1,y1,msgcol):
    fontobj = pygame.font.SysFont ('Times New Roman',30)
    msgobj = fontobj.render (msg,False,msgcol)
    screen.blit (msgobj,(x1,y1))
clickx = 0
clicky = 0
while True:
    text ('Flappy Bird',250,50,(255,255,255))
    pygame.draw.rect (screen,(0,255,0),(100,300,200,100))
    text ('Play',175,325,(255,255,255))
    pygame.draw.rect (screen,(255,0,0),(350,300,200,100))
    text ('Quit',425,325,(255,255,255))
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
        if event.type == MOUSEBUTTONDOWN:
            (clickx,clicky) = event.pos
    if 350 <= clickx <= 550 and 300 <= clicky <= 400:
        pygame.quit ()
        exit ()
    if 100 <= clickx <= 300 and 300 <= clicky <= 400:
        game ()
        break
    pygame.display.update ()
