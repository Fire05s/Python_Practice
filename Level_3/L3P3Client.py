import pygame
import random
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Client Screen')

import socket
host = 'localhost'
port = 12345
s = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
s.connect ((host,port))

def text (msg,x1,y1,msgcol):
    fontobj = pygame.font.SysFont ('Times New Roman',30)
    msgobj = fontobj.render (msg,False,msgcol)
    screen.blit (msgobj,(x1,y1))
xclient = 0
yclient = 300
coords = ''
while True:
    screen.fill ((0,0,0))
    coords = s.recv (1024).decode ()
    
    xserv,yserv = coords.split ()
    print (coords,xserv,yserv)
    if coords != ():
        pygame.draw.circle (screen,(255,255,255),(xclient,yclient),10)
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
    pygame.display.update ()
