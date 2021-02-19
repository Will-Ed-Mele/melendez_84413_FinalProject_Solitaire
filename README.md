# Final Project
This program is based off of the popular card game Solitaire. I recreated it to the best of my ability, only using the graphics.py module. Some of the more noticeable changes is that when you want to move a card or a pile of cards you have to press the key 'm' then click on the card you want to move, afterwards click where you want to move the card or pile of cards. Another change is that when you want to move the cards that go between stock and waste you have to press the key 's' and the cards automaticaly move. The game moves the completed set to the foundations automaticaly. If you want to exit from the game all you have to do is press the key 'q' and the game closes. The game also verifies if you won and displays a message on the screen.

# Algorithm
The program starts by displaying a window with the name of the game, some instructions and two buttons(play button and quit button). If you click the 'Quit' button the window will close. If you click the 'Play' button the game sets up black rectangles so the user knows where the cards go. Then it deletes the message and the buttons. After that is makes an object form the Deck class which is a 52 card deck and shuffles the deck twice using a function from the deck class. When the deck is shuffled twice it is then sent to the Piles class which places the cards in the window. After all the cards are placed, an infinite loop starts and depending on what key the user presses it does different actions. When the user presses the 's' key a function in the Piles class is called and moves cards from the stock pile to the waste pile and back to the stock pile. When the user presses the 'm' key the program will then wait for the user to click the card or card pile he wants to move, the mouse click is then sent to a function to verify which pile was clicked and to get the card or card pile from that pile, it then waits for another mouse click from the user and sends it to a function in the Piles class to verify if it's a valid move and after that is moves the card or pile of cards to the new pile and deletes them from the old pile or just doesn't move the cards if it is an invalid move. When the user presses the 'q' the window is closed.
