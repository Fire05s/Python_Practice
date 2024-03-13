import pygame
import random
pygame.init ()
from pygame.locals import *

image1 = pygame.image.load ('Alien1.png')
image1 = pygame.transform.scale (image1,(20,20))
i1_rect = pygame.Rect (150,300,20,20) #can use i1.colliderect (i2)
image2 = pygame.image.load ('Alien2.png')
image2 = pygame.transform.scale (image2,(20,20))
projimage = pygame.image.load ('Laser.png')
projimage = pygame.transform.scale (projimage,(10,10))

screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')
def text (msg,x1,y1,msgcol):
    fontobj = pygame.font.SysFont ('Times New Roman',30)
    msgobj = fontobj.render (msg,False,msgcol)
    screen.blit (msgobj,(x1,y1))

l1 = [image1,image1,image1]
laslist = []
for loop in range (30):
    laslist.append (projimage)
ax = 150
ay = 200
lx = 150
ly = 300
for loop in l1:
    screen.blit (loop,(ax,ay))
    ax += 50
for loop in laslist:
    screen.blit (loop,(lx,ly))
    lx += 10
while True:
    screen.fill ((0,0,0))
    ax = 150
    lx = 150
    for loop in l1:
        screen.blit (loop,(ax,ay))
        ax += 50
    for loop in laslist:
        screen.blit (loop,(lx,ly))
        lx += 10
    for loop in laslist:
        ly -= 1
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
    pygame.display.update ()
