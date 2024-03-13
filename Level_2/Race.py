import pygame
import random
import time
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')
def text (msg,x1,y1,msgcol):
    fontobj = pygame.font.SysFont ('Times New Roman',20)
    msgobj = fontobj.render (msg,False,msgcol)
    screen.blit (msgobj,(x1,y1))
road = pygame.image.load ('Road.png')
road = pygame.transform.scale (road,(600,600))
redc = pygame.image.load ('RCar.png')
redc = pygame.transform.scale (redc,(200,100))
grnc = pygame.image.load ('GCar.png')
grnc = pygame.transform.scale (grnc,(200,100))
ornc = pygame.image.load ('OCar.png')
ornc = pygame.transform.scale (ornc,(200,100))
screen.blit (road,(0,0))
screen.blit (redc,(0,120))
screen.blit (grnc,(0,250))
screen.blit (ornc,(0,380))
text ('-- This is your car.',250,300,(255,255,255))
pygame.display.update ()
time.sleep (2)
screen.blit (road,(0,0))
screen.blit (redc,(0,120))
screen.blit (grnc,(0,250))
screen.blit (ornc,(0,380))
text ('Use the Arrow Keys to move your car.',250,300,(255,255,255))
pygame.display.update ()
time.sleep (3)
rx = 0
gx = 0
ox = 0
ry = 120
gy = 250
oy = 380
rchange = random.randint (1,7)
gchange = random.randint (1,7)
ochange = random.randint (1,7)
points = 0
rpoints = 0
opoints = 0
gupmove = False
gdownmove = False
gleftmove = False
grightmove = False
while True:
    screen.blit (road,(0,0))
    redcar = screen.blit (redc,(rx,ry))
    grncar = screen.blit (grnc,(gx,gy))
    orncar = screen.blit (ornc,(ox,oy))
    text ('Player\'s Points: '+str(points),250,20,(255,255,255))
    text ('Red\s Points: '+str(rpoints),20,20,(255,0,0))
    text ('Orange\s Points: '+str(opoints),450,20,(255,190,0))
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                gupmove = True
                gdownmove = False
            if event.key == K_DOWN:
                gdownmove = True
                gupmove = False
            if event.key == K_LEFT and grightmove != True:
                gleftmove = True
                grightmove = False
                gupmove = False
                gdownmove = False
            if event.key == K_RIGHT and gleftmove != True:
                grightmove = True
                gleftmove = False
                gupmove = False
                gdownmove = False
    rx = rx + rchange
    ox = ox + ochange
    if gupmove == True:
        gy = gy - gchange*0.6
    if gdownmove == True:
        gy = gy + gchange*0.6
    if gleftmove == True:
        gx = gx - gchange*0.1
    if grightmove == True:
        gx = gx + gchange*0.9
    if gx + 200 >= 600:
        points = points + 1
        gx = 0
        gy = 250
        gchange = random.randint (1,7)
    if rx + 200 >= 600:
        rpoints = rpoints + 1
        rx = 0
        ry = 120
        rchange = random.randint (1,7)
    if ox + 200 >= 600:
        opoints = opoints + 1
        ox = 0
        oy = 380
        ochange = random.randint (1,7)
    if gy + 100 >= 600:
        gy = 500
    if gy >= 600:
        gy = 0
    if grncar.colliderect (redcar):
        gx = 0
        gy = 250
        rx = 0
        ry = 120
        gupmove = False
        gchange = random.randint (1,7)
        rchange = random.randint (1,7)
        points = points - 1
        rpoints = points - 1
        if points <= 0:
            points = 0
        if rpoints <= 0:
            rpoints = 0
        screen.fill ((0,0,0))
        screen.blit (road,(0,0))
        screen.blit (redc,(rx,ry))
        screen.blit (grnc,(gx,gy))
        screen.blit (ornc,(ox,oy))
        text ('Player\'s Points: '+str(points),250,20,(255,255,255))
        text ('Red\s Points: '+str(rpoints),20,20,(255,0,0))
        text ('Orange\s Points: '+str(opoints),450,20,(255,190,0))
        pygame.display.update ()
    if grncar.colliderect (orncar):
        gx = 0
        gy = 250
        ox = 0
        oy = 380
        gdownmove = False
        gchange = random.randint (1,7)
        ochange = random.randint (1,7)
        points = points - 1
        opoints = points - 1
        if points <= 0:
            points = 0
        if opoints <= 0:
            opoints = 0
        screen.fill ((0,0,0))
        screen.blit (road,(0,0))
        screen.blit (redc,(rx,ry))
        screen.blit (grnc,(gx,gy))
        screen.blit (ornc,(ox,oy))
        text ('Player\'s Points: '+str(points),250,20,(255,255,255))
        text ('Red\s Points: '+str(rpoints),20,20,(255,0,0))
        text ('Orange\s Points: '+str(opoints),450,20,(255,190,0))
        pygame.display.update ()
    if points == 10:
        screen.fill ((0,0,0))
        screen.blit (road,(0,0))
        screen.blit (redc,(rx,ry))
        screen.blit (grnc,(gx,gy))
        screen.blit (ornc,(ox,oy))
        text ('Player\'s Points: '+str(points),250,20,(255,255,255))
        text ('Red\s Points: '+str(rpoints),20,20,(255,0,0))
        text ('Orange\s Points: '+str(opoints),450,20,(255,190,0))
        text ('Player Wins!',250,50,(0,255,0))
        pygame.display.update ()
        break
    if rpoints == 10:
        screen.fill ((0,0,0))
        screen.blit (road,(0,0))
        screen.blit (redc,(rx,ry))
        screen.blit (grnc,(gx,gy))
        screen.blit (ornc,(ox,oy))
        text ('Player\'s Points: '+str(points),250,20,(255,255,255))
        text ('Red\s Points: '+str(rpoints),20,20,(255,0,0))
        text ('Orange\s Points: '+str(opoints),450,20,(255,190,0))
        text ('Red Wins!',250,50,(255,0,0))
        pygame.display.update ()
        break
    if opoints == 10:
        screen.fill ((0,0,0))
        screen.blit (road,(0,0))
        screen.blit (redc,(rx,ry))
        screen.blit (grnc,(gx,gy))
        screen.blit (ornc,(ox,oy))
        text ('Player\'s Points: '+str(points),250,20,(255,255,255))
        text ('Red\s Points: '+str(rpoints),20,20,(255,0,0))
        text ('Orange\s Points: '+str(opoints),450,20,(255,190,0))
        text ('Orange Wins!',250,50,(255,190,0))
        pygame.display.update ()
        break
    pygame.display.update ()
