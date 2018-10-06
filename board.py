from color import ColoredText
from collections import namedtuple
from random import choice


class CellNotEmptyError(ValueError):
    pass


ShipType = namedtuple('ShipType', 'size amount')


class Board:
    SIZE = 10
    SHIPS = (
        ShipType(4, 1),
        ShipType(3, 2),
        ShipType(2, 3),
        ShipType(1, 4),
    )
    TOTAL_SHIP_CELLS = 4

    def __init__(self):
        self.ships = [[None] * self.SIZE for _ in range(self.SIZE)]
        self.hits = [[False] * self.SIZE for _ in range(self.SIZE)]
        self.empty_hit_cells = self.create_empty_set()

    def get_field(self, show_ships):
        field_str = ColoredText().yellow("".join("({:<2})".format(i) for i in range(self.SIZE + 1)) + "\n")
        for x in range(self.SIZE):
            field_str.yellow("({:<2})".format(x + 1))
            for y in range(self.SIZE):
                if self.ships[x][y] and self.hits[x][y]:
                    if self.ships[x][y].is_dead():
                        field_str.red("[SX]")
                    else:
                        field_str.magenta("[SX]")
                elif self.hits[x][y]:
                    field_str.blue("[ X]")
                elif self.ships[x][y]:
                    field_str.default("[ S]") if show_ships else field_str.grey("[  ]")
                else:
                    field_str.grey("[  ]")

            field_str.default("\n")

        return field_str

    def shoot(self, x, y):
        if x < 0 or x >= self.SIZE or y < 0 or y >= self.SIZE:
            raise ValueError

        if not (x, y) in self.empty_hit_cells:
            raise CellNotEmptyError

        self.empty_hit_cells.remove((x, y))
        self.hits[x][y] = True

        if self.ships[x][y]:
            self.ships[x][y].take_hit()
            return True
        else:
            return False

    def create_empty_set(self):
        result = set()
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                result.add((x, y))
        return result

    def give_random(self):
        point = choice(tuple(self.empty_hit_cells))
        return point

    @property
    def has_alive(self):
        hit_count = 0
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                if self.ships[x][y] and self.hits[x][y]:
                    hit_count += 1
        return hit_count < self.TOTAL_SHIP_CELLS
