import pygame
import random
import time
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')
def text (msg,x1,y1,msgcol):
    fontobj = pygame.font.SysFont ('Times New Roman',30)
    msgobj = fontobj.render (msg,False,msgcol)
    screen.blit (msgobj,(x1,y1))
circle = pygame.image.load ('Tic-Tac-Toe_O.png')
triangle = pygame.image.load ('Triangle_Pict.png')
circle = pygame.transform.scale (circle,(100,100))
triangle = pygame.transform.scale (triangle,(100,100))
list1 = [circle,triangle]
print (list1)
while True:
    figurex = random.randint (0,500)
    figurey = random.randint (0,500)
    for loop in list1:
        screen.fill ((255,255,255))
        screen.blit (loop,(figurex,figurey))
        time.sleep (1)
        pygame.display.update ()
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
    pygame.display.update ()

##import pygame
##from pygame.locals import*
##pygame.init()
##screen=pygame.display.set_mode((600,600))
##pygame.display.set_caption("Sprite animation")
##img=pygame.image.load("Tic-Tac-Toe_O.png")
##img=pygame.transform.scale(img,(100,100))
##img1=pygame.image.load("Triangle_Pict.png")
##img1=pygame.transform.scale(img1,(100,100))
##pygame.display.update()
##import time
##l=[]
##
##l.append(img)
##l.append(img1)
##print(l)
##clock=pygame.time.Clock()
##x=200
##y=200
##w=200
##z=200
##
##
##while True:
##   
##    pygame.display.update()
##    for i in l:
##        screen.blit(i,(x,y))
##        time.sleep(1)
##        screen.fill((255,255,255))
##        screen.blit(i,(w,z))
##        time.sleep(1)
##        pygame.display.update()
##   
##    for event in pygame.event.get():
##        if event.type==QUIT:
##            pygame.quit()
##            exit()
