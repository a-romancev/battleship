from random import randint



class Board(object):
    def __init__(self, size):
        self.size = size
        self.graph = [["0"] * self.size for i in range(self.size)]

    def show(self):
        for row in self.graph:
            print(" ".join(row))



class Ship(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


bordy = Board(int(input("Board size?: ")))
bordy.graph[1][2] = "X"
bordy.show()



