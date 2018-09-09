class BaseController:
    def turn(self):
        raise NotImplementedError

    def receive_guess(self, x, y):
        raise NotImplementedError

    def win(self):
        pass

    def loose(self):
        pass

    def __init__(self, board, name):
        self.board = board
        self.name = name
        self.opponent = None
