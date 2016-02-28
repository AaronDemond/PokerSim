import random
import string
import itertools
from exceptions import ValueError

class Card:
    def __init__(self, suit, rank): 
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{}".format(self.rank).ljust(2) + self.suit


    def getValue(self):
        '''
            Return a dict of possible numerical values of the card. Dict used
            because ace can cake high or low (1,14) 
        '''
        if self.rank in ['2','3','4','5','6','7','8','9','10']:
            return [int(self.rank)]
        else:
            if self.rank == 'A': return [1,14]
            elif self.rank == 'J': return [11]
            elif self.rank == 'Q': return [12]
            elif self.rank == 'K': return [13]

        

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
            Returns a list (hand) of two cards and updates deck
            by removing the cards from it
        '''
        hand = []
        for i in range(0,ammount):
            rand = random.randint(1,len(self.cards) - 1)
            card_drawn = self.cards[rand]
            hand.append(card_drawn)
            self.cards.remove(card_drawn)
        return hand

class Player:
    def __init__(self, name, starting_stack):
        self.name = name
        self.starting_stack = starting_stack

class Poker:


    def __init__(self, num_players, starting_stack):
        '''
            Setup a game, init must be called before other methods.
        '''
        self.num_players = num_players;
        self.players = []

        # Create a unique player, assign their starting cash and append to game
        for x in range(0,num_players):
            name = 'Player ' + string.uppercase[x]
            player = Player(name, starting_stack)
            self.players.append(player)


    
    @staticmethod
    def _isFlush(hand):
        suit = hand[0].suit
        for card in hand:
            if card.suit != suit:
                return False
        return True

    def getBestHand(self):

        curr_best = 11 #1 = Royal Flush - 10 = High card. 11 means nothing.

        did_happen = 0
        # loop through players, assign p_hands as a dict of all possible 5 card hands
        for player in self.players:
            card_pile = player.hand
            river = self.river
            for c in river:
                card_pile.append(c)
            player.p_hands = itertools.combinations(card_pile, 5)

            #check for each of 10 hands
            for hand in player.p_hands:
                if Poker._isFlush(hand):
                    print "flush for " + player.name

                ### following determins if a hand, or dict of cards, is a straight. ###

                suits = []
                ace_height = 0
                for card in hand:
                    suits.append(card.suit)
                if 'A' in suits and 'K' in suits:
                    ace_height = 1

                values = []
                for card in hand:
                    cur_v = card.getValue() #always returns a dict
                    if len(cur_v) > 1 and ace_height == 1: #if ace in hand, and ace high
                        cur_v = 14 #set int current card int value to 14
                    elif len(cur_v) > 1: # ace must otherwise be low (if present)
                        cur_v = 1
                    else:
                        cur_v = cur_v[0] # ace not in hand, return first val in dict

                    values.append(cur_v)


                # following tests if the values dict forms a straight
                sv = sorted(values)
                s = True
                for i in range(0,5):
                    expected = i + sv[0]
                    if expected != sv[i]:
                        s = False


                if s:
                    print "============================================================"
                    print "Straight for " + player.name  + "!!!!!!!!!!!!!!!!!!"
                    did_happen = 1



                
                print "==============printing hand and its values========="
                print player.name + "'s p-hand: "
                for card in hand:
                    print card
                print player.name + "'s values: "
                for v in values:
                    print v

                
                '''
                if _isRoyalFlush(hand):
                    print "royal flush for " + player.name
                if _isStraight(hand):
                    print "striaght for " player.name
                '''

        return did_happen


    def getHighestCard(self):
        '''
            Returns a dict containing the highest valued cards
        '''
        cur_max = None
        cur_max_cards = []
        for player in self.players:
            for card in player.hand:
                for v in card.getValue(): #Cards can have multiple values (Only ace, but it is coded to always return a dict)
                    if v == cur_max:
                        cur_max_cards.append(card)
                    elif v > cur_max:
                        cur_max = v
                        cur_max_cards = [card]

        return cur_max_cards
                    


    def printHands(self):
        '''
            Can be called at any time to print players hands
        '''
        for x in range(0,len(self.players)):
            player = self.players[x]
            print "Printing hand for " + player.name
            for card in player.hand:
                print(card)

    def playSampleGame(self):
        '''
            Interactively play a game with the user
        '''

        deck = Deck()
        hands = []

        # Draw x hands, assign to all players of class Poker
        for player in self.players:
            hand = deck.drawHand(2)
            player.hand = hand


        # Optionally reveal each hand (todo: combine with above)
        for player in self.players:
            inp = raw_input('Reveal' + player.name + "'s hand? [yn] ");
            if inp in ['y', 'Y']:
                print "Printing hand for " + player.name
                for card in player.hand:
                    print(card)

        # Optionally show all hands and the highest card dealt
        inp = raw_input('Show all hands and highest valued card? [yn]');
        if inp in ['y', 'Y']:
            self.printHands();
            highest_cards = self.getHighestCard()
            print "Printing Highest cards:"
            for hc in highest_cards:
                print(hc)



        # Interactive dealer
        inp = raw_input('Dealer ready. Flop river? [y][Enter]');
        if inp in ['y', 'Y', None, ""]:
            # Flop then flip no more then 2 additional cards
            for i in range(0,3):
                if i==0:
                    self.river = deck.drawHand(3)
                else:
                    inp = raw_input('Show another card? [y][Enter]')   # If the round ends, this loop breaks and it continues below.
                    if inp in ['y', 'Y', None, ""]:
                        self.river = self.river + deck.drawHand(1)
                    else:
                        print "Round over"
                        break
                print "=========== Printing river ========== "
                for card in self.river:
                    print(card)

        # Optionally show all possible hands for players
        inp = raw_input('Show all possible hands [y][Enter]');
        if inp in ['y', 'Y', None, ""]:
            did_happen = self.getBestHand()
            if did_happen:
                print "Straight occurred"
            print "Straight not occurred"

        # The game is now over. Show options

        inp = raw_input('Show all hands? [yn]')
        if inp in ['y', 'Y']:
            self.printHands();

        inp = raw_input("Options? [yn]")
        if inp in [None,'y']:
                inp = raw_input('Would you like to show deck? [yn]')
                if inp in [None,'y']:
                    print "Printing updated deck\n"
                    for card in deck.cards:
                        print(card)




while True: 
    try:
        num_players = int(raw_input('How many players would you like to play? '));
        game = Poker(num_players,500)
        game.playSampleGame()
        break
    except ValueError:
        print "Enter an int"
    





