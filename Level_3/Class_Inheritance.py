import random

##class person:
##    def __init__ (self,first,last,email,DOB):
##        self.first = first
##        self.last = last
##        self.email = email
##        self.DOB = DOB
##    def show (self):
##        print (self.first,self.last,self.email,self.DOB)

##p1 = person ('Brandon','Tsai','b..','12/21')

##class student (person):
##    #pass
##    def __init__ (self,first,last,email,DOB,age):
##        person.__init__ (self,first,last,email,DOB)
##        self.age = age
##    def show1 (self):
##        print (self.age)

##s1 = student ('Brandon','Tsai','b..','12/21',14)
##s1.show ()
##s1.show1 ()

##class student (person):
##    #pass
##    def __init__ (self,first,last,email,DOB,sid,GPA):
##        super ().__init__ (first,last,email,DOB)
##        self.sid = sid
##        self.gpa = GPA
##    def show1 (self):
##        print (self.sid,self.gpa)
##
##s1 = student ('Brandon','Tsai','b...','12/21',14,4)
##s2 = student ('John','Smith','jsmith...','2/5',10,4)
##s3 = student ('Jane','Smith','jn...','8/2',13,3)
##s4 = student ('Jim','Mann','jman...','9/15',12,2)
##slist = [s1,s2,s3,s4]
##
##class teacher (person):
##    def __init__ (self,first,last,email,DOB,tid,slist):
##        super ().__init__ (first,last,email,DOB)
##        self.tid = tid
##        self.slist = slist
##        self.csize = len (slist)
##    def show2 (self):
##        print (self.tid,self.slist)
##    def show_student (self):
##        print (self.first,self.last)
##        for loop in self.slist:
##            loop.show ()
##            loop.show1 ()
##            print ()
##    def add (self,alist):
##        for loop in alist:
##            self.slist.append (loop)
##        self.csize = len (self.slist)
##        print (self.csize)
##    def remove (self,rlist):
##        for loop in rlist:
##            self.slist.remove (loop)
##        self.csize = len (self.slist)
##        print (self.csize)
##t1 = teacher ('Mike','Johnson','mj...','1/28',1,slist)
##t1.show_student ()
##t1.remove ([s3,s4])
##t1.show_student ()
##t1.add ([s3])
##t1.show_student ()

import pygame
import random
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')

def text (msg,x1,y1,msgcol):
    fontobj = pygame.font.SysFont ('Times New Roman',30)
    msgobj = fontobj.render (msg,False,msgcol)
    screen.blit (msgobj,(x1,y1))

class shapes:
    def __init__ (self):
        self.x = random.randint (0,500)
        self.y = random.randint (0,500)
        self.color = (random.randint (0,255),random.randint (0,255),random.randint (0,255))

class rect (shapes):
    def __init__ (self,height,width):
        super ().__init__ ()
        self.height = height
        self.width = width
    def draw (self):
        pygame.draw.rect (screen,self.color,(self.x,self.y,self.height,self.width))

class circle (shapes):
    def __init__ (self,r):
        super ().__init__ ()
        self.r = r
    def draw (self):
        pygame.draw.circle (screen,self.color,(self.x,self.y),self.r)

r1 = rect (100,50)
c1 = circle (50)
olist = [r1,c1]
while True:
    screen.fill ((0,0,0))
    for loop in olist:
        loop.draw ()
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
        if event.type == KEYDOWN:
            if event.key == K_r:
                r = rect (10,20)
                olist.append (r)
            if event.key == K_c:
                c = circle (20)
                olist.append (c)
            if event.key == K_s:
                s = rect (15,15)
                olist.append (s)
    pygame.display.update ()
