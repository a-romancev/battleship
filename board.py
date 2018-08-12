from random import randint


class Board(object):
    def __init__(self, size, ships_count, show_ships=False):
        self.size = size
        self.ships_count = ships_count
        self.show_ships = show_ships
        self.ships = [[False] * self.size for i in range(self.size)]
        self.hits = [[False] * self.size for i in range(self.size)]

        self.create_ships()

    def create_ships(self):
        for i in range(self.ships_count):
            self.ships[randint(0, self.size - 1)][randint(0, self.size - 1)] = True

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
        self.hits[x][y] = True

    @property
    def has_alive(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.ships[x][y] and not self.hits[x][y]:
                    return True

        return False
