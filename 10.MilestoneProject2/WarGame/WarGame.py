'''
WarGame main file
'''

from GameLogic import GameLogic

if __name__ == '__main__':
    print("----=== WAR GAME ===----")
    try:
        player_one_name = input("Please enter player one name: ")
        player_two_name = input("Please enter player two name: ")

        print("Creating Game Logic...")

        game_logic = GameLogic(player_one_name,player_two_name)

        game_logic.run_game()

        print("----=== GAME OVER ===----")

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)



