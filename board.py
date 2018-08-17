from random import choice


class CellNotEmptyError(ValueError):
    pass


class Board:
    def __init__(self, size, ships_count, show_ships=False):
        self.size = size
        self.ships_count = ships_count
        self.show_ships = show_ships
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

    def get_field(self):
        field_str = ""
        for x in range(self.size):
            for y in range(self.size):
                if self.ships[x][y] and self.hits[x][y]:
                    field_str += "[SX]"
                elif self.hits[x][y]:
                    field_str += "[X ]"
                elif self.ships[x][y]:
                    field_str += "[S ]" if self.show_ships else "[  ]"
                else:
                    field_str += "[  ]"

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
