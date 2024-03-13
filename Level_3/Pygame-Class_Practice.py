import pygame
import random
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')
def text (msg,x1,y1,msgcol):
    fontobj = pygame.font.SysFont ('Times New Roman',15)
    msgobj = fontobj.render (msg,False,msgcol)
    screen.blit (msgobj,(x1,y1))

##class circle: #1
##    def __init__ (self,r,x,y,col):
##        self.r = r
##        self.x = x
##        self.y = y
##        self.col = col
##    def draw (self):
##        pygame.draw.circle (screen,(self.col),(self.x,self.y),self.r)
##circ1 = circle (15,random.randint (0,600),random.randint (0,600),(random.randint (0,255),random.randint (0,255),random.randint (0,255)))
##circ2 = circle (15,random.randint (0,600),random.randint (0,600),(random.randint (0,255),random.randint (0,255),random.randint (0,255)))
##circ3 = circle (15,random.randint (0,600),random.randint (0,600),(random.randint (0,255),random.randint (0,255),random.randint (0,255)))
##circ4 = circle (15,random.randint (0,600),random.randint (0,600),(random.randint (0,255),random.randint (0,255),random.randint (0,255)))
##circ5 = circle (15,random.randint (0,600),random.randint (0,600),(random.randint (0,255),random.randint (0,255),random.randint (0,255)))
##circ6 = circle (15,random.randint (0,600),random.randint (0,600),(random.randint (0,255),random.randint (0,255),random.randint (0,255)))
##circ7 = circle (15,random.randint (0,600),random.randint (0,600),(random.randint (0,255),random.randint (0,255),random.randint (0,255)))
##circ8 = circle (15,random.randint (0,600),random.randint (0,600),(random.randint (0,255),random.randint (0,255),random.randint (0,255)))
##circ9 = circle (15,random.randint (0,600),random.randint (0,600),(random.randint (0,255),random.randint (0,255),random.randint (0,255)))
##circ10 = circle (15,random.randint (0,600),random.randint (0,600),(random.randint (0,255),random.randint (0,255),random.randint (0,255)))
##circ1.draw ()
##circ2.draw ()
##circ3.draw ()
##circ4.draw ()
##circ5.draw ()
##circ6.draw ()
##circ7.draw ()
##circ8.draw ()
##circ9.draw ()
##circ10.draw ()

##class circle: #2
##    def __init__ (self,r,x,y,col):
##        self.r = r
##        self.x = x
##        self.y = y
##        self.col = col
##        self.speed = random.randint (3,7)
##        self.letter = [chr (var1) for var1 in range (97,123,1)]
##        self.randlett = random.choice (self.letter)
##        self.appear = True
##    def text (self,msg,x1,y1,msgcol):
##        fontobj = pygame.font.SysFont ('Times New Roman',30)
##        msgobj = fontobj.render (msg,False,msgcol)
##        screen.blit (msgobj,(x1,y1))
##    def draw (self):
##        pygame.draw.circle (screen,(self.col),(self.x,self.y),self.r)
##        list1 [loop].text (self.randlett,self.x-5,self.y-25,(255,255,255))
##        self.x = self.x + self.speed
##        if self.x >= 615: #Reappearing
##            self.x = -15
##        if self.x >= 600: #Bouncing
##            self.speed = -self.speed
##        elif self.x <= 0:
##            self.speed = -self.speed
##list1 = []
##clock = pygame.time.Clock ()
##circkey = False
##for loop in range (0,10,1):
##    c1 = circle (25,30+loop*70,100,(random.randint (0,255),random.randint (0,255),random.randint (0,255)))
##    list1.append (c1)
##for loop in range (0,10,1):
##    c1 = circle (25,30+loop*70,300,(random.randint (0,255),random.randint (0,255),random.randint (0,255)))
##    list1.append (c1)
##for loop in range (0,10,1):
##    c1 = circle (25,30+loop*70,500,(random.randint (0,255),random.randint (0,255),random.randint (0,255)))
##    list1.append (c1)

##class circle: #3
##    def __init__ (self,y,col):
##        self.r = 15
##        self.x = 20
##        self.y = y
##        self.col = col
##        self.speed = random.randint (3,7)
##        self.score = 0
##    def text (self,msg,x1,y1,msgcol):
##        fontobj = pygame.font.SysFont ('Times New Roman',15)
##        msgobj = fontobj.render (msg,False,msgcol)
##        screen.blit (msgobj,(x1,y1))
##    def draw (self):
##        global finishers
##        pygame.draw.circle (screen,(self.col),(self.x,self.y),self.r)
##        self.x = self.x + self.speed
##        if self.x >= 600:
##            self.speed = -self.speed
##        elif self.x <= 0:
##            self.speed = -self.speed
##            self.score = self.score + 1
##            if self.score == 10:
##                self.speed = 0
##                self.x = 0
##                finishers = finishers + 1
##                print (finishers)
##                if finishers == 1:
##                    self.col = (255,0,0)
##                    text ('<-- 1st Place',self.x+50,self.y,(255,255,0))
##                if finishers == 2:
##                    self.col = (0,0,255)
##                    text ('<-- 2nd Place',self.x+50,self.y,(50,50,50))
##                if finishers == 3:
##                    self.col = (0,255,0)
##                    text ('<-- 3rd Place',self.x+50,self.y,(100,100,0))
##list1 = []
##clock = pygame.time.Clock ()
##for loop in range (0,10,1):
##    c1 = circle (70+loop*50,(random.randint (0,255),random.randint (0,255),random.randint (0,255)))
##    list1.append (c1)
##move = False
##finishers = 0

