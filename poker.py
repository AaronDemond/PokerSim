import random
class Card:
    def __init__(self, suit, rank): 
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{}".format(self.rank).ljust(2) + self.suit


def __what__():
    return open('poker_help.text', 'r+')





def getDeck():
    suits = ['H','D','S','C']
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','K','Q']
    cards = []

    for s in suits:
        for r in ranks:
            cards.append(Card(s,r))

    return cards

def drawHand(ammount, deck):
    ''' Returns a deck of ammount card objects '''
    #deck should be dict of cards
    #ammount should be int

    hand = []
    for i in range(0,ammount):
        rand = random.randint(1,len(deck) - 1)
        hand.append(deck[rand])

    return hand


def removeFromDeck(cards, deck):
    ''' removes all cards in the cards dict from the deck dict '''
    for c in cards:
        if c in deck:
            deck.remove(c)

    return deck

    
deck = getDeck()#get new deck
hands = []

#Get a deck, clear the table

for x in range(0,5):
    hand = drawHand(2,deck)            #draw a hand from deck
    hands.append(hand)
    deck = removeFromDeck(hand, deck)  #update deck by removing drawn cards

for hand in hands:
    print "\nPrinting hand for player\n"
    for card in hand:
        print(card)

for i in range(0,4):
    if i==0:
        river = drawHand(3, deck)



    else:

        inp = raw_input('Would you like to flop another card? [fh]')
        if inp in ['y','Y',None,'','yes','YES']:
            river = river + drawHand(1,deck)

        else:
            print "flip the cards"
            break

    print "\nPrinting river\n"
    for card in river:
        print(card)



    deck = removeFromDeck(river, deck)


inp = raw_input("dev_opts? [yn]")

if inp in [None,'y']:
        inp = raw_input('Would you like to show deck? [yn]')
        if inp in [None,'y']:
            print "\nPrinting updated deck\n"
            for card in deck:
                print(card)


    




