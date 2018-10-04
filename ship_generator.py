from random import randint
from ship import Ship


class ShipGenerator:
    def __init__(self, board):
        self.board = board
        self.empty_cells = self.board.create_empty_set()

    def check_ship(self, ship):
        for x, y in ship.iter_cells():
            if (x, y) not in self.empty_cells:
                return False
        return True

    def generate(self):
        self.empty_cells = self.board.create_empty_set()
        for ship_tuple in self.board.SHIPS:
            for _ in range(ship_tuple.amount):
                self.create_random_ship(ship_tuple.size)

    def create_random_ship(self, size):
        ship = self.get_random_ship(size)
        if self.check_ship(ship):
            self.save_ship(ship)
        else:
            self.create_random_ship(size)

    def save_ship(self, ship):
        for x, y in ship.iter_cells():
            self.board.ships[x][y] = ship
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    try:
                        self.empty_cells.remove((x+dx, y+dy))
                    except KeyError:
                        pass

    def get_random_ship(self, size):
        x = randint(0, self.board.SIZE - 1)
        y = randint(0, self.board.SIZE - 1)
        is_vertical = bool(randint(0, 1))
        ship = Ship(x, y, is_vertical, size)
        return ship
