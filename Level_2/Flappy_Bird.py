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
clock = pygame.time.Clock ()
space = 100
birdx = 100
birdy = 300
pipex = 550
pipey = 0
pipel = random.randint (0,450)
pipew = 50
Bpipey = pipel + space
Bpipel = pipel + 600
birdmove = False
pipemove = True
score = 0
while True:
    screen.fill ((0,0,0))
    clock.tick (300)
    pygame.draw.circle (screen,(255,255,0),(birdx,birdy),25)
    pygame.draw.rect (screen,(0,255,0),(pipex,pipey,pipew,pipel))
    pygame.draw.rect (screen,(0,255,0),(pipex,Bpipey,pipew,Bpipel))
    for event in pygame.event.get ():
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                birdmove = True
        if event.type == pygame.KEYUP:
            if event.key == K_SPACE:
                birdmove = False
        if event.type == QUIT:
            pygame.quit ()
            exit ()
    if birdmove == True:
        birdy = birdy - 1
    else:
        birdy = birdy + 1
    if pipemove == True:
        pipex = pipex - 1
    if pipex <= 0:
        pipex = 550
        pipel = random.randint (0,450)
        Bpipey = pipel + space
        score = score + 1
    if score == 10:
        text ('You Win!',250,100,(0,255,0))
        pygame.display.update ()
    text ('Points: '+str(score),275,50,(255,255,255))
    pygame.display.update ()
    if birdy <= 25:
        text ('Game Over...',230,100,(255,0,0))
        pygame.display.update ()
        print ('Game Over...')
        break
    if birdy >= 575:
        text ('Game Over...',230,100,(255,0,0))
        pygame.display.update ()
        print ('Game Over...')
        break
    if birdx + 25 >= pipex and pipey <= birdy <= pipey + pipel:
        text ('Game Over...',230,100,(255,0,0))
        pygame.display.update ()
        print ('Game Over...')
        break
    if birdx + 25 >= pipex and Bpipey <= birdy <= Bpipey + Bpipel:
        text ('Game Over...',230,100,(255,0,0))
        pygame.display.update ()
        print ('Game Over...')
        break
    if pipex <= birdx + 25 <= pipex + pipew and pipey <= birdy - 25 <= pipey + pipel:
        text ('Game Over...',230,100,(255,0,0))
        pygame.display.update ()
        print ('Game Over...')
        break
    if pipex <= birdx - 25 <= pipex + pipew and pipey <= birdy - 25 <= pipey + pipel:
        text ('Game Over...',230,100,(255,0,0))
        pygame.display.update ()
        print ('Game Over...')
        break
    if pipex <= birdx + 25 <= pipex + pipew and Bpipey <= birdy - 25 <= Bpipey + Bpipel:
        text ('Game Over...',230,100,(255,0,0))
        pygame.display.update ()
        print ('Game Over...')
        break
    if pipex <= birdx - 25 <= pipex + pipew and Bpipey <= birdy - 25 <= Bpipey + Bpipel:
        text ('Game Over...',230,100,(255,0,0))
        pygame.display.update ()
        print ('Game Over...')
        break
    pygame.display.update ()
