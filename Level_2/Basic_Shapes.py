import pygame
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')
while True:
##    pygame.draw.rect (screen,(255,255,255),(50,50,100,50),5)
##    pygame.draw.circle (screen,(255,255,255),(100,100),30,3)
##    pygame.draw.line (screen,(255,255,255),(50,50),(150,150))

##    pygame.draw.line (screen,(255,255,255),(50,50),(50,100))
##    pygame.draw.line (screen,(255,255,255),(50,100),(75,75))
##    pygame.draw.line (screen,(255,255,255),(75,75),(50,50))

##    pygame.draw.rect (screen,(255,255,255),(0,0,100,100))
##    pygame.draw.rect (screen,(255,255,255),(500,500,600,600))

##    pygame.draw.circle (screen,(255,255,255),(0,0),30)
##    pygame.draw.circle (screen,(255,255,255),(0,600),30)
##    pygame.draw.circle (screen,(255,255,255),(600,0),30)
##    pygame.draw.circle (screen,(255,255,255),(600,600),30)
##    pygame.draw.circle (screen,(255,255,255),(300,300),30)

##    pygame.draw.line (screen,(255,255,255),(0,0),(600,600))
##    pygame.draw.line (screen,(255,255,255),(600,0),(0,600))

    pygame.draw.polygon (screen,(255,255,255),((100,100),(150,150),(125,325),(50,300)),1)
    
##    for x in range (0,600,100):
##        pygame.draw.line (screen,(255,255,255),(x,0),(x,600))
##    for y in range (0,600,100):
##        pygame.draw.line (screen,(255,255,255),(0,y),(600,y))
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
    pygame.display.update ()
