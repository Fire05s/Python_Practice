import pygame
#from Checkerboard import checkerboard
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')
#def checkerboard ():
col1 = (0,0,0)
col2 = (255,255,0)
for loop in range (0,600,200):
    pygame.draw.rect (screen,(col1),(loop,0,200,200))
    col1,col2 = col2,col1
for loop1 in range (0,600,200):
    pygame.draw.rect (screen,(col1),(loop1,200,200,200))
    col1,col2 = col2,col1
for loop2 in range (0,600,200):
    pygame.draw.rect (screen,(col1),(loop2,400,200,200))
    col1,col2 = col2,col1
dict1 = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
turn = 0
x,y = 0,0
def text (msg,x1,y1,msgcol):
    fontobj = pygame.font.SysFont ('Times New Roman',30)
    msgobj = fontobj.render (msg,False,msgcol)
    screen.blit (msgobj,(x1,y1))
while True:
    #checkerboard ()
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            print (x,y)
            if 0 < x < 200 and 0 < y < 200 and dict1 [1] == '':
                if turn % 2 == 0:
                    pygame.draw.line (screen,(255,255,255),(50,50),(150,150),5)
                    pygame.draw.line (screen,(255,255,255),(150,50),(50,150),5)
                    dict1 [1] = 'X'
                else:
                    pygame.draw.circle (screen,(255,255,255),(100,100),50,5)
                    dict1 [1] = 'O'
            if 200 < x < 400 and 0 < y < 200 and dict1 [2] == '':
                if turn % 2 == 0:
                    pygame.draw.line (screen,(255,255,255),(250,50),(350,150),5)
                    pygame.draw.line (screen,(255,255,255),(350,50),(250,150),5)
                    dict1 [2] = 'X'
                else:
                    pygame.draw.circle (screen,(255,255,255),(300,100),50,5)
                    dict1 [2] = 'O'
            if 400 < x < 600 and 0 < y < 200 and dict1 [3] == '':
                if turn % 2 == 0:
                    pygame.draw.line (screen,(255,255,255),(450,50),(550,150),5)
                    pygame.draw.line (screen,(255,255,255),(550,50),(450,150),5)
                    dict1 [3] = 'X'
                else:
                    pygame.draw.circle (screen,(255,255,255),(500,100),50,5)
                    dict1 [3] = 'O'
            if 0 < x < 200 and 200 < y < 400 and dict1 [4] == '':
                if turn % 2 == 0:
                    pygame.draw.line (screen,(255,255,255),(50,250),(150,350),5)
                    pygame.draw.line (screen,(255,255,255),(150,250),(50,350),5)
                    dict1 [4] = 'X'
                else:
                    pygame.draw.circle (screen,(255,255,255),(100,300),50,5)
                    dict1 [4] = 'O'
            if 200 < x < 400 and 200 < y < 400 and dict1 [5] == '':
                if turn % 2 == 0:
                    pygame.draw.line (screen,(255,255,255),(250,250),(350,350),5)
                    pygame.draw.line (screen,(255,255,255),(350,250),(250,350),5)
                    dict1 [5] = 'X'
                else:
                    pygame.draw.circle (screen,(255,255,255),(300,300),50,5)
                    dict1 [5] = 'O'
            if 400 < x < 600 and 200 < y < 400 and dict1 [6] == '':
                if turn % 2 == 0:
                    pygame.draw.line (screen,(255,255,255),(450,250),(550,350),5)
                    pygame.draw.line (screen,(255,255,255),(550,250),(450,350),5)
                    dict1 [6] = 'X'
                else:
                    pygame.draw.circle (screen,(255,255,255),(500,300),50,5)
                    dict1 [6] = 'O'
            if 0 < x < 200 and 400 < y < 600 and dict1 [7] == '':
                if turn % 2 == 0:
                    pygame.draw.line (screen,(255,255,255),(50,450),(150,550),5)
                    pygame.draw.line (screen,(255,255,255),(150,450),(50,550),5)
                    dict1 [7] = 'X'
                else:
                    pygame.draw.circle (screen,(255,255,255),(100,500),50,5)
                    dict1 [7] = 'O'
            if 200 < x < 400 and 400 < y < 600 and dict1 [8] == '':
                if turn % 2 == 0:
                    pygame.draw.line (screen,(255,255,255),(250,450),(350,550),5)
                    pygame.draw.line (screen,(255,255,255),(350,450),(250,550),5)
                    dict1 [8] = 'X'
                else:
                    pygame.draw.circle (screen,(255,255,255),(300,500),50,5)
                    dict1 [8] = 'O'
            if 400 < x < 600 and 400 < y < 600 and dict1 [9] == '':
                if turn % 2 == 0:
                    pygame.draw.line (screen,(255,255,255),(450,450),(550,550),5)
                    pygame.draw.line (screen,(255,255,255),(550,450),(450,550),5)
                    dict1 [9] = 'X'
                else:
                    pygame.draw.circle (screen,(255,255,255),(500,500),50,5)
                    dict1 [9] = 'O'
            turn = turn + 1
            print (dict1,turn)
    if dict1[1] == dict1[2] == dict1[3] != '':
        text (dict1[1] + ' Wins',300,300,(255,0,0))
        pygame.display.update ()
        break
    if dict1[1] == dict1[4] == dict1[7] != '':
        text (dict1[1] + ' Wins',300,300,(255,0,0))
        pygame.display.update ()
        break
    if dict1[1] == dict1[5] == dict1[9] != '':
        text (dict1[1] + ' Wins',300,300,(255,0,0))
        pygame.display.update ()
        break
    if dict1[2] == dict1[5] == dict1[8] != '':
        text (dict1[2] + ' Wins',300,300,(255,0,0))
        pygame.display.update ()
        break
    if dict1[3] == dict1[6] == dict1[9] != '':
        text (dict1[3] + ' Wins',300,300,(255,0,0))
        pygame.display.update ()
        break
    if dict1[4] == dict1[5] == dict1[6] != '':
        text (dict1[4] + ' Wins',300,300,(255,0,0))
        pygame.display.update ()
        break
    if dict1[7] == dict1[8] == dict1[9] != '':
        text (dict1[7] + ' Wins',300,300,(255,0,0))
        pygame.display.update ()
        break
    if dict1[3] == dict1[5] == dict1[7] != '':
        text (dict1[3] + ' Wins',300,300,(255,0,0))
        pygame.display.update ()
        break
    if dict1[1] != '' and dict1[2] != '' and dict1[3] != '' and dict1[4] != '' and dict1[5] != '' and dict1[6] != '' and dict1[7] != '' and dict1[8] != '' and dict1[9] != '':
        text ('Tie!',300,300,(255,0,0))
        pygame.display.update ()
        break
    pygame.display.update ()
