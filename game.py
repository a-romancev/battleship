from board import Board, CellNotEmptyError
from random import randint
import os


class Game:
    def __init__(self):
        self.my_board = Board(5, 3, show_ships=True)
        self.target_board = Board(5, 3)

    def print_boards(self):
        os.system('clear')
        print("Your board:")
        print(self.my_board.get_field())
        print("Enemy board:")
        print(self.target_board.get_field())

    def start(self):
        self.print_boards()
        while True:
            try:
                x, y = [int(c) for c in input("Guess x, y: ").split()]
                self.target_board.shoot(x, y)

            except CellNotEmptyError:
                print("You can't shoot same cords")
                continue

            except (ValueError, IndexError):
                print("Wrong x/y")
                continue

            self.my_board.shoot_random()
            self.print_boards()
            if not self.my_board.has_alive:
                print("You loose!FOOOL")
                return
            if not self.target_board.has_alive:
                print("You won!")
                return
