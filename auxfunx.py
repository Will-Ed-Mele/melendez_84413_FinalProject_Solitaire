def card_img(suit, rank):
    '''Verifies the rank and suit of the card and returns the 
    image that corresponds to that card.'''
    if suit == 'c' or suit == 'C':
        if rank == 1:
            return 'AC.png'
        elif rank == 2:
            return '2C.png'
        elif rank == 3:
            return '3C.png'
        elif rank == 4:
            return '4C.png'
        elif rank == 5:
            return '5C.png'
        elif rank == 6:
            return '6C.png'
        elif rank == 7:
            return '7C.png'
        elif rank == 8:
            return '8C.png'
        elif rank == 9:
            return '9C.png'
        elif rank == 10:
            return '10C.png'
        elif rank == 11:
            return 'JC.png'
        elif rank == 12:
            return 'QC.png'
        elif rank == 13:
            return 'KC.png'
    elif suit == 's' or suit == 'S':
        if rank == 1:
            return 'AS.png'
        elif rank == 2:
            return '2S.png'
        elif rank == 3:
            return '3S.png'
        elif rank == 4:
            return '4S.png'
        elif rank == 5:
            return '5S.png'
        elif rank == 6:
            return '6S.png'
        elif rank == 7:
            return '7S.png'
        elif rank == 8:
            return '8S.png'
        elif rank == 9:
            return '9S.png'
        elif rank == 10:
            return '10S.png'
        elif rank == 11:
            return 'JS.png'
        elif rank == 12:
            return 'QS.png'
        elif rank == 13:
            return 'KS.png'
    elif suit == 'h' or suit == 'H':
        if rank == 1:
            return 'AH.png'
        elif rank == 2:
            return '2H.png'
        elif rank == 3:
            return '3H.png'
        elif rank == 4:
            return '4H.png'
        elif rank == 5:
            return '5H.png'
        elif rank == 6:
            return '6H.png'
        elif rank == 7:
            return '7H.png'
        elif rank == 8:
            return '8H.png'
        elif rank == 9:
            return '9H.png'
        elif rank == 10:
            return '10H.png'
        elif rank == 11:
            return 'JH.png'
        elif rank == 12:
            return 'QH.png'
        elif rank == 13:
            return 'KH.png'
    elif suit == 'd' or suit == 'D':
        if rank == 1:
            return 'AD.png'
        elif rank == 2:
            return '2D.png'
        elif rank == 3:
            return '3D.png'
        elif rank == 4:
            return '4D.png'
        elif rank == 5:
            return '5D.png'
        elif rank == 6:
            return '6D.png'
        elif rank == 7:
            return '7D.png'
        elif rank == 8:
            return '8D.png'
        elif rank == 9:
            return '9D.png'
        elif rank == 10:
            return '10D.png'
        elif rank == 11:
            return 'JD.png'
        elif rank == 12:
            return 'QD.png'
        elif rank == 13:
            return 'KD.png'

