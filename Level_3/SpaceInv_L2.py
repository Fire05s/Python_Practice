import pygame
import random
import time
pygame.init ()
from pygame.locals import *
def lvl2 ():
    screen = pygame.display.set_mode ((600,600))
    pygame.display.set_caption ('Screen')
    image1 = pygame.image.load ('Alien1.png')
    image1 = pygame.transform.scale (image1,(20,20))
    image2 = pygame.image.load ('Alien2.png')
    image2 = pygame.transform.scale (image2,(20,20))
    image3 = pygame.image.load ('Alien4.png')
    image3 = pygame.transform.scale (image3,(20,20))

    shipimage = pygame.image.load ('Ship.png')
    shipimage = pygame.transform.scale (shipimage,(50,50))

    projimage = pygame.image.load ('Laser.png')
    projimage = pygame.transform.scale (projimage,(10,10))

    lifeimage = pygame.image.load ('Life.png')
    lifeimage = pygame.transform.scale (lifeimage,(30,30))

    def text (msg,x1,y1,msgcol):
        fontobj = pygame.font.SysFont ('Times New Roman',30)
        msgobj = fontobj.render (msg,False,msgcol)
        screen.blit (msgobj,(x1,y1))

    class character:
        def __init__ (self,x,y,image,length,width):
            self.x = x
            self.y = y
            self.img = image
            self.l = length
            self.w = width
        def draw (self):
            screen.blit (self.img,(self.x,self.y))

    class alien (character):
        def __init__ (self,x,y,image,length,width):
            super ().__init__ (x,y,image,length,width)
            self.change = 10
            self.direction = 1
        def move (self):
            self.x += self.change
    ##        if self.direction == 1:
    ##            self.x += self.change
    ##        else:
    ##            self.x -= self.change

    arow = []
    def createaliens ():
        x = 60
        y = 50
        for loop in range (1,2,1):
            a1 = alien (x,y,pygame.transform.scale (pygame.image.load ('Alien1.png'),(20,20)),20,20)
            arow.append (a1)
            x = x + 50
            if loop % 10 == 0:
                x = 60
                y += 20
    createaliens ()

    start = time.time () #starts at 0

    step = 1
    countaliens = 0

    changedir = False

    amovestart = time.time ()

    class ship (character):
        def __init__ (self,x,y,image,length,width):
            super ().__init__ (x,y,image,length,width)
            self.direction = None
        def move (self):
            if self.direction == 'left':
                self.x -= 0.5
            if self.direction == 'right':
                self.x += 0.5
            if self.x + self.w >= 600:
                self.x = self.x - self.w
            if self.x <= 0:
                self.x = 0

    player = ship (265,550,shipimage,50,50)

    class laser (character):
        def __init__ (self,x,y,image,length,width):
            super ().__init__ (x,y,image,length,width)
        def move (self):
            self.y -= 15

    lmove = False
    lock = 0
    laslist = []

    state = ''

    #Level 2 Specific Code
    class supera (alien):
        def __init__ (self,x,y,image,length,width):
            super ().__init__ (x,y,image,length,width)
            self.change = 20
            self.lives = 3
            self.indchange = False
        def move (self):
            self.x += self.change
            if self.x + self.w >= 600:
                self.change = -self.change
                self.y += 30
            elif self.x <= 10:
                self.change = -self.change
                self.y += 30
            if self.y >= 650:
                self.y = -30
    randspawn = random.randint (3,5)
    spawnstart = time.time ()
    superl = []
    print (randspawn)

    clock = pygame.time.Clock ()
    resety = False
    while state == '':
        #clock.tick (60)
        screen.fill ((123,123,123))
        end = time.time ()
        amoveend = time.time ()
        spawnend = time.time ()
        #diff = end - start
        amovediff = amoveend - amovestart
        spawndiff=  spawnend - spawnstart
        for loop in arow:
            loop.draw ()
        player.draw ()
        player.move ()
        if amovediff >= 0.5 and amovediff <= 0.6:
            amovestart = time.time ()
            for loop in arow:
                if loop.x <= player.x <= loop.x + loop.w and loop.y <= player.y <= loop.y + loop.l:
                    print ('Lose Level 2')
                    state = 'lose'
                loop.move ()
                if loop.x + loop.w >= 600:
                    changedir = True
                if loop.x <= 0:
                    changedir = True
                if loop.y >= 680:
                    resety = True
            #Added super alien move here
            for sloop in superl:
                if sloop.x <= player.x <= sloop.x + sloop.w and sloop.y <= player.y <= sloop.y + sloop.l:
                    print ('Lose Level 2')
                    state = 'lose'
                sloop.move ()
        if changedir == True:
            for loop in arow:
                loop.change = -loop.change
                loop.y += 30
            changedir = False
        if resety == True:
            for loop in arow:
                loop.y = loop.y - 770
            resety = False
        if arow == [] and superl == []:
            print ('Win Level 2')
            state = 'win'

        #Level 2 Specific Code
        if spawndiff >= randspawn:
            spawnstart= time.time ()
            randspawn = random.randint (3,5)
            print (randspawn)
            addsuper = supera (1,0,image2,20,20)
            if len (superl) <= 9:
                superl.append (addsuper)
        for loop in superl:
            loop.draw ()
        
        for event in pygame.event.get ():
            if event.type == QUIT:
                pygame.quit ()
                exit ()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    player.direction = 'right'
                if event.key == K_LEFT:
                    player.direction = 'left'
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    player.direction = False
                    player.direction = False
                if event.key == K_LEFT:
                    player.direction = False
                    player.direction = False
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                (clickx,clicky) = event.pos
                lmove = True
            if event.type == MOUSEBUTTONUP and event.button == 1:
                lmove = False
            if lmove == True:
                #lock += 1
                addlaser = laser (player.x + 20,player.y,projimage,10,10)
                laslist.append (addlaser)
        for lasloop in laslist:
            lasloop.draw ()
            lasloop.move ()
            for aloop in arow:
                if aloop.x <= lasloop.x <= aloop.x + aloop.w or aloop.x <= lasloop.x + lasloop.w <= aloop.x + aloop.w:
                    if aloop.y <= lasloop.y <= aloop.y + aloop.l or aloop.y <= lasloop.y + lasloop.l <= aloop.y + aloop.l:
                        arow.remove (aloop)
                        laslist.remove (lasloop)
                        break
            for aloop in superl:
                if aloop.x <= lasloop.x <= aloop.x + aloop.w or aloop.x <= lasloop.x + lasloop.w <= aloop.x + aloop.w:
                    if aloop.y <= lasloop.y <= aloop.y + aloop.l or aloop.y <= lasloop.y + lasloop.l <= aloop.y + aloop.l:
                        laslist.remove (lasloop)
                        aloop.lives -= 1
                        if aloop.lives == 0:
                            superl.remove (aloop)
                        break
            if lasloop.y <= 0:
                laslist.remove (lasloop)
        pygame.display.update ()
    pygame.quit ()
    return state
