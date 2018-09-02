from random import choice
from collections import namedtuple
from ship_generator import ShipGenerator


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

    def __init__(self):
        self.ships = [[False] * self.SIZE for _ in range(self.SIZE)]
        self.hits = [[False] * self.SIZE for _ in range(self.SIZE)]
        self.empty_hit_cells = self.create_empty_set()
        ShipGenerator(self).generate()

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

    def create_empty_set(self):
        result = set()
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                result.add((x, y))
        return result

    def shoot_random(self):
        point = choice(tuple(self.empty_hit_cells))
        self.hits[point[0]][point[1]] = True
        self.empty_hit_cells.remove(point)

    @property
    def has_alive(self):
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                if self.ships[x][y] and not self.hits[x][y]:
                    return True

        return False


class Color:
    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Blue = '\033[94m'
    Magenta = '\033[95m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Grey = '\033[90m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
