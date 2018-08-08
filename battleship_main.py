from random import randint

board = []


def create_board(board_in):
    for i in range(5):
        board_in.append(["0"] * 5)


def print_board(board_in):
    for row in board_in:
        print(" ".join(row))


def random_cord(board_in):
    return randint(0, len(board_in) - 1)


def game_begin(board_in):
    ship_x = randint(0, len(board_in) - 1)
    ship_y = randint(0, len(board_in) - 1)

    print("Let's begin!", ship_x, ship_y)
    attempts = int(input("How many attempts do you want?: "))

    count = 0

    while count < attempts:
        print ("Your ", count + 1, " attempt:")
        guess_x = int(input("guess x: "))
        guess_y = int(input("guess y: "))
        if (guess_x == ship_x) and (guess_y == ship_y):
            print ("you got it!")
            board_in[guess_x][guess_y] = "X"
            print_board(board)
            break
        else:
            board_in[guess_x][guess_y] = "x"
            print("nope!")
            print_board(board)
        count = count + 1


create_board(board)
game_begin(board)
print('banana')


