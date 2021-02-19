from graphics import *
from DeckClass import Deck
from CardClass import Cards

class Piles:
    '''Is responsible for setting up the starting piles of the game. Also checks 
    which pile was clicked, moves cards, moves card piles and checks if any of the 
    piles have a completed set of cards.'''

    def __init__(self, deck, win):
        '''Receives a shuffled deck and sets up the starting piles of the game.'''
        start_x = 50
        start_y = 250
        pile_spacing = 50
        pile_spacing1 = 75
        width = 100
        foundation_step = width + pile_spacing
        foundation_start_x = 1100 -  (foundation_step * 4)
        self.order = {None:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9, 9:10, 10:11, 11:12, 12:13, 13:None}
        self.color_order = {'red':'black', 'black':'red'}
        self.color_orderN = {'red':None, 'black':None}
        self.c1 = []
        self.c2 = []
        self.c3 = []
        self.c4 = []
        self.c5 = []
        self.c6 = []
        self.c7 = []
        self.s = []
        self.w = []
        self.f1 = []
        self.f2 = []
        self.f3 = []
        self.f4 = []

        column7 = [deck.getCard(), deck.getCard(), deck.getCard(), deck.getCard(), deck.getCard(), deck.getCard(), deck.getCard()]
        for i in range(7):
            if i == 6:
                column7[i].show()
            column7[i].draw(win, Point(start_x + width * 6 + pile_spacing * 6, start_y + i * 35))
            self.c7.append(column7[i])
        column6 = [deck.getCard(), deck.getCard(), deck.getCard(), deck.getCard(), deck.getCard(), deck.getCard()]
        for i in range(6):
            if i == 5:
                column6[i].show()
            column6[i].draw(win, Point(start_x + width * 5 + pile_spacing * 5, start_y + i * 35))
            self.c6.append(column6[i])
        column5 = [deck.getCard(), deck.getCard(), deck.getCard(), deck.getCard(), deck.getCard()]
        for i in range(5):
            if i == 4:
                column5[i].show()
            column5[i].draw(win, Point(start_x + width * 4 + pile_spacing * 4, start_y + i * 35))
            self.c5.append(column5[i])
        column4 = [deck.getCard(), deck.getCard(), deck.getCard(), deck.getCard()]
        for i in range(4):
            if i == 3:
                column4[i].show()
            column4[i].draw(win, Point(start_x + width * 3 + pile_spacing * 3, start_y + i * 35))
            self.c4.append(column4[i])
        column3 = [deck.getCard(), deck.getCard(), deck.getCard()]
        for i in range(3):
            if i == 2:
                column3[i].show()
            column3[i].draw(win, Point(start_x + width * 2 + pile_spacing * 2, start_y + i * 35))
            self.c3.append(column3[i])
        column2 = [deck.getCard(), deck.getCard()]
        for i in range(2):
            if i == 1:
                column2[i].show()
            column2[i].draw(win, Point(start_x + width + pile_spacing, start_y + i * 35))
            self.c2.append(column2[i])
        column1 = [deck.getCard()]
        for i in range(1):
            if i == 0:
                column1[i].show()
            column1[i].draw(win, Point(50, 250))
            self.c1.append(column1[i])

        stock = []
        for i in range(24):
            stock.append(deck.getCard())
        for i in range(24):
            stock[i].draw(win, Point(start_x, pile_spacing1))
            self.s.append(stock[i])


    def pile_clicked(self, p):
        '''Verifies which pile of cards was click and returns the clicked pile of cards.'''
        if 0 < p.getX() < 100 and 175 < p.getY() < 800:
            return self.c1
        elif 150 < p.getX() < 250 and 175 < p.getY() < 800:
            return self.c2
        elif 300 < p.getX() < 400 and 175 < p.getY() < 800:
            return self.c3
        elif 450 < p.getX() < 550 and 175 < p.getY() < 800:
            return self.c4
        elif 600 < p.getX() < 700 and 175 < p.getY() < 800:
            return self.c5
        elif 750 < p.getX() < 850 and 175 < p.getY() < 800:
            return self.c6
        elif 900 < p.getX() < 1000 and 175 < p.getY() < 800:
            return self.c7
        elif 0 < p.getX() < 100 and 0 < p.getY() < 150:
            return self.s
        elif 150 < p.getX() < 250 and 0 < p.getY() < 150:
            return self.w
        elif 450 < p.getX() < 550 and 0 < p.getY() < 150:
            return self.f1
        elif 600 < p.getX() < 700 and 0 < p.getY() < 150:
            return self.f2
        elif 750 < p.getX() < 950 and 0 < p.getY() < 150:
            return self.f3
        elif 900 < p.getX() < 1000 and 0 < p.getY() < 150:
            return self.f4

    def pile_clickedN(self, p):
        '''Verifies which pile of cards was click and returns the clicked pile of cards and the name of the pile of cards.'''
        if 0 < p.getX() < 100 and 175 < p.getY() < 800:
            return self.c1, 'c1'
        elif 150 < p.getX() < 250 and 175 < p.getY() < 800:
            return self.c2, 'c2'
        elif 300 < p.getX() < 400 and 175 < p.getY() < 800:
            return self.c3, 'c3'
        elif 450 < p.getX() < 550 and 175 < p.getY() < 800:
            return self.c4, 'c4'
        elif 600 < p.getX() < 700 and 175 < p.getY() < 800:
            return self.c5, 'c5'
        elif 750 < p.getX() < 850 and 175 < p.getY() < 800:
            return self.c6, 'c6'
        elif 900 < p.getX() < 1000 and 175 < p.getY() < 800:
            return self.c7, 'c7'
        elif 0 < p.getX() < 100 and 0 < p.getY() < 150:
            return self.s, 's'
        elif 150 < p.getX() < 250 and 0 < p.getY() < 150:
            return self.w, 'w'
        elif 450 < p.getX() < 550 and 0 < p.getY() < 150:
            return self.f1, 'f1'
        elif 600 < p.getX() < 700 and 0 < p.getY() < 150:
            return self.f2, 'f2'
        elif 750 < p.getX() < 950 and 0 < p.getY() < 150:
            return self.f3, 'f3'
        elif 900 < p.getX() < 1000 and 0 < p.getY() < 150:
            return self.f4, 'f4'

    def getCardPile(self, c_pile, p):
        '''Verifies which card was clicked and then returns a pile of cards.'''
        cardpile = []
        card = Cards(1, 'c')
        card.emptyCard()
        c_pile.reverse()
        for i in range(len(c_pile)):
            if (c_pile[i].clickedTop(p) or c_pile[i].clicked(p)) and c_pile[i].getFU():
                for j in range(i+1):
                    cardpile.append(c_pile[j])
                break
        c_pile.reverse()
        cardpile.reverse()
        return cardpile
        


    
    def moveCardPile(self, card_pile, mouse_click, old_pile, win):
        '''Moves a pile of cards from one pile to another pile.'''
        card = card_pile[0]
        pile, pile_name = self.pile_clickedN(mouse_click)
        if len(pile) == 0:
            rank = None
            color = None
        else:
            rank = pile[-1].getRank()
            color = pile[-1].getColor()

        if pile_name == 'c1' and self.order[card.getRank()] == rank and (self.color_order[card.getColor()] == color or self.color_orderN[card.getColor()] == color):
            for i in range(len(card_pile)):
                card_pile[i].undraw()
                card_pile[i].draw(win, Point(50, 250 + (len(pile) * 35)))
                pile.append(card_pile[i])
            old_pile.reverse()
            del old_pile[0:len(card_pile)]
            old_pile.reverse()
            if len(old_pile) != 0 :
                old_pile[-1].undraw()
                old_pile[-1].show()
                old_pile[-1].draw(win, old_pile[-1].getPOS())
            card_pile.clear()
        elif pile_name == 'c2' and self.order[card.getRank()] == rank and (self.color_order[card.getColor()] == color or self.color_orderN[card.getColor()] == color):
            for i in range(len(card_pile)):
                card_pile[i].undraw()
                card_pile[i].draw(win, Point(200, 250 + (len(pile) * 35)))
                pile.append(card_pile[i])
            old_pile.reverse()
            del old_pile[0:len(card_pile)]
            old_pile.reverse()
            if len(old_pile) != 0 :
                old_pile[-1].undraw()
                old_pile[-1].show()
                old_pile[-1].draw(win, old_pile[-1].getPOS())
            card_pile.clear()
        elif pile_name == 'c3' and self.order[card.getRank()] == rank and (self.color_order[card.getColor()] == color or self.color_orderN[card.getColor()] == color):
            for i in range(len(card_pile)):
                card_pile[i].undraw()
                card_pile[i].draw(win, Point(350, 250 + (len(pile) * 35)))
                pile.append(card_pile[i])
            old_pile.reverse()
            del old_pile[0:len(card_pile)]
            old_pile.reverse()
            if len(old_pile) != 0 :
                old_pile[-1].undraw()
                old_pile[-1].show()
                old_pile[-1].draw(win, old_pile[-1].getPOS())
            card_pile.clear()
        elif pile_name == 'c4' and self.order[card.getRank()] == rank and (self.color_order[card.getColor()] == color or self.color_orderN[card.getColor()] == color):
            for i in range(len(card_pile)):
                card_pile[i].undraw()
                card_pile[i].draw(win, Point(500, 250 + (len(pile) * 35)))
                pile.append(card_pile[i])
            old_pile.reverse()
            del old_pile[0:len(card_pile)]
            old_pile.reverse()
            if len(old_pile) != 0 :
                old_pile[-1].undraw()
                old_pile[-1].show()
                old_pile[-1].draw(win, old_pile[-1].getPOS())
            card_pile.clear()
        elif pile_name == 'c5' and self.order[card.getRank()] == rank and (self.color_order[card.getColor()] == color or self.color_orderN[card.getColor()] == color):
            for i in range(len(card_pile)):
                card_pile[i].undraw()
                card_pile[i].draw(win, Point(650, 250 + (len(pile) * 35)))
                pile.append(card_pile[i])
            old_pile.reverse()
            del old_pile[0:len(card_pile)]
            old_pile.reverse()
            if len(old_pile) != 0 :
                old_pile[-1].undraw()
                old_pile[-1].show()
                old_pile[-1].draw(win, old_pile[-1].getPOS())
            card_pile.clear()
        elif pile_name == 'c6' and self.order[card.getRank()] == rank and (self.color_order[card.getColor()] == color or self.color_orderN[card.getColor()] == color):
            for i in range(len(card_pile)):
                card_pile[i].undraw()
                card_pile[i].draw(win, Point(800, 250 + (len(pile) * 35)))
                pile.append(card_pile[i])
            old_pile.reverse()
            del old_pile[0:len(card_pile)]
            old_pile.reverse()
            if len(old_pile) != 0 :
                old_pile[-1].undraw()
                old_pile[-1].show()
                old_pile[-1].draw(win, old_pile[-1].getPOS())
            card_pile.clear()
        elif pile_name == 'c7' and self.order[card.getRank()] == rank and (self.color_order[card.getColor()] == color or self.color_orderN[card.getColor()] == color):
            for i in range(len(card_pile)):
                card_pile[i].undraw()
                card_pile[i].draw(win, Point(950, 250 + (len(pile) * 35)))
                pile.append(card_pile[i])
            old_pile.reverse()
            del old_pile[0:len(card_pile)]
            old_pile.reverse()
            if len(old_pile) != 0 :
                old_pile[-1].undraw()
                old_pile[-1].show()
                old_pile[-1].draw(win, old_pile[-1].getPOS())
            card_pile.clear()
        elif pile_name == 'f1' and self.order[card.getRank()] == rank and (self.color_order[card.getColor()] == color or self.color_orderN[card.getColor()] == color):
            for i in range(len(card_pile)):
                card_pile[i].undraw()
                card_pile[i].draw(win, Point(500, 75))
                pile.append(card_pile[i])
            old_pile.reverse()
            del old_pile[0:len(card_pile)]
            old_pile.reverse()
            if len(old_pile) != 0 :
                old_pile[-1].undraw()
                old_pile[-1].show()
                old_pile[-1].draw(win, old_pile[-1].getPOS())
            card_pile.clear()
        elif pile_name == 'f2' and self.order[card.getRank()] == rank and (self.color_order[card.getColor()] == color or self.color_orderN[card.getColor()] == color):
            for i in range(len(card_pile)):
                card_pile[i].undraw()
                card_pile[i].draw(win, Point(650, 75))
                pile.append(card_pile[i])
            old_pile.reverse()
            del old_pile[0:len(card_pile)]
            old_pile.reverse()
            if len(old_pile) != 0 :
                old_pile[-1].undraw()
                old_pile[-1].show()
                old_pile[-1].draw(win, old_pile[-1].getPOS())
            card_pile.clear()
        elif pile_name == 'f3' and self.order[card.getRank()] == rank and (self.color_order[card.getColor()] == color or self.color_orderN[card.getColor()] == color):
            for i in range(len(card_pile)):
                card_pile[i].undraw()
                card_pile[i].draw(win, Point(800, 75))
                pile.append(card_pile[i])
            old_pile.reverse()
            del old_pile[0:len(card_pile)]
            old_pile.reverse()
            if len(old_pile) != 0 :
                old_pile[-1].undraw()
                old_pile[-1].show()
                old_pile[-1].draw(win, old_pile[-1].getPOS())
            card_pile.clear()
        elif pile_name == 'f4' and self.order[card.getRank()] == rank and (self.color_order[card.getColor()] == color or self.color_orderN[card.getColor()] == color):
            for i in range(len(card_pile)):
                card_pile[i].undraw()
                card_pile[i].draw(win, Point(950, 75))
                pile.append(card_pile[i])
            old_pile.reverse()
            del old_pile[0:len(card_pile)]
            old_pile.reverse()
            if len(old_pile) != 0 :
                old_pile[-1].undraw()
                old_pile[-1].show()
                old_pile[-1].draw(win, old_pile[-1].getPOS())
            card_pile.clear()
        
    def checkPiles(self, win):
        '''Calls all the other functions responsible for verifying if there is a completed set.'''
        self.checkC1(win)
        self.checkC2(win)
        self.checkC3(win)
        self.checkC4(win)
        self.checkC5(win)
        self.checkC6(win)
        self.checkC7(win)
    
    def checkC1(self, win):
        '''Verifies if there is a completed set of cards in column number 1 and then moves to an empty foundation.'''
        num = 1
        c_pile = []
        found1 = Point(500, 75)
        self.c1.reverse()
        for item in self.c1:
            if item.getRank() == num and item.getFU():
                c_pile.append(item)
                if num == 13:
                    break
            else:
                c_pile.clear()
                break
            num = num + 1
        self.c1.reverse()
        c_pile.reverse()
        if len(self.f1) == 0 and len(c_pile) == 13:
            self.moveCardPile(c_pile, found1, self.c1, win)
        elif len(self.f2) == 0 and len(c_pile) == 13:
            self.moveCardPile(c_pile, Point(650, 75), self.c1, win)
        elif len(self.f3) == 0 and len(c_pile) == 13:
            self.moveCardPile(c_pile, Point(800, 75), self.c1, win)
        elif len(self.f4) == 0 and len(c_pile) == 13:
            self.moveCardPile(c_pile, Point(950, 75), self.c1, win)

    def checkC2(self, win):
        '''Verifies if there is a completed set of cards in column number 2 and then moves to an empty foundation.'''
        num = 1
        card_pile = []
        self.c2.reverse()
        for item in self.c2:
            if item.getRank() == num and item.getFU():
                card_pile.append(item)
                if num == 13:
                    break
            else:
                card_pile.clear()
                break
            num = num + 1
        self.c2.reverse()
        card_pile.reverse()
        if len(self.f1) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(500, 75), self.c2, win)
        elif len(self.f2) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(650, 75), self.c2, win)
        elif len(self.f3) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(800, 75), self.c2, win)
        elif len(self.f4) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(950, 75), self.c2, win)
    
    def checkC3(self, win):
        '''Verifies if there is a completed set of cards in column number 3 and then moves to an empty foundation.'''
        num = 1
        card_pile = []
        self.c3.reverse()
        for item in self.c3:
            if item.getRank() == num and item.getFU():
                card_pile.append(item)
                if num == 13:
                    break
            else:
                card_pile.clear()
                break
            num = num + 1
        self.c3.reverse()
        card_pile.reverse()
        if len(self.f1) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(500, 75), self.c3, win)
        elif len(self.f2) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(650, 75), self.c3, win)
        elif len(self.f3) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(800, 75), self.c3, win)
        elif len(self.f4) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(950, 75), self.c3)

    def checkC4(self, win):
        '''Verifies if there is a completed set of cards in column number 4 and then moves to an empty foundation.'''
        num = 1
        card_pile = []
        self.c4.reverse()
        for item in self.c4:
            if item.getRank() == num and item.getFU():
                card_pile.append(item)
                if num == 13:
                    break
            else:
                card_pile.clear()
                break
            num = num + 1
        self.c4.reverse()
        card_pile.reverse()
        if len(self.f1) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(500, 75), self.c4, win)
        elif len(self.f2) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(650, 75), self.c4, win)
        elif len(self.f3) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(800, 75), self.c4, win)
        elif len(self.f4) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(950, 75), self.c4, win)

    def checkC5(self, win):
        '''Verifies if there is a completed set of cards in column number 5 and then moves to an empty foundation.'''
        num = 1
        card_pile = []
        self.c5.reverse()
        for item in self.c5:
            if item.getRank() == num and item.getFU():
                card_pile.append(item)
                if num == 13:
                    break
            else:
                card_pile.clear()
                break
            num = num + 1
        self.c5.reverse()
        card_pile.reverse()
        if len(self.f1) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(500, 75), self.c5, win)
        elif len(self.f2) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(650, 75), self.c5, win)
        elif len(self.f3) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(800, 75), self.c5, win)
        elif len(self.f4) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(950, 75), self.c5, win)

    def checkC6(self, win):
        '''Verifies if there is a completed set of cards in column number 6 and then moves to an empty foundation.'''
        num = 1
        card_pile = []
        self.c6.reverse()
        for item in self.c6:
            if item.getRank() == num and item.getFU():
                card_pile.append(item)
                if num == 13:
                    break
            else:
                card_pile.clear()
                break
            num = num + 1
        self.c6.reverse()
        card_pile.reverse()
        if len(self.f1) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(500, 75), self.c6, win)
        elif len(self.f2) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(650, 75), self.c6, win)
        elif len(self.f3) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(800, 75), self.c6, win)
        elif len(self.f4) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(950, 75), self.c6, win)

    def checkC7(self, win):
        '''Verifies if there is a completed set of cards in column number 7 and then moves to an empty foundation.'''
        num = 1
        card_pile = []
        self.c7.reverse()
        for item in self.c7:
            if item.getRank() == num and item.getFU():
                card_pile.append(item)
                if num == 13:
                    break
            else:
                card_pile.clear()
                break
            num = num + 1
        self.c7.reverse()
        card_pile.reverse()
        if len(self.f1) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(500, 75), self.c7, win)
        elif len(self.f2) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(650, 75), self.c7, win)
        elif len(self.f3) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(800, 75), self.c7, win)
        elif len(self.f4) == 0 and len(card_pile) == 13:
            self.moveCardPile(card_pile, Point(950, 75), self.c7, win)
    
    def moveStock(self, win):
        '''Moves cards from the stock to waste and when there are no more cards it moves them back to stock.'''
        if len(self.s) != 0:
            card = self.s.pop(-1)
            card.undraw()
            card.show()
            card.draw(win, Point(200, 75))
            self.w.append(card)
        else:
            self.w.reverse()
            for i in range(len(self.w)):
                self.w[i].undraw()
                self.w[i].hide()
                self.w[i].draw(win, Point(50,75))
                self.s.append(self.w[i])
            self.w.clear()

    def GameOver(self):
        '''Verifies if the game is over and returns True or False.'''
        if len(self.c1) == 0 and len(self.c2) == 0 and len(self.c3) == 0 and len(self.c4) == 0 and len(self.c5) == 0 and len(self.c6) == 0 and len(self.c7) == 0:
            return True
        else:
            return False
