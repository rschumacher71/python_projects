#!/usr/bin/env python
#

import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

screen=pygame.display.set_mode((1024,480),0,32)
pygame.display.set_caption("Cards by Rich Schumacher")

#Create a  background.
background = pygame.Surface((1024,480))
background.fill((0,255,0))

class Card(pygame.sprite.Sprite):
    card_image = pygame.image.load('cards.gif')
    CARD_WIDTH=71
    CARD_HEIGHT=96

# Constructor. Pass in the color of the block,
# and its x and y position
    def __init__(self, cardnum, x_pos, y_pos):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([CARD_WIDTH, CARD_HEIGHT])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()



#Display A Card Function
#cardnum : 0:12 = Ace to King, Hearts, 13:25 = Hearts, 25:38 = Clubs, 39:51 = Spades
#loc_x, loc_y : x,y coordinate on screen to place image
def display_a_card(cardnum, loc_x, loc_y):
    cardnum = cardnum % 52
    suit = int(cardnum/13)
    cardnum = cardnum % 13
    card_to_show = pygame.Rect((cardnum * CARD_WIDTH, suit * CARD_HEIGHT),
                               (CARD_WIDTH, CARD_HEIGHT))
    screen.blit(card_image,(loc_x,loc_y),card_to_show)

#Initialize locals
number = 0
suit = 0

#clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri",40)

#Create a Deck 0..51
myDeck = list(range(52))
spacing = CARD_WIDTH

#Shuffle Deck
def shuffle():
    effect = pygame.mixer.Sound('shuffling-cards-1.wav')
    effect.play()

def display_deck(deck):
    xpos = 0
    ypos = 0

    for j in range(4):
        for i in range(13):
            display_a_card(deck[i+j+j*12], xpos, ypos)
            xpos += spacing
        xpos = 0
        ypos += CARD_HEIGHT

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            flag = True            
        if event.type == KEYUP:
            if (event.key == K_s) and (flag == True):
                random.shuffle(myDeck)
                shuffle()
                flag = False
            if (event.key == K_d) and (flag == True):
                spacing /= 2
                flag = False
            if (event.key == K_i) and (flag == True):
                spacing *= 2
                flag = False

    screen.blit(background,(0,0))
    display_deck(myDeck)
    text = font.render('Hit S to Shuffle', True,(0,0,0))
    screen.blit(text,(250,410))
    text2 = font.render('Hit i or d to change spacing', True,(0,0,0))
    screen.blit(text2,(250,440))
                      
    pygame.display.update()
