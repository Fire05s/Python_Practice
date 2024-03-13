import pygame
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')
def checkerboard ():
    col1 = (255,0,0)
    col2 = (0,0,255)
    for loop in range (0,600,200):
        pygame.draw.rect (screen,(col1),(loop,0,200,200))
        col1,col2 = col2,col1
    for loop1 in range (0,600,200):
        pygame.draw.rect (screen,(col1),(loop1,200,200,200))
        col1,col2 = col2,col1
    for loop2 in range (0,600,200):
        pygame.draw.rect (screen,(col1),(loop2,400,200,200))
        col1,col2 = col2,col1
checkerboard ()
while True:
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
    pygame.display.update ()
