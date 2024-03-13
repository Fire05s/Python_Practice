import pygame
import random
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')
def ponggm ():
    clock = pygame.time.Clock ()
    x = 25
    x1 = 550
    y = 200
    y1 = 200
    bx = 300
    by = 300
    keypress = False
    keypress1 = False
    keypress2 = False
    keypress3 = False
    bmove = 10
    bmove1 = 10
    p1 = 0
    p2 = 0
    def text (msg,x1,y1,msgcol):
        fontobj = pygame.font.SysFont ('Times New Roman',20)
        msgobj = fontobj.render (msg,False,msgcol)
        screen.blit (msgobj,(x1,y1))
    while True:
        screen.fill ((0,0,0))
        clock.tick (30)
    #    screen.fill ((0,0,0))
        pygame.draw.rect (screen,(255,255,255),(x,y,25,100))
        pygame.draw.rect (screen,(255,255,255),(x1,y1,25,100))
        pygame.draw.circle (screen,(255,255,255),(bx,by),20)
        bx = bx + bmove
        by = by + bmove1
        for event in pygame.event.get ():
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    keypress = True
                if event.key == K_s:
                    keypress1 = True
                if event.key == K_UP:
                    keypress2 = True
                if event.key == K_DOWN:
                    keypress3 = True
            if event.type == pygame.KEYUP:
                if event.key == K_w:
                    keypress = False
                if event.key == K_s:
                    keypress1 = False
                if event.key == K_UP:
                    keypress2 = False
                if event.key == K_DOWN:
                    keypress3 = False
            if event.type == QUIT:
                pygame.quit ()
                exit ()
        if keypress == True:
            y = y - 10
        if keypress1 == True:
            y = y + 10
        if keypress2 == True:
            y1 = y1 - 10
        if keypress3 == True:
            y1 = y1 + 10
        if y <= 0:
            y = 0
        if y >= 500:
            y = 500
        if y1 <= 0:
            y1 = 0
        if y1 >= 500:
            y1 = 500
        if bx == 580:
            bx = 300
            by = 300
            p1 = p1 + 1
            print ('Hit right side')
        if bx == 20:
            bx = 300
            by = 300
            p2 = p2 + 1
            print ('Hit left side')
        if by <= 20:
            bmove1 = -1 * bmove1
            print ('Bounced off top')
        if by >= 580:
            bmove1 = -1 * bmove1
            print ('Bounced off bottom')
        if bx >= x1 - 20 and y1 - 25 <= by <= y1 + 125:
            bmove = -1 * bmove
            print ('Pong')
        if x <= bx - 20 <= x + 20 and y - 25 < by < y + 125:
            bmove = -1 * bmove
            print ('Ping')
        text ('Player 1: '+str(p1),90,25,(255,255,255))
        text ('Player 2: '+str(p2),450,25,(255,255,255))
        if p1 == 5:
            text ('Player 1 Wins!',300,250,(0,255,0))
            pygame.display.update ()
            break
        elif p2 == 5:
            text ('Player 2 Wins!',300,250,(0,255,0))
            pygame.display.update ()
            break
        pygame.display.update ()
