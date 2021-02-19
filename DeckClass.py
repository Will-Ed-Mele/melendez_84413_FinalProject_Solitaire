from CardClass import Cards
import random

class Deck:
    '''Responsible for making a deck of cards, can shuffle the deck, 
    get a card from the deck and verify if the deck is empty.'''

    def __init__(self):
        '''Generates an organized deck of cards.'''
        self.cards = []
        suits = ['c', 'd', 'h', 's']
        ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        for suit in suits:
            for rank in ranks:
                card = Cards(rank, suit)
                self.cards.append(card)
    
    def shuffle_deck(self):
        '''Shuffles the deck of cards.'''
        random.shuffle(self.cards)

    def getCard(self):
        '''Retruns a card and removes it from the deck.'''
        if len(self.cards) > 0:
            return self.cards.pop()
    
    def isEmpty(self):
        '''Returns True if the deck is empty.'''
        return len(self.cards) <= 0
