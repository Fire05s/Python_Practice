import pygame
import random
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Server Screen')

import socket
s = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
host = ''
port = 12345
s.bind ((host,port))
s.listen (5)
print ('listening')
conn,addr = s.accept ()
print ('connection received from',addr)

def text (msg,x1,y1,msgcol):
    fontobj = pygame.font.SysFont ('Times New Roman',30)
    msgobj = fontobj.render (msg,False,msgcol)
    screen.blit (msgobj,(x1,y1))

xserv = 0
yserv = 300
while True:
    screen.fill ((0,0,0))
    if xserv <= 590:
        pygame.draw.circle (screen,(255,255,255),(xserv,yserv),10)
        xserv += 10
        print (xserv)
    else:
        coords = str (xserv) + ' ' + str (yserv)
        print (coords)
        conn.sendall (coords.encode ())
##        coords = conn.recv (1024)
##        xclient,xserver = coords [0],coords [1]
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
    pygame.display.update ()
