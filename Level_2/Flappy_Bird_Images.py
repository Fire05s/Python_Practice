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
birdx = 85
birdy = 285
pipex = 550
pipey = 0
pipel = random.randint (0,450)
pipew = 50
Bpipey = pipel + space
Bpipel = 600 - Bpipey
birdmove = False
pipemove = True
score = 0  
birdup = pygame.image.load ('Flappy_Bird_Up.png')
pipeimg = pygame.image.load ('Flappy_Bird_Pipe.png')
pipeflipped = pygame.image.load ('Flappy_Bird_Pipe_Flip.png')
background = pygame.image.load ('Flappy_Bird_Background.png')
birdup = pygame.transform.scale (birdup,(30,30))
pipeimg = pygame.transform.scale (pipeimg,(50,pipel))
pipeflipped = pygame.transform.scale (pipeflipped,(50,Bpipel))
background = pygame.transform.scale (background,(600,600))
screen.blit (birdup,(birdx,birdy))
pygame.display.update ()
while True:
    screen.fill ((0,0,0))
    screen.blit (background,(0,0))
    clock.tick (60)
    showbird = screen.blit (birdup,(birdx,birdy))
    showtpipe = screen.blit (pipeimg,(pipex,pipey))
    showbpipe = screen.blit (pipeflipped,(pipex,Bpipey))
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
        birdy = birdy - 5
    else:
        birdy = birdy + 5
    if pipemove == True:
        pipex = pipex - 10
    if pipex <= 0:
        pipex = 550
        pipel = random.randint (0,450)
        Bpipey = pipel + space
        Bpipel = 600 - Bpipey
        score = score + 1
    if score == 10:
        text ('You Win!',250,100,(0,255,0))
        pygame.display.update ()
    text ('Points: '+str(score),275,50,(255,255,255))
##        if showbird.colliderect (showtpipe) or showbird.colliderect (showbpipe):
##            text ('Game Over!',250,100,(255,0,0))
##            pygame.display.update ()
##            break
    pygame.display.update ()
