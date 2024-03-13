import pygame
import random
import time
from SpaceInv_L1 import lvl1
from SpaceInv_L2 import lvl2
from SpaceInv_L3 import lvl3
pygame.init ()
from pygame.locals import *

level = 1
wincond = 'lose'
while True:
    while level == 1 and wincond == 'lose':
        wincond = lvl1 ()
        if wincond == 'lose':
            response = input ('Try again? [Y/N] - ')
            if response == 'N':
                wincond = 'pass'
    wincond = 'lose'
    level += 1
    while level == 2 and wincond == 'lose':
        wincond = lvl2 ()
        if wincond == 'lose':
            response = input ('Try again? [Y/N] - ')
            if response == 'N':
                wincond = 'pass'
    wincond = 'lose'
    level += 1
    while level == 3 and wincond == 'lose': #has some problem with font
        wincond = lvl3 ()
        if wincond == 'lose':
            response = input ('Try again? [Y/N] - ')
            if response == 'N':
                wincond = 'pass'
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
    pygame.display.update ()
