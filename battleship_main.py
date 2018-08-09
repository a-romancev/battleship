from random import randint

board = []


class Ship(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(%d, %d)" % (self.x, self.y)


def create_board(board_in):
    size = int(input("Board size?: "))
    for i in range(size):
        board_in.append(["0"] * size)


def print_board(board_in):
    for row in board_in:
        print(" ".join(row))


def game_begin(board_in):
    shippy = Ship(randint(0, len(board_in) - 1), randint(0, len(board_in) - 1))

    print("Let's begin!", shippy.x, shippy.y)
    attempts = int(input("How many attempts do you want?: "))

    count = 0

    while count < attempts:
        print ("Your ", count + 1, " attempt:")
        guess_x = int(input("guess x: "))
        guess_y = int(input("guess y: "))
        if (guess_x == shippy.x) and (guess_y == shippy.y) and not(board_in[guess_x][guess_y] == "X"):
            print("you got it!")
            board_in[guess_x][guess_y] = "X"
            print_board(board)
            break
        elif (guess_x < len(board_in)) and (guess_y < len(board_in)):
                board_in[guess_x][guess_y] = "x"
                print("nope!")
                print_board(board)
        else:
            print("Out of range!")
        count = count + 1


create_board(board)
game_begin(board)



