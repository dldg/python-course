'''
GameLogic Class
'''

from Chips import Chips
from Deck import Deck
from Hand import Hand

playing = True

class GameLogic:

    def __init__(self,player_name):
        # Game Setup

        self.player_name = player_name

        # Create & shuffle the deck
        print("Creating Deck...")
        self.new_deck = Deck()
        self.new_deck.shuffle()

        # Create the player Hand
        self.player_hand = Hand()

        # Create the Dealer Hand
        self.dealer_hand = Hand()

        # Set up the Player's chips
        self.player_chips = Chips()

    def take_bet(self):
        '''
        Take a bet
        Ask usr for the amount
        Check if Chips balance is ok
        '''
        # Waiting for correct response
        waiting = True
        while waiting:
            try:
                bet = int(input("How many chips would you like to bet? "))
            except:
                print("An error occurred! Please try again!")
                continue
            else:
                if bet > self.player_chips.total:
                    print("The bet is higher than the total! Please try again!")
                else:
                    waiting = False
                    break
        
        self.player_chips.bet = bet

    def hit(self):
        self.player_hand.add_card(self.new_deck.deal_one())
        self.player_hand.adjust_for_ace()
    
    def hit_or_stand(self):
        global playing  # to control an upcoming while loop

        # Waiting for correct response
        waiting = True
        while waiting:
            try:
                option_chosen = input("Hit or Stand? (Insert h fot Hit or s for Stand)")
                if option_chosen[0].lower() == 'h':
                    self.hit()
                elif option_chosen[0].lower() == 's':
                    print("Player Stands, Dealer's turn")
                    playing = False
                else:
                    print("Sorry, I did not understand, Please enter h or s only!")
                    continue
            except:
                print("An error occurred! Please try again!")
                continue
            else:
                waiting = False        


    def show_some(self):
        print("Dealer's hand: \n")
        print("First card hidden! \n")
        self.dealer_hand.show_second_card()
        print("Player's hand:\n")
        self.player_hand.show_all_cards()
    
    def show_all(self):
        print("Dealer's hand:\n")
        self.dealer_hand.show_all_cards()
        print(f"Value of Dealer's hand is: {self.dealer_hand.value}")
        print("Player's hand:\n")
        self.player_hand.show_all_cards()
        print(f"Value of Player's hand is: {self.player_hand.value}")

    def player_busts(self):
        print("\nPlayer Busts!")
        self.player_chips.lose_bet()

    def player_wins(self):
        print("\nPlayer Wins!")
        self.player_chips.win_bet()

    def dealer_busts(self):
        print("\nDealer Busted! Player Wins!")
        self.player_chips.win_bet()
        
    def dealer_wins(self):
        print("\nDealer Wins!")
        self.player_chips.lose_bet()

    def push(self):
        '''
        Both dealer and player have 21
        '''
        print("\nDealer and player tie! PUSH")

    def run_game(self):
        global playing
        playing = True
        print("Running the game...")

        # Deal two cards to each player
        self.dealer_hand.add_card(self.new_deck.deal_one())
        self.player_hand.add_card(self.new_deck.deal_one())

        self.dealer_hand.add_card(self.new_deck.deal_one())
        self.player_hand.add_card(self.new_deck.deal_one())

        # Prompt the Player for their bet
        self.take_bet()
        
        # Show cards (but keep one dealer card hidden)
        self.show_some()

        # recall this variable from our hit_or_stand function
        while playing:
            
            # Prompt for Player to Hit or Stand
            self.hit_or_stand()
            
            # Show cards (but keep one dealer card hidden)
            self.show_some()
            
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if self.player_hand.value > 21:
                self.player_busts()
                break

            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
            if self.player_hand.value <= 21:
                # another option is to hit as long as the dealer has less value than the player.
                while self.dealer_hand.value < 17:
                    self.dealer_hand.add_card(self.new_deck.deal_one())
        
                # Show all cards
                self.show_all()

                # Run different winning scenarios
                if self.dealer_hand.value > 21:
                    self.dealer_busts()
                elif self.dealer_hand.value > self.player_hand.value:
                    self.dealer_wins()
                elif self.dealer_hand.value < self.player_hand.value:
                    self.player_wins()
                else:
                    self.push()
        
            # Inform Player of their chips total
            print(f'\nYour Chips balance is: {self.player_chips.total}')
