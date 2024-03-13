import pygame
import random
from Tic_Tac_Toe_Function import *
from Pong_Function import *
from Flappy_Bird_Function import *
from Snake_Function import *
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
    pygame.draw.rect (screen,(255,255,255),(50,100,200,100))
    text ('Tic-Tac-Toe',110,125,(0,0,0))
    pygame.draw.rect (screen,(0,0,255),(350,100,200,100))
    text ('Pong',380,125,(0,0,0))
    pygame.draw.rect (screen,(255,255,0),(50,400,200,100))
    text ('Flappy Bird',110,425,(0,0,0))
    pygame.draw.rect (screen,(0,255,0),(350,400,200,100))
    text ('Snake',380,425,(0,0,0))
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            (clickx,clicky) = event.pos
    if 50 <= clickx <= 250 and 100 <= clicky <= 200:
        screen.fill ((0,0,0))
        tic_tac ()
        pygame.display.update ()
        break
    elif 350 <= clickx <= 550 and 100 <= clicky <= 200:
        screen.fill ((0,0,0))
        ponggm ()
        pygame.display.update ()
        break
    elif 50 <= clickx <= 250 and 400 <= clicky <= 500:
        screen.fill ((0,0,0))
        game ()
        pygame.display.update ()
        break
    elif 350 <= clickx <= 550 and 400 <= clicky <= 500:
        screen.fill ((0,0,0))
        snakegm ()
        pygame.display.update ()
        break
    pygame.display.update ()
