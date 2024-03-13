import pygame
import random
import time
pygame.init ()
from pygame.locals import *
def lvl3 ():
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

    projimage1 = pygame.image.load ('Alien_Laser2.png')
    projimage1 = pygame.transform.scale (projimage1,(10,10))

    lifeimage = pygame.image.load ('Life.png')
    lifeimage = pygame.transform.scale (lifeimage,(30,30))

    def text (msg,x1,y1,msgcol):
        fontobj = pygame.font.SysFont ('Times New Roman',15)
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
            self.hp = 100
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
            self.change = 15
        def move (self):
            self.y -= self.change

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
    print ('super',randspawn)

    #Level 3 Specific Code
    class shoota (alien):
        def __init__ (self,x,y,image,length,width):
            super ().__init__ (x,y,image,length,width)
            self.change = 50
            self.lives = 5
            self.firetime = random.randint (3,6)
            self.alaserstart = time.time ()
            self.alaserend = 0
            self.alaserdiff = 0
            self.alaslist = []
        def move (self):
            self.x += self.change
            if self.x + self.w >= 550:
                self.change = -self.change
                self.y += 30
            elif self.x <= 10:
                self.change = -self.change
                self.y += 30
            if self.y >= 650:
                self.y = -30
        def shoot (self):
            self.alaserend = time.time ()
            self.alaserdiff = int (self.alaserend) - int (self.alaserstart)
            if int (self.alaserdiff) >= self.firetime:
                self.alaserstart = time.time ()
                addalaser = laser (self.x + 5,self.y + 10,projimage1,10,10)
                addalaser.change = -5
                self.alaslist.append (addalaser)
    randspawn1 = random.randint (3,8)
    spawnstart1 = time.time ()
    shooterl = []
    print ('shooter',randspawn1)

    clock = pygame.time.Clock ()
    resety = False
    while state == '':
        #clock.tick (60)
        screen.fill ((123,123,123))
        end = time.time ()
        amoveend = time.time ()
        spawnend = time.time ()
        spawnend1 = time.time ()
        #diff = end - start
        amovediff = amoveend - amovestart
        spawndiff=  spawnend - spawnstart
        spawndiff1 = spawnend1 - spawnstart1
        for loop in arow:
            loop.draw ()
        player.draw ()
        player.move ()
        text (str (player.hp) + ' HP',550,530,(255,0,0))
        if amovediff >= 0.5 and amovediff <= 0.6:
            amovestart = time.time ()
            for loop in arow:
                if loop.x <= player.x <= loop.x + loop.w and loop.y <= player.y <= loop.y + loop.l:
                    print ('Lose Level 3')
                    state = 'lose'
                loop.move ()
                if loop.x + loop.w >= 600:
                    changedir = True
                if loop.x <= 0:
                    changedir = True
                if loop.y >= 680:
                    resety = True
            #Super alien move
            for sloop in superl:
                if sloop.x <= player.x <= sloop.x + sloop.w and sloop.y <= player.y <= sloop.y + sloop.l:
                    print ('Lose Level 3')
                    state = 'lose'
                sloop.move ()
            #Shooter alien move
            for shloop in shooterl:
                if shloop.x <= player.x <= shloop.x + shloop.w and shloop.y <= player.y <= shloop.y + shloop.l:
                    print ('Lose Level 3')
                    state = 'lose'
                shloop.move ()
        if changedir == True:
            for loop in arow:
                loop.change = -loop.change
                loop.y += 30
            changedir = False
        if resety == True:
            for loop in arow:
                loop.y = loop.y - 770
            resety = False
        if arow == [] and superl == [] and shooterl == []:
            print ('Win Level 3')
            state = 'win'

        #Level 2 Specific Code
        if spawndiff >= randspawn:
            spawnstart = time.time ()
            randspawn = random.randint (3,5)
            print ('super',randspawn)
            addsuper = supera (1,0,image2,20,20)
            if len (superl) <= 9:
                superl.append (addsuper)
        for aloop in superl:
            aloop.draw ()

        #Level 3 Specific Code
        if spawndiff1 >= randspawn1:
            spawnstart1 = time.time ()
            randspawn1 = random.randint (3,8)
            print ('shooter',randspawn1)
            addshooter = shoota (1,0,image3,20,20)
            if len (shooterl) <= 9:
                shooterl.append (addshooter)
        for aloop in shooterl:
            aloop.draw ()
            aloop.shoot ()
            for alasloop in aloop.alaslist:
                alasloop.draw ()
                alasloop.move ()
                if player.x <= alasloop.x <= player.x + player.w or player.x <= alasloop.x + alasloop.w <= player.x + player.w:
                    if player.y <= alasloop.y <= player.y + player.l or player.y <= alasloop.y + alasloop.l <= player.y + player.l:
                
    ##            if player.x <= alasloop.lasrectx <= player.x + player.w or player.x <= alasloop.lasrectx + alasloop.w <= player.x + player.w:
    ##                if player.y <= alasloop.lasrecty <= player.y + player.l or player.y <= alasloop.lasrecty + alasloop.l <= player.y + player.l:
                        
                        aloop.alaslist.remove (alasloop)
                        player.hp -= 10
                        print (player.hp,'hit')
                        if player.hp == 0:
                            print ('Lose Level 3')
                            state = 'lose'
                        break
                if alasloop.y >= 610:
                    aloop.alaslist.remove (alasloop)
        
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
            removed = False
            for aloop in arow:
                if aloop.x <= lasloop.x <= aloop.x + aloop.w or aloop.x <= lasloop.x + lasloop.w <= aloop.x + aloop.w:
                    if aloop.y <= lasloop.y <= aloop.y + aloop.l or aloop.y <= lasloop.y + lasloop.l <= aloop.y + aloop.l:
                        arow.remove (aloop)
                        laslist.remove (lasloop)
                        removed = True
                        break
                    break
            if removed == False:
                for aloop in superl:
                    if aloop.x <= lasloop.x <= aloop.x + aloop.w or aloop.x <= lasloop.x + lasloop.w <= aloop.x + aloop.w:
                        if aloop.y <= lasloop.y <= aloop.y + aloop.l or aloop.y <= lasloop.y + lasloop.l <= aloop.y + aloop.l:
                            laslist.remove (lasloop)
                            aloop.lives -= 1
                            if aloop.lives == 0:
                                superl.remove (aloop)
                            removed = True
                            break
                        break

            if removed == False:
                for aloop in shooterl:
                    if aloop.x <= lasloop.x <= aloop.x + aloop.w or aloop.x <= lasloop.x + lasloop.w <= aloop.x + aloop.w:
                        if aloop.y <= lasloop.y <= aloop.y + aloop.l or aloop.y <= lasloop.y + lasloop.l <= aloop.y + aloop.l:
                            laslist.remove (lasloop)
                            aloop.lives -= 1
                            if aloop.lives == 0:
                                shooterl.remove (aloop)
                            break
                        break
            if lasloop.y <= -10:
                laslist.remove (lasloop)
        pygame.display.update ()
    pygame.quit ()
    return state
