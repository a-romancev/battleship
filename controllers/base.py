class BaseController:
    def turn(self):
        raise NotImplementedError

    def win(self):
        pass

    def loose(self):
        pass

    def __init__(self, my_board, target_board, name):
        self.my_board = my_board
        self.target_board = target_board
        self.name = name
