class Ship:
    def __init__(self, x, y, is_vertical, size):
        self.x = x
        self.y = y
        self.is_vertical = is_vertical
        self.size = size

    def iter_cells(self):
        counter = 0
        while counter < self.size:
            if self.is_vertical:
                yield self.x, self.y + counter
            else:
                yield self.x + counter, self.y
            counter += 1
