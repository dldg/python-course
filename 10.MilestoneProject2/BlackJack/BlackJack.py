'''
BlackJack main file
'''

from GameLogic import GameLogic

if __name__ == '__main__':
    print("----=== BlackJack GAME ===----")
    try:
        player_name = input("Please enter your name: ")
        print("Creating Game Logic...")

        game_logic = GameLogic(player_name)

        while True:
            game_logic.run_game()

            # Ask to play again
            new_game = input("Would you like to play another hand? y/n")
            
            if new_game[0].lower() == 'y':
                playing = True
                continue
            else:
                print("Thank you fo playing!")
                break

        print("----=== GAME OVER ===----")

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
