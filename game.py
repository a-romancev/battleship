from board import Board
from random import randint
import os


class Game:
    def __init__(self):
        self.my_board = Board(5, 3, show_ships=True)
        self.target_board = Board(5, 3)
        self.attempts = 5

    def print_boards(self):
        os.system('clear')
        print("Your board:")
        print(self.my_board.get_field())
        print("Enemy board:")
        print(self.target_board.get_field())

    def start(self):
        self.print_boards()
        while self.target_board.has_alive:
            try:
                x, y = [int(c) for c in input("Guess x, y: ").split()]
                self.target_board.shoot(x, y)
            except (ValueError, IndexError):
                print("Wrong x/y")
                continue

            self.autoshoot(self.my_board)
            self.print_boards()
            self.attempts -= 1
            if not self.attempts:
                print("You loose!FOOOL")
                return
        print("You won!")

    def autoshoot(self, board):
        board.shoot(randint(0, board.size - 1), randint(0, board.size - 1))
