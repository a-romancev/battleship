from random import randint
from ship import Ship


class Board(object):
    def __init__(self, size, attempts, ships_count):
        self.size = size
        self.graph = [["0"] * self.size for i in range(self.size)]
        self.attempts = attempts
        self.ships_count = ships_count

    def get_field(self):
        rows = []
        for row in self.graph:
            rows.append(" ".join(row))

        return '\n'.join(rows)

    def game_begin(self):
        shippy = Ship(randint(0, len(self.graph) - 1), randint(0, len(self.graph) - 1))
        shippy_2 = Ship(randint(0, len(self.graph) - 1), randint(0, len(self.graph) - 1))
    
        print("Let's begin!", shippy.x, shippy.y, shippy_2.x, shippy_2.y)
    
        count = 1
        win_count = 0
    
        while count < self.attempts:
            print("Your ", count, " attempt:")
            guess_x = int(input("guess x: "))
            guess_y = int(input("guess y: "))
            if (guess_x == shippy.x) and (guess_y == shippy.y) and not (self.graph[guess_x][guess_y] == "X"):
                print("you got it!")
                self.graph[guess_x][guess_y] = "X"
                print(self.get_field())
                win_count += 1
                if (win_count == 2) or (self.ships_count == 1):
                    print("You win!")
                    break
            elif (self.ships_count == 2) and (guess_x == shippy_2.x) and (guess_y == shippy_2.y) \
                    and not (self.graph[guess_x][guess_y] == "X"):
                print("you got it!")
                self.graph[guess_x][guess_y] = "X"
                print(self.get_field())
                win_count += 1
                if win_count == 2:
                    print("You win!")
                    break
            elif (guess_x < len(self.graph)) and (guess_y < len(self.graph)):
                self.graph[guess_x][guess_y] = "x"
                print("nope!")
                print(self.get_field())
                if count + 1 == self.attempts:
                    print("You loose!")
                    break
            else:
                print("Out of range!")
                if count + 1 == self.attempts:
                    print("You loose!")
                    break
            count = count + 1
