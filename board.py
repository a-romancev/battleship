from random import randint
from ship import Ship
from hit import Hit


class Board(object):
    def __init__(self, size, attempts, ships_count):
        self.size = size
        self.attempts = attempts
        self.ships_count = ships_count
        self.ships = [[None] * self.size for i in range(self.size)]
        self.hits = [[None] * self.size for i in range(self.size)]

        self.create_ships()

    def create_ships(self):
        for i in range(1, self.ships_count):
            ship = Ship(randint(0, self.size - 1), randint(0, self.size - 1))
            self.ships[ship.x][ship.y] = ship

    def get_field(self):
        field_str = ""
        for x in range(self.size):
            for y in range(self.size):
                if self.ships[x][y] and self.hits[x][y]:
                    field_str += "[SX]"
                elif self.hits[x][y]:
                    field_str += "[X ]"
                elif self.ships[x][y]:
                    field_str += "[S ]"
                else:
                    field_str += "[  ]"

            field_str += "\n"

        return field_str

    def guess(self, x, y):
        hit = Hit(x, y, bool(self.ships[x][y]))
        self.hits[x][y] = hit

    # def game_begin(self):
    #     shippy = Ship(randint(0, len(self.graph) - 1), randint(0, len(self.graph) - 1))
    #     shippy_2 = Ship(randint(0, len(self.graph) - 1), randint(0, len(self.graph) - 1))
    #
    #     print("Let's begin!", shippy.x, shippy.y, shippy_2.x, shippy_2.y)
    #
    #     count = 1
    #     win_count = 0
    #
    #     while count < self.attempts:
    #         print("Your ", count, " attempt:")
    #         guess_x = int(input("guess x: "))
    #         guess_y = int(input("guess y: "))
    #         if (guess_x == shippy.x) and (guess_y == shippy.y) and not (self.graph[guess_x][guess_y] == "X"):
    #             print("you got it!")
    #             self.graph[guess_x][guess_y] = "X"
    #             print(self.get_field())
    #             win_count += 1
    #             if (win_count == 2) or (self.ships_count == 1):
    #                 print("You win!")
    #                 break
    #         elif (self.ships_count == 2) and (guess_x == shippy_2.x) and (guess_y == shippy_2.y) \
    #                 and not (self.graph[guess_x][guess_y] == "X"):
    #             print("you got it!")
    #             self.graph[guess_x][guess_y] = "X"
    #             print(self.get_field())
    #             win_count += 1
    #             if win_count == 2:
    #                 print("You win!")
    #                 break
    #         elif (guess_x < len(self.graph)) and (guess_y < len(self.graph)):
    #             self.graph[guess_x][guess_y] = "x"
    #             print("nope!")
    #             print(self.get_field())
    #             if count + 1 == self.attempts:
    #                 print("You loose!")
    #                 break
    #         else:
    #             print("Out of range!")
    #             if count + 1 == self.attempts:
    #                 print("You loose!")
    #                 break
    #         count = count + 1
