import random
'''
    Init a new poker obj to setup the game
    call playSimpleGame to see an example run.

    ex:

        import poker.py
        my_game = Poker(5,500) // Start a 5 person game, at $500 ea
        my_game.playSimpleGame()

        then run the above in the python shell

    more to come. For now it will interactively play a game of poker,
    with the exception being that it WILL show ALL hands. No UI has 
    been built on top, and this software is intended to be used for
    teating various game conditions and outcomes. 


'''
class Card:
    def __init__(self, suit, rank): 
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{}".format(self.rank).ljust(2) + self.suit

class Deck:
    def __init__(self):
        '''
            Create a deck, or list, of 52 card objects.
        '''
        suits = ['H','D','S','C']
        ranks = ['A','2','3','4','5','6','7','8','9','10','J','K','Q']
        cards = []

        for s in suits:
            for r in ranks:
                cards.append(Card(s,r))
        self.cards = cards

    def drawHand(self, ammount):
        '''
        Draws a players hand and updates deck
        '''
        hand = []
        for i in range(0,ammount):
            rand = random.randint(1,len(self.cards) - 1)
            card_drawn = self.cards[rand]
            hand.append(card_drawn)
            self.cards.remove(card_drawn)
        return hand

class Poker:
    def __init__(self, num_players, starting_stack):
        self.num_players = num_players;
        self.starting_stack = starting_stack;

    def playSampleGame(self):
        '''
            Interactively play a game with the user
        '''

        deck = Deck()
        hands = []

        # Draw x hands
        for x in range(0,self.num_players):
            hand = deck.drawHand(2)
            hands.append(hand)

        # print hand values. Insert any templating in this area
        for hand in hands:
            print "\nPrinting hand for player\n"
            for card in hand:
                print(card)

        # flop up to 5 cards
        for i in range(0,3):

            if i==0:
                river = deck.drawHand(3)

            else:

                inp = raw_input('Would you like to flop another card? Hit Enter to continue, or hit any other key to stop')
                if inp in [None]:
                    river = river + deck.drawHand(1)

                else:
                    print "flip the cards"
                    break

            print "\nPrinting river\n"
            for card in river:
                print(card)

        inp = raw_input("dev_opts? [yn]")

        if inp in [None,'y']:
                inp = raw_input('Would you like to show deck? [yn]')
                if inp in [None,'y']:
                    print "\nPrinting updated deck\n"
                    for card in deck.cards:
                        print(card)



game = Poker(5,500)
game.playSampleGame()


    


    




