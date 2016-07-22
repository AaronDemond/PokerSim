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

class Tests:
    
    def testTwoPair():
        cards = [('4','D'), ('4', 'D'), ('8','S'), ('6','C'), ('J','D')]
        player = Player('Aaron', 500)



class Player:
    def __init__(self, name, starting_stack):
        self.name = name
        self.starting_stack = starting_stack
        self.score = 11

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
            player.var1 = 'test!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
            self.players.append(player)


    
    @staticmethod
    def _isFlush(p_hands):
        for hand in p_hands:
            suit = hand[0].suit
            for card in hand:
                if card.suit != suit:
                    return False
            return True

    @staticmethod
    def _isStraightFlush(p_hands):
        if Poker._isFlush(p_hands) and Poker._isStraight(p_hands):
            return True

    @staticmethod
    def _isRoyalFlush(p_hands):
        for hand in p_hands:
            if Poker._isFlush(p_hands):
                suits = [card.suit for card in p_hands[0]]
                if 'A' in suits and 'K' in suits:
                    return True

    @staticmethod
    def _isPair(p_hands):
        for hand in p_hands:
            for card in hand:
                if hand.count(card) == 2:
                    return True

    @staticmethod
    def _isTwoPair(p_hands):
        for hand in p_hands:
            for card in hand:
                if hand.count(card) == 2:
                    return True

    @staticmethod
    def _isThreeOfAKind(p_hands):
        for hand in p_hands:
            ranks = [card.rank for card in hand]
            return bool([True for x in ranks if ranks.count(x) == 3])

    @staticmethod
    def _isFourOfAKind(p_hands):
        for hand in p_hands:
            ranks = [card.rank for card in hand]
            return bool([True for x in ranks if ranks.count(x) == 4])

    @staticmethod
    def _isFullHouse(p_hands):
        for hand in p_hands:
            two = bool([True for x in hand if hand.count(x) == 2])
            three = bool([True for x in hand if hand.count(x) == 3])
            if two and three:
                return True



    @staticmethod
    def _isStraight(p_hands):

        for hand in p_hands:
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

            if s == True:
                return True

        return False


    @staticmethod
    def convertScoreToText(score):
        print "GIVEN:::::: " + str(score)
        if score == 1:
            return 'Royal Flush'

        if score == 2:
            return 'Straight Flush'

        if score == 3:
            return 'Four of a Kind'

        if score == 4:
            return 'Full House'

        if score == 5:
            return 'Flush'

        if score == 6:
            return 'Straight'
        
        if score == 7:
            return 'Three of a Kind'

        if score == 8:
            return 'Two Pair'

        if score == 9:
            return 'One Pair'

        if score == 10:
            return 'High Card'



    def getBestHand(self):

        curr_best = 11 #1 = Royal Flush - 10 = High card. 11 means nothing.

        # loop through players, assign p_hands as a dict of all possible 5 card hands
        for player in self.players:
            card_pile = player.hand
            river = self.river
            for c in river:
                card_pile.append(c)
            player.p_hands = list(itertools.permutations(card_pile, 5))
            player.p_hands = [[card for card in hand] for hand in player.p_hands] 
            


            player.score = 11

            if self._isPair(player.p_hands):
                player.score = 9

            if self._isTwoPair(player.p_hands):
                player.score = 8

            if self._isThreeOfAKind(player.p_hands):
                player.score = 7

            if self._isStraight(player.p_hands):
                player.score = 6

            if self._isFlush(player.p_hands):
                player.score = 5

            if self._isFullHouse(player.p_hands):
                player.score = 4

            if self._isFourOfAKind(player.p_hands):
                player.score = 3

            if self._isStraightFlush(player.p_hands):
                player.score = 2

            if self._isRoyalFlush(player.p_hands):
                player.score = 1


            player.high_card = self.highestCard(card_pile)

        return min([player.score for player in self.players])




    @staticmethod
    def highestCard(cards):

        cur_max = None
        cur_max_cards = []
        for card in cards:
            for v in card.getValue(): #Cards can have multiple values (Only ace, but it is coded to always return a dict)
                if v == cur_max:
                    cur_max_cards.append(card)
                elif v > cur_max:
                    cur_max = v
                    cur_max_cards = [card]

        return cur_max_cards[0]

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


        highscore = self.getBestHand()
        winner = None
        for player in self.players:
            if highscore == player.score:
                winner = player
        print "Winner: " 
        print winner.name
        print self.convertScoreToText(int(winner.score))


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
    





