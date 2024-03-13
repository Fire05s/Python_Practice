import pygame
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')
col1 = (0,0,0)
col2 = (255,255,0)
dict1 = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
turn = 0
x,y = 0,0
def text (msg,x1,y1,msgcol):
    fontobj = pygame.font.SysFont ('Times New Roman',30)
    msgobj = fontobj.render (msg,False,msgcol)
    screen.blit (msgobj,(x1,y1))
image = pygame.image.load ('Tic-Tac-Toe_Board.png')
image = pygame.transform.scale (image,(600,600))
screen.blit (image,(0,0))
ximg = pygame.image.load ('Tic-Tac-Toe_X.png')
ximg = pygame.transform.scale (ximg,(200,200))
oimg = pygame.image.load ('Tic-Tac-Toe_O.png')
oimg = pygame.transform.scale (oimg,(200,200))
while True:
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            print (x,y)
            if 0 < x < 200 and 0 < y < 200 and dict1 [1] == '':
                if turn % 2 == 0:
                    screen.blit (ximg,(0,0))
                    pygame.display.update ()
                    dict1 [1] = 'X'
                else:
                    screen.blit (oimg,(0,0))
                    pygame.display.update ()
                    dict1 [1] = 'O'
            if 200 < x < 400 and 0 < y < 200 and dict1 [2] == '':
                if turn % 2 == 0:
                    screen.blit (ximg,(200,0))
                    pygame.display.update ()
                    dict1 [2] = 'X'
                else:
                    screen.blit (oimg,(200,0))
                    pygame.display.update ()
                    dict1 [2] = 'O'
            if 400 < x < 600 and 0 < y < 200 and dict1 [3] == '':
                if turn % 2 == 0:
                    screen.blit (ximg,(400,0))
                    pygame.display.update ()
                    dict1 [3] = 'X'
                else:
                    screen.blit (oimg,(400,0))
                    pygame.display.update ()
                    dict1 [3] = 'O'
            if 0 < x < 200 and 200 < y < 400 and dict1 [4] == '':
                if turn % 2 == 0:
                    screen.blit (ximg,(0,200))
                    pygame.display.update ()
                    dict1 [4] = 'X'
                else:
                    screen.blit (oimg,(0,200))
                    pygame.display.update ()
                    dict1 [4] = 'O'
            if 200 < x < 400 and 200 < y < 400 and dict1 [5] == '':
                if turn % 2 == 0:
                    screen.blit (ximg,(200,200))
                    pygame.display.update ()
                    dict1 [5] = 'X'
                else:
                    screen.blit (oimg,(200,200))
                    pygame.display.update ()
                    dict1 [5] = 'O'
            if 400 < x < 600 and 200 < y < 400 and dict1 [6] == '':
                if turn % 2 == 0:
                    screen.blit (ximg,(400,200))
                    pygame.display.update ()
                    dict1 [6] = 'X'
                else:
                    screen.blit (oimg,(400,200))
                    pygame.display.update ()
                    dict1 [6] = 'O'
            if 0 < x < 200 and 400 < y < 600 and dict1 [7] == '':
                if turn % 2 == 0:
                    screen.blit (ximg,(0,400))
                    pygame.display.update ()
                    dict1 [7] = 'X'
                else:
                    screen.blit (oimg,(200,400))
                    dict1 [7] = 'O'
            if 200 < x < 400 and 400 < y < 600 and dict1 [8] == '':
                if turn % 2 == 0:
                    screen.blit (ximg,(200,400))
                    pygame.display.update ()
                    dict1 [8] = 'X'
                else:
                    screen.blit (oimg,(200,400))
                    pygame.display.update ()
                    dict1 [8] = 'O'
            if 400 < x < 600 and 400 < y < 600 and dict1 [9] == '':
                if turn % 2 == 0:
                    screen.blit (ximg,(400,400))
                    pygame.display.update ()
                    dict1 [9] = 'X'
                else:
                    screen.blit (oimg,(400,400))
                    pygame.display.update ()
                    dict1 [9] = 'O'
            turn = turn + 1
            print (dict1,turn)
    if dict1[1] == dict1[2] == dict1[3] != '':
        text (dict1[1] + ' Wins',300,300,(0,255,0))
        pygame.display.update ()
        break
    if dict1[1] == dict1[4] == dict1[7] != '':
        text (dict1[1] + ' Wins',300,300,(0,255,0))
        pygame.display.update ()
        break
    if dict1[1] == dict1[5] == dict1[9] != '':
        text (dict1[1] + ' Wins',300,300,(0,255,0))
        pygame.display.update ()
        break
    if dict1[2] == dict1[5] == dict1[8] != '':
        text (dict1[2] + ' Wins',300,300,(0,255,0))
        pygame.display.update ()
        break
    if dict1[3] == dict1[6] == dict1[9] != '':
        text (dict1[3] + ' Wins',300,300,(0,255,0))
        pygame.display.update ()
        break
    if dict1[4] == dict1[5] == dict1[6] != '':
        text (dict1[4] + ' Wins',300,300,(0,255,0))
        pygame.display.update ()
        break
    if dict1[7] == dict1[8] == dict1[9] != '':
        text (dict1[7] + ' Wins',300,300,(0,255,0))
        pygame.display.update ()
        break
    if dict1[3] == dict1[5] == dict1[7] != '':
        text (dict1[3] + ' Wins',300,300,(0,255,0))
        pygame.display.update ()
        break
    if dict1[1] != '' and dict1[2] != '' and dict1[3] != '' and dict1[4] != '' and dict1[5] != '' and dict1[6] != '' and dict1[7] != '' and dict1[8] != '' and dict1[9] != '':
        text ('Tie!',300,300,(0,0,255))
        pygame.display.update ()
        break
    pygame.display.update ()
