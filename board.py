from random import choice


class CellNotEmptyError(ValueError):
    pass


class Board:
    def __init__(self, size, ships_count, show_ships=False):
        self.size = size
        self.ships_count = ships_count
        self.ships = [[False] * self.size for i in range(self.size)]
        self.hits = [[False] * self.size for i in range(self.size)]
        self.empty_cells = self.create_empty_set()
        self.create_ships()

    def create_ships(self):
        empty_cells_ships = self.create_empty_set()
        for i in range(self.ships_count):
            point = choice(tuple(empty_cells_ships))
            self.ships[point[0]][point[1]] = True
            empty_cells_ships.remove(point)

    def get_field(self, show_ships):
        field_str = "".join((Color.Yellow + "({:<2})" + Color.END).format(i) for i in range(self.size + 1)) + "\n"
        for x in range(self.size):
            field_str += "".join((Color.Yellow + "({:<2})" + Color.END).format(x + 1))
            for y in range(self.size):
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
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            raise ValueError

        if not (x, y) in self.empty_cells:
            raise CellNotEmptyError

        self.empty_cells.remove((x, y))
        self.hits[x][y] = True

    def create_empty_set(self):
        result = set()
        for x in range(self.size):
            for y in range(self.size):
                result.add((x, y))
        return result

    def shoot_random(self):
        point = choice(tuple(self.empty_cells))
        self.hits[point[0]][point[1]] = True
        self.empty_cells.remove(point)

    @property
    def has_alive(self):
        for x in range(self.size):
            for y in range(self.size):
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
