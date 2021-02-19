from graphics import *
from auxfunx import card_img
import random


class Cards:
    '''Creates a card with a rank and suit. Assigns the image that corresponds 
    to the card and sets the card face down. Also assigns a color depending on 
    the suit of the card.'''

    def __init__(self, rank, suit, face_up = False):
        '''Creates a card with a rank and suit. Assigns the image that corresponds 
        to the card and sets the card face down. Also assigns a color depending on 
        the suit of the card.'''

        self.rank = rank
        self.suit = suit
        self.face_up = face_up
        self.imagename = self.imageC(suit, rank)
        self.drawn = False
        if self.suit == 'c' or self.suit == 's':
            self.color = 'black'
        elif self.suit == 'h' or self.suit == 'd':
            self.color = 'red'

    def getRank(self):
        '''Returns the rank or number of the card.'''
        return self.rank
    
    def getSuit(self):
        '''Returns the suit of the card.'''
        return self.suit

    def getImage(self):
        '''Returns the image object of the card'''
        return self.image

    def getColor(self):
        '''Returns the color of the card.'''
        return self.color

    def getPOS(self):
        '''Returns the position of the card after it is placed.'''
        return self.pos

    def getFU(self):
        '''Returns if the card is face up or face down.'''
        return self.face_up

    def show(self):
        '''Sets the card face up.'''
        self.face_up = True

    def hide(self):
        '''Sets the card face down.'''
        self.face_up = False

    def imageC(self, suit, rank):
        '''Assigns an image to the card depending on if it is face up or face down.'''
        if self.face_up == True:
            return card_img(suit, rank)
        elif self.face_up == False:
            return 'card_back.png'

    def value(self):
        '''Returns the cards value.'''
        if self.getRank() == 1:
            return "Ace"
        elif self.getRank() == 11:
            return "Jack"
        elif self.getRank() == 12:
            return "Queen"
        elif self.getRank() == 13:
            return "King"
        else:
            return self.getRank()

    def clicked(self, mouse_pos):
        '''Returns if the card was clicked on any spot.'''
        if self.pos.getX() - 50 < mouse_pos.getX() < self.pos.getX() + 50 and self.pos.getY() - 75 < mouse_pos.getY() < self.pos.getY() + 75:
            return True
        else:
            return False
    
    def clickedTop(self, mouse_pos):
        '''Returns if the card was clicked on the top of the card. Used when the card is not infront of the pile of cards.'''
        if self.pos.getX() - 50 < mouse_pos.getX() < self.pos.getX() + 50 and self.pos.getY() - 75 < mouse_pos.getY() < self.pos.getY() - 40:
            return True
        else:
            return False

    def ofSuit(self):
        '''Returns the suit of the card as a string.'''
        if self.getSuit() == 'c' or self.getSuit() == 'C':
            return ' of Clubs'
        elif self.getSuit() == 's' or self.getSuit() == 'S':
            return ' of Spades'
        elif self.getSuit() == 'h' or self.getSuit() == 'H':
            return ' of Hearts'
        elif self.getSuit() == 'd' or self.getSuit() == 'D':
            return ' of Diamonds'
    
    def __str__(self):
        '''Returns the name of the card.'''
        return str(self.value()) + self.ofSuit()
    

    def draw(self, win, center):
        '''Draws the card in a window at the given center point.'''
        self.imagename = self.imageC(self.suit, self.rank)
        self.image = Image(center, self.imagename)
        self.image.draw(win)
        self.pos = center
    
    def undraw(self):
        '''Undraws the card from the window.'''
        self.image.undraw()

    def emptyCard(self):
        '''Emties the card so that it has no value, rank, color, etc.'''
        self.rank = 0
        self.suit = None
        self.color = None

