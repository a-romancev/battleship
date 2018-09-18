from color import Color
from collections import namedtuple
from random import choice


class CellNotEmptyError(ValueError):
    pass


ShipType = namedtuple('ShipType', 'size amount')


class Board:
    SIZE = 10
    SHIPS = (
        ShipType(4, 0),
        ShipType(3, 0),
        ShipType(2, 0),
        ShipType(1, 2),
    )
    TOTAL_SHIP_CELLS = 2

    def __init__(self):
        self.ships = [[False] * self.SIZE for _ in range(self.SIZE)]
        self.hits = [[False] * self.SIZE for _ in range(self.SIZE)]
        self.empty_hit_cells = self.create_empty_set()

    def get_field(self, show_ships):
        field_str = "".join((Color.Yellow + "({:<2})" + Color.END).format(i) for i in range(self.SIZE + 1)) + "\n"
        for x in range(self.SIZE):
            field_str += "".join((Color.Yellow + "({:<2})" + Color.END).format(x + 1))
            for y in range(self.SIZE):
                if self.ships[x][y] and self.hits[x][y]:
                    field_str += Color.Red + "[SX]" + Color.END
                elif self.hits[x][y]:
                    field_str += Color.Blue + "[ X]" + Color.END
                elif self.ships[x][y]:
                    field_str += "[ S]" if show_ships else Color.Grey + "[  ]" + Color.END
                else:
                    field_str += Color.Grey + "[  ]" + Color.END

            field_str += "\n"

        return field_str

    def shoot(self, x, y):
        if x < 0 or x >= self.SIZE or y < 0 or y >= self.SIZE:
            raise ValueError

        if not (x, y) in self.empty_hit_cells:
            raise CellNotEmptyError

        self.empty_hit_cells.remove((x, y))
        self.hits[x][y] = True

        if self.ships[x][y]:
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
