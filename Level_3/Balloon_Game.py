import pygame,random,winsound
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')
def text (msg,x1,y1,msgcol):
    fontobj = pygame.font.SysFont ('Times New Roman',30)
    msgobj = fontobj.render (msg,False,msgcol)
    screen.blit (msgobj,(x1,y1))
class balloon:
    def __init__ (self):
        self.x = random.randint (0,500)
        self.y = 700
        self.balloon1 = pygame.image.load ('Balloon.png')
        self.balloon1 = pygame.transform.scale (self.balloon1,(100,100))
        self.letter = [chr (var1) for var1 in range (97,123,1)]
        self.randlett = random.choice (self.letter)
    def display (self):
        screen.blit (self.balloon1,(self.x,self.y))
        loop1.text (self.randlett,self.x+45,self.y+25,(255,255,255))
        loop1.text ('Score: '+str(score),250,50,(255,255,255))
        pygame.display.update ()
    def text (self,msg,x1,y1,msgcol):
        fontobj = pygame.font.SysFont ('Times New Roman',30)
        msgobj = fontobj.render (msg,False,msgcol)
        screen.blit (msgobj,(x1,y1))
    def move (self):
        self.y = self.y - 3
        
moveball = [balloon ()]
clock = pygame.time.Clock ()
score = 0
speed = 30
var1 = True
(b1f,b1t) = (9000,10)
(b2f,b2t) = (5000,50)
while var1 == True:
    screen.fill ((0,0,0))
    clock.tick (speed)
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
        if event.type == KEYDOWN:
            kpress = pygame.key.name (event.key)
            moveball.append (balloon ())
            for loop in moveball:
                if kpress == loop.randlett:
                    moveball.remove (loop)
                    score = score + 1
                    pygame.display.update ()
##                    pygame.mixer.music.load ('Correct_Sound.mp3')
##                    pygame.mixer.music.play (0)
                    
##                    winsound.Beep (b1f,b1t)
                    break
            if kpress != loop.randlett:
                score = score - 1
##                winsound.Beep (b2f,b2t)
            if score % 2 == 0:
                speed = speed + 5
                if score % 4 == 0:
                    moveball.append (balloon ())
            
    for loop1 in moveball:
        loop1.move ()
        loop1.display ()
        if loop1.y <= -100:
            score = score - 5
            moveball.remove (loop1)
            print (score)
            var1 = False
        if score < 0:
            loop1.text ('You Lose!',250,100,(255,0,0))
            pygame.display.update ()
            print (score)
            var1 = False
    pygame.display.update ()
