
class Board(object):
    def __init__(self, size):
        self.size = size
        self.graph = [["0"] * self.size for i in range(self.size)]

    def show(self):
        for row in self.graph:
            print(" ".join(row))