class circle: #4
    rad = 15 #Increasing/Decreasing all radii
    def __init__ (self):
        #self.r = 15
        self.x = random.randint (0,600)
        self.y = random.randint (0,600)
        self.col = (random.randint (0,255),random.randint (0,255),random.randint (0,255))
    def draw (self):
        pygame.draw.circle (screen,(self.col),(self.x,self.y),self.rad)
list1 = []
clock = pygame.time.Clock ()
for loop in range (0,10,1):
    c1 = circle ()
    list1.append (c1)

##class circle: #5
##    def __init__ (self):
##        self.r = 15
##        self.x = random.randint (0,600)
##        self.y = random.randint (0,600)
##        red = (255,0,0)
##        blue = (0,0,255)
##        self.col = random.choice ([red,blue])
##        self.speedx = 0
##        self.speedy = 0
##    def draw (self):
##        pygame.draw.circle (screen,(self.col),(self.x,self.y),self.r)
##        self.x = self.x + self.speedx
##        self.y = self.y + self.speedy
##        if self.col == (255,0,0):
##            self.speedx = 5
##            self.speedy = 0
##        else:
##            self.speedy = 5
##            self.speedx = 0
##        if self.x >= 600: #Bouncing conditions don't work
##            self.speedx = -self.speedx
##        elif self.x <= 0:
##            self.speedx = -self.speedx
##        elif self.y >= 600:
##            self.speedy = -self.speedy
##        elif self.y <= 0:
##            self.speedy = -self.speedy
##list1 = []
##clock = pygame.time.Clock ()
##for loop in range (0,20,1):
##    c1 = circle ()
##    list1.append (c1)

#Skipped Alien Question

##class circle:
##    def __init__ (self):
##        self.r = 15
##        self.x = random.randint (0,600)
##        self.y = random.randint (0,600)
##        self.col = (random.randint (0,255),random.randint (0,255),random.randint (0,255))
##    def draw (self):
##        pygame.draw.circle (screen,(self.col),(self.x,self.y),self.r)
##list1 = []
##for loop in range (0,10,1):
##    circ1 = circle ()
##    list1.append (circ1)
##    list1 [loop].draw ()

while True:

    screen.fill ((0,0,0))

##    clock.tick (60) #2
##    for loop in range (0,30,1):
##        if list1 [loop].appear == True:
##            list1 [loop].draw ()

##    clock.tick (60) #3
##    text ('# of Finishers: '+str (finishers),500,25,(255,255,0))
##    for loop in range (0,10,1):
##        if move == True:
##            list1 [loop].draw ()
##        else:
##            text ('Press SPACEBAR to start the race.',200,270,(255,255,255))

    clock.tick (60) #4
    for loop in list1:
        loop.draw ()

##    clock.tick (60) #5
##    for loop in list1:
##        loop.draw ()

    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
    
##        if event.type == KEYDOWN: #2
##            kpress = pygame.key.name (event.key)
##            circkey = True
##        if event.type == KEYUP:
##            circkey = False
##    if circkey == True:
##        for loop in list1:
##            if kpress == loop.randlett:
##                loop.appear = not loop.appear
            
##        if event.type == KEYDOWN: #3
##            if event.key == K_SPACE:
##                move = True

        if event.type == KEYDOWN: #4
            if event.key == K_UP: #Increasing/Decreasing all radii
                circle.rad = circle.rad + 2
            if event.key == K_DOWN:
                circle.rad = circle.rad - 2
            if event.key == pygame.MOUSEBUTTONDOWN and event.button == 1: #Increasing/Decreasing individual circles
                cx,cy = event.pos
                for loop in list1:
                    if loop.x-loop.rad <= cx <= loop.x+loop.rad and loop.y-loop.rad <= cy <= loop.y+loop.rad:
                        loop.rad = loop.rad + 2
            if event.key == pygame.MOUSEBUTTONDOWN and event.button == 3:
                cx,cy = event.pos
                for loop in list1:
                    if loop.x-loop.rad <= cx <= loop.x+loop.rad and loop.y-loop.rad <= cy <= loop.y+loop.rad:
                        loop.rad = loop.rad - 2
            
##            if event.type == KEYDOWN: #KEYDOWN doesn't work #5
##                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #Increasing/Decreasing individual circles
##                    cx,cy = event.pos
##                    print (cx,cy)
##                    for loop in list1:
##                        if loop.x-loop.r <= cx <= loop.x+loop.r and loop.y-loop.r <= cy <= loop.y+loop.r:
##                            for loop in list1:
##                                if loop.col == (255,0,0):
##                                    loop.col = (0,0,255)
##                                else:
##                                    loop.col = (255,0,0)

    pygame.display.update ()
