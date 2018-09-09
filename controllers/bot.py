from controllers.base import BaseController
from ship_generator import ShipGenerator


class BotController(BaseController):
    def __init__(self, board, name):
        super(BotController, self).__init__(board, name)
        ShipGenerator(board).generate()

    def turn(self):
        self.opponent.receive_guess(*self.opponent.board.give_random())

    def receive_guess(self, x, y):
        return self.board.shoot(x, y)
