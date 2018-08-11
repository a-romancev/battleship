from random import randint
from ship import Ship
from board import Board


def game_begin(board_in):
    shippy = Ship(randint(0, len(board_in) - 1), randint(0, len(board_in) - 1))
    shippy_2 = Ship(randint(0, len(board_in) - 1), randint(0, len(board_in) - 1))

    print("Let's begin!", shippy.x, shippy.y, shippy_2.x, shippy_2.y)

    count = 0
    win_count =0

    while count < attempts:
        print("Your ", count + 1, " attempt:")
        guess_x = int(input("guess x: "))
        guess_y = int(input("guess y: "))
        if (guess_x == shippy.x) and (guess_y == shippy.y) and not (board_in[guess_x][guess_y] == "X"):
            print("you got it!")
            board_in[guess_x][guess_y] = "X"
            bordy.show()
            win_count += 1
            if win_count == 2:
                print("You win!")
                break
        elif (guess_x == shippy_2.x) and (guess_y == shippy_2.y) and not (board_in[guess_x][guess_y] == "X"):
            print("you got it!")
            board_in[guess_x][guess_y] = "X"
            bordy.show()
            win_count += 1
            if win_count == 2:
                print("You win!")
                break
        elif (guess_x < len(board_in)) and (guess_y < len(board_in)):
            board_in[guess_x][guess_y] = "x"
            print("nope!")
            bordy.show()
        else:
            print("Out of range!")
        count = count + 1


bordy = Board(int(input("Board size?: ")))
attempts = int(input("How many attempts do you want?: "))

game_begin(bordy.graph)



