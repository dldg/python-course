'''
Instantiate a new deck
 - Create all 52 card objects
 - Hold as a list of Card Objects
Shuffle a Deck through a method call
 - Random library shuffle() function
Deal cards from the Deck object
 - Pop method from cards list
'''

import random
import Variables
from Card import Card

class Deck:
    def __init__(self):

        self.all_cards = []

        for suit in Variables.suits:
            for rank in Variables.ranks:
                # Create the Card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def __str__(self):
        to_str = ''
        for card_object in self.all_cards:
            to_str +=  '\n' + card_object.__str__()
        return "The Deck has: " + to_str

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

