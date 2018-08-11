
class Hit(object):
    def __init__(self, x, y, is_hit):
        self.x = x
        self.y = y
        self.is_hit = is_hit

    def __str__(self):
        return "X " if self.is_hit else "x "
