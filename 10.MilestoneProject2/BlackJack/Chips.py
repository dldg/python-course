'''
Card Chips
'''

import Variables

class Chips:
    
    def __init__(self):
        # This can be set to a default value or supplied by a user input
        self.total = 100
        self.bet = 0
 
    def __str__(self):
        return "Total: " + self.total + " Bet: " + self.bet

    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet