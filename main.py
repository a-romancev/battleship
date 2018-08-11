from board import Board


attempts = int(input("How many attempts do you want?: ")) + 1
ships_count = int(input("How many ships do you want?(1,2): "))
board_size = int(input("Board size?: "))
bordy = Board(board_size, attempts, ships_count)
bordy.game_begin()

# if (attempts < 2) and (ships_count > 1):
#     print("You Can't have 1 attempt then there is 2 ships")
# elif ships_count > 2:
#      print("Can't have more than 2 ships")
# else:
