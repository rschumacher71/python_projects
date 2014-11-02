#!/usr/bin/env python
#

import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Cards by Rich Schumacher")

#Create a  background.
background = pygame.Surface((640,480))
background.fill((0,255,0))

#Load cards image
card_image = pygame.image.load('cards.gif')
CARD_WIDTH=71
CARD_HEIGHT=96

#Display A Card Function
#cardnum : 1 to 13 (1 = Ace, 13 = King)
#suit : 1 = Diamonds, 2 = Hearts, 3 = Clubs , 4 = Spades
#loc_x, loc_y : x,y coordinate on screen to place image
def display_a_card(cardnum, suit, loc_x, loc_y):
    card_to_show = pygame.Rect((cardnum * CARD_WIDTH, suit * CARD_HEIGHT),
                               (CARD_WIDTH, CARD_HEIGHT))
    screen.blit(card_image,(loc_x,loc_y),card_to_show)

#Initialize locals
number = 0
suit = 0

#clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri",40)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            flag = True            
        if event.type == KEYUP:
            if (event.key == K_UP) and (flag == True):
                number += 1
                flag = False
            elif (event.key == K_DOWN) and (flag == True):
                number -= 1
                flag = False
            if (event.key == K_RIGHT) and (flag == True):
                suit += 1
                flag = False
            elif (event.key == K_LEFT) and (flag == True):
                suit -= 1
                flag = False


    screen.blit(background,(0,0))
    display_a_card(number,suit,200,200)

    num = font.render('CARD ' + str(number), True,(255,255,255))
    screen.blit(num,(450.,210.))    

    suit_num = font.render('SUIT ' + str(suit), True,(255,255,255))
    screen.blit(suit_num,(450.,310.))
    pygame.display.update()
