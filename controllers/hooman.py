import socket
import sys
import os
from controllers.base import BaseController
from board import CellNotEmptyError
from color import Color
from connector import Connector


class HoomanController(BaseController):
    Connector.connect('localhost')
    Connector.listen('localhost')

    def __init__(self, my_board, target_board, name):
        super(HoomanController, self).__init__(my_board, target_board, name)

    def print_boards(self):
        os.system('clear')
        print("My board:")
        print(self.my_board.get_field(True))
        print("Enemy board:")
        print(self.target_board.get_field(False))

    def turn(self):
        input("{} ready?".format(self.name))
        self.print_boards()
        print("Attempt:", self.attempts, ".")
        try:
            x, y = [(int(c) - 1) for c in input("Guess row and column: ").split()]
            Connector.send_guess(x, y)

        except CellNotEmptyError:
            print(Color.Red + "You can't shoot same cords." + Color.END)
            self.turn()

        except (ValueError, IndexError):
            print(Color.Red + "Wrong column or row." + Color.END)
            self.turn()

        else:
            self.attempts += 1
            self.print_boards()

    def win(self):
        self.print_boards()
        print(Color.Green + "{} has won!".format(self.name) + Color.END)

    def loose(self):
        self.print_boards()
        print(Color.Red + "{} has lost!".format(self.name) + Color.END)
