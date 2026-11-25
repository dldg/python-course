'''
Instantiate a new Hand
 - holds those Cards that have been dealt to each player from the Deck.
'''

from Card import Card
import Variables

class Hand:
    def __init__(self):
        # start with an empty list as we did in the Deck class
        self.cards = []
        # start with zero value
        self.value = 0
        # add an attribute to keep track of aces
        self.aces = 0

    def __str__(self):
        to_str = ''
        for card_object in self.cards:
            to_str += '\n' + card_object.__str__()
        to_str += '\n' + "value" + self.value
        to_str += '\n' + "aces" + self.aces
        return "The Hand has: " + to_str

    def add_card(self,card):
        self.cards.append(card)
        self.value += Variables.values[card.rank]
        # Track Aces
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        # If total value > 21 and I still have an ace
        # change my ace to be a 1 instead of an 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

    def show_all_cards(self):
        print("All cards: ", *self.cards,sep='\n')
    
    def show_second_card(self):
        print(f'Second Card: {self.cards[1]}' + '\n')