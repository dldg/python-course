'''
Card Class
'''

import Variables

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = Variables.values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit
    