def card_img(suit, rank):
    '''Verifies the rank and suit of the card and returns the 
    image that corresponds to that card.'''
    if suit == 'c' or suit == 'C':
        if rank == 1:
            return 'Cards/AC.png'
        elif rank == 2:
            return 'Cards/2C.png'
        elif rank == 3:
            return 'Cards/3C.png'
        elif rank == 4:
            return 'Cards/4C.png'
        elif rank == 5:
            return 'Cards/5C.png'
        elif rank == 6:
            return 'Cards/6C.png'
        elif rank == 7:
            return 'Cards/7C.png'
        elif rank == 8:
            return 'Cards/8C.png'
        elif rank == 9:
            return 'Cards/9C.png'
        elif rank == 10:
            return 'Cards/10C.png'
        elif rank == 11:
            return 'Cards/JC.png'
        elif rank == 12:
            return 'Cards/QC.png'
        elif rank == 13:
            return 'Cards/KC.png'
    elif suit == 's' or suit == 'S':
        if rank == 1:
            return 'Cards/AS.png'
        elif rank == 2:
            return 'Cards/2S.png'
        elif rank == 3:
            return 'Cards/3S.png'
        elif rank == 4:
            return 'Cards/4S.png'
        elif rank == 5:
            return 'Cards/5S.png'
        elif rank == 6:
            return 'Cards/6S.png'
        elif rank == 7:
            return 'Cards/7S.png'
        elif rank == 8:
            return 'Cards/8S.png'
        elif rank == 9:
            return 'Cards/9S.png'
        elif rank == 10:
            return 'Cards/10S.png'
        elif rank == 11:
            return 'Cards/JS.png'
        elif rank == 12:
            return 'Cards/QS.png'
        elif rank == 13:
            return 'Cards/KS.png'
    elif suit == 'h' or suit == 'H':
        if rank == 1:
            return 'Cards/AH.png'
        elif rank == 2:
            return 'Cards/2H.png'
        elif rank == 3:
            return 'Cards/3H.png'
        elif rank == 4:
            return 'Cards/4H.png'
        elif rank == 5:
            return 'Cards/5H.png'
        elif rank == 6:
            return 'Cards/6H.png'
        elif rank == 7:
            return 'Cards/7H.png'
        elif rank == 8:
            return 'Cards/8H.png'
        elif rank == 9:
            return 'Cards/9H.png'
        elif rank == 10:
            return 'Cards/10H.png'
        elif rank == 11:
            return 'Cards/JH.png'
        elif rank == 12:
            return 'Cards/QH.png'
        elif rank == 13:
            return 'Cards/KH.png'
    elif suit == 'd' or suit == 'D':
        if rank == 1:
            return 'Cards/AD.png'
        elif rank == 2:
            return 'Cards/2D.png'
        elif rank == 3:
            return 'Cards/3D.png'
        elif rank == 4:
            return 'Cards/4D.png'
        elif rank == 5:
            return 'Cards/5D.png'
        elif rank == 6:
            return 'Cards/6D.png'
        elif rank == 7:
            return 'Cards/7D.png'
        elif rank == 8:
            return 'Cards/8D.png'
        elif rank == 9:
            return 'Cards/9D.png'
        elif rank == 10:
            return 'Cards/10D.png'
        elif rank == 11:
            return 'Cards/JD.png'
        elif rank == 12:
            return 'Cards/QD.png'
        elif rank == 13:
            return 'Cards/KD.png'

