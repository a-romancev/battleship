from controllers.base import BaseController
from connector import Connector
from board import CellNotEmptyError


class NetworkController(BaseController):
    def __init__(self, board, name, is_server):
        super(NetworkController, self).__init__(board, name)
        self.is_server = is_server
        self.connector = Connector()
        if self.is_server:
            self.connector.listen('localhost')
        else:
            self.connector.connect('localhost')

    def turn(self):
        x, y = self.connector.receive_guess()
        is_hit = self.opponent.receive_guess(x, y)
        self.connector.send_answer(is_hit)

    def receive_guess(self, x, y):
        if x < 0 or x >= self.board.SIZE or y < 0 or y >= self.board.SIZE:
            raise ValueError

        if not (x, y) in self.board.empty_hit_cells:
            raise CellNotEmptyError

        self.board.empty_hit_cells.remove((x, y))
        self.board.hits[x][y] = True

        self.connector.send_guess(x, y)
        is_hit = self.connector.receive_answer()
        self.board.ships[x][y] = is_hit

        return is_hit
