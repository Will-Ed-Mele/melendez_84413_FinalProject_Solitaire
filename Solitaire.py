from graphics import *
from button import Button
from PileClass import Piles
from DeckClass import Deck


class Solitaire:
    '''Class responsible for running the game, setting up 
    the black rectangles that mark where the cards go, 
    generating the menu and instructions.'''
    def __init__(self, win):
        '''The game is set up and waits for the user input to complete actions'''
        self.menu(win)
        self.set_up(win)
        d = Deck()
        d.shuffle_deck()
        d.shuffle_deck()
        p = Piles(d, win)

        while True:
            key = win.getKey()
            if key == 's':
                p.moveStock(win)
            elif key == 'm':
                m = win.getMouse()
                pile = p.pile_clicked(m)
                card_pile = p.getCardPile(pile, m)
                moveto = win.getMouse()
                p.moveCardPile(card_pile, moveto, pile, win)
            elif key == 'q':
                break
            p.checkPiles(win)
            game = p.GameOver()
            self.Winner(game, win)
            if game:
                while True:
                    end_key = win.checkKey()
                    self.you_win.setTextColor('black')
                    self.you_win.setTextColor('red')
                    if end_key == 'q':
                        break
            


    def set_up(self, win):
        '''Sets up the black rectangles that show where the cards are placed'''
        for i in range(4):
            f = Rectangle(Point(550 + 150 * i, 0), Point(450 + 150 * i, 150))
            f.setFill('green')
            f.setOutline('black')
            f.draw(win)
        for i in range(7):
            c = Rectangle(Point(100 + i * 150, 175), Point(0 + i * 150, 325))
            c.setFill('green')
            c.setOutline('black')
            c.draw(win)
        for i in range(2):
            sw = Rectangle(Point(100 + i * 150, 0), Point(0 + i * 150, 150))
            sw.setFill('green')
            sw.setOutline('black')
            sw.draw(win)
    
    def menu(self, win):
        '''Sets up he start menu which displays the game name and two buttons, 
        one button to start the game and another to exit the game. Waits for the 
        user to click one of the buttons'''

        message = Text(Point(550, 300), 'Solitaire')
        message.setFace('helvetica')
        message.setSize(35)
        message.draw(win)
        instructions = Text(Point(550, 345), "Press 's' to move the stock" + '\n' + "Press 'm' then click the card you want to move, afterwards click where you want to move it" + '\n' + "Press 'q' to exit the game")
        instructions.setFace('helvetica')
        instructions.draw(win)
        heart = Text(Point(50, 50), '♥')
        heart.setSize(35)
        heart.setTextColor('red')
        heart.draw(win)
        club = Text(Point(50, 750), '♣')
        club.setSize(35)
        club.setTextColor('black')
        club.draw(win)
        spade = Text(Point(1050, 50), '♠')
        spade.setSize(35)
        spade.setTextColor('black')
        spade.draw(win)
        diamond = Text(Point(1050, 750), '♦')
        diamond.setSize(35)
        diamond.setTextColor('red')
        diamond.draw(win)
        self.play = Button(win, Point(550, 400), 100, 50, 'Play')
        self.play.activate()
        self.quit =Button(win, Point(550, 475), 100, 50, 'Quit')
        self.quit.activate()

        while True:
            start = win.getMouse()
            if self.play.clicked(start):
                message.undraw()
                self.play.undraw()
                self.quit.undraw()
                heart.undraw()
                club.undraw()
                spade.undraw()
                diamond.undraw()
                instructions.move(0,400)
                break
            elif self.quit.clicked(start):
                win.close()
                break

    def Winner(self, game_status, win):
        '''Displays a you win text when the player wins the game.'''
        if game_status:
            self.you_win = Text(Point(550, 400), 'YOU WIN!!!')
            self.you_win.setSize(35)
            self.you_win.setFace('helvetica')
            self.you_win.setTextColor('red')
            self.you_win.draw(win)
