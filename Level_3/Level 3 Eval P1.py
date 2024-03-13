import pygame,random
from pygame.locals import *
pygame.init ()
screen = pygame.display.set_mode ((600,600))

class cell:
    def __init__ (self,x,y,r,color):
        self.x = x
        self.y = y
        self.r = r
        self.col = color
    def draw (self):
        pygame.draw.circle (screen,self.col,(self.x,self.y),self.r)

clist = []
for loop in range (0,30,1):
    c1 = cell (random.randint (0,600),random.randint (0,600),random.randint (1,20),(random.randint (0,255),random.randint (0,255),random.randint (0,255)))
    clist.append (c1)

player = cell (300,300,5,(255,255,255))

game = True
while game == True:
    screen.fill ((0,0,0))
    for cloop in clist:
        cloop.draw ()
        if cloop.x - cloop.r <= player.x + player.r <= cloop.x + cloop.r or cloop.x - cloop.r <= player.x - player.r <= cloop.x + cloop.r:
            if cloop.y - cloop.r <= player.y - player.r <= cloop.y + cloop.r or cloop.y - cloop.r <= player.y + player.r <= cloop.y + cloop.r:
                if cloop.r < player.r:
                    player.r += cloop.r
                    clist.remove (cloop)
                else:
                    game = False
    player.draw ()
    pygame.display.update ()
    for event in pygame.event.get ():
        if event.type == pygame.MOUSEMOTION:
            (player.x,player.y) = event.pos
            print (player.x,player.y)
        if event.type == pygame.QUIT:
            pygame.quit ()
            exit ()
print ('Game Over')
