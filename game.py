from board import Board, CellNotEmptyError, Color
import os


class Game:
    def __init__(self, size, ships):
        self.my_board = Board(size, ships, show_ships=True)
        self.target_board = Board(size, ships)
        self.size = size
        self.ships = ships
        self.attempts = 1

    def print_boards(self):
        os.system('clear')
        print("Your board:")
        print(self.my_board.get_field())
        print("Enemy board:")
        print(self.target_board.get_field())

    def start(self):
        self.print_boards()
        while True:
            print("Attempt:", self.attempts, ".")
            try:
                x, y = [(int(c) - 1) for c in input("Guess row and column: ").split()]
                self.target_board.shoot(x, y)

            except CellNotEmptyError:
                print(Color.Red + "You can't shoot same cords." + Color.END)
                continue

            except (ValueError, IndexError):
                print(Color.Red + "Wrong column or row." + Color.END)
                continue

            self.my_board.shoot_random()
            self.print_boards()
            self.attempts += 1
            if not self.my_board.has_alive:
                print(Color.Red + "You loose!FOOOL." + Color.END)
                return
            if not self.target_board.has_alive:
                print(Color.Green + "You won!" + Color.END)
                return
