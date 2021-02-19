from CardClass import Cards

class ColorCard(Cards):
    '''Changes the image that is assigned to the card.'''
    def setCardImage(self, rank, suit):
        self.rank = rank
        self.suit = suit
        Cards.imageC(suit, rank)

