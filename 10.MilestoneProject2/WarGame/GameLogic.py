'''
GameLogic Class
'''

from Deck import Deck
from Player import Player

NUM_OF_CARDS_ON_WAR = 10

class GameLogic:

    def __init__(self,player_one_name, player_two_name):
        # Game Setup

        print("Creating players...")

        self.player_one = Player(player_one_name)
        self.player_two = Player(player_two_name)

        print("Creating Deck...")

        self.new_deck = Deck()
        self.new_deck.shuffle()

        print("Distributing cards...")

        for x in range(26):
            self.player_one.add_cards(self.new_deck.deal_one())
            self.player_two.add_cards(self.new_deck.deal_one())

    def run_game(self):

        print("Running the game...")

        game_on = True
        round_num = 0

        while game_on:
            round_num += 1
            print(f"Round {round_num}")

            if len(self.player_one.all_cards) == 0:
                print(f'Player {self.player_one.name}, out of cards! Player {self.player_two.name} Wins!')
                game_on = False
                break

            if len(self.player_two.all_cards) == 0:
                print(f'Player {self.player_two.name}, out of cards! Player {self.player_one.name} Wins!')
                game_on = False
                break

            # Start a mew round
            player_one_cards = []
            player_one_cards.append(self.player_one.remove_one())
            player_two_cards = []
            player_two_cards.append(self.player_two.remove_one())

            at_war = True
            # While at war
            while at_war:
                if player_one_cards[-1].value > player_two_cards[-1].value:
                    self.player_one.add_cards(player_one_cards)
                    self.player_one.add_cards(player_two_cards)
                    at_war = False
                elif player_one_cards[-1].value < player_two_cards[-1].value:
                    self.player_two.add_cards(player_one_cards)
                    self.player_two.add_cards(player_two_cards)
                    at_war = False
                else:
                    print('WAR!')

                    if len(self.player_one.all_cards) < NUM_OF_CARDS_ON_WAR:
                        print(f'Player {self.player_one.name} unable to declare war')
                        print(f'Player {self.player_two.name} wins!')
                        game_on = False
                        break
                    elif len(self.player_two.all_cards) < NUM_OF_CARDS_ON_WAR:
                        print(f'Player {self.player_two.name} unable to declare war')
                        print(f'Player {self.player_one.name} wins!')
                        game_on = False 
                        break
                    else:
                        for num in range(NUM_OF_CARDS_ON_WAR):
                            player_one_cards.append(self.player_one.remove_one())
                            player_two_cards.append(self.player_two.remove_one())




