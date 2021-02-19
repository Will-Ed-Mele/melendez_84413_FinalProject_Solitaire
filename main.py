from graphics import *
from Solitaire import Solitaire

def main():
    win = GraphWin("Solitaire", 1100, 800)
    win.setBackground('green')
    g = Solitaire(win)
    win.close()

main()