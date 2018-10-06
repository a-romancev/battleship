from board import Board
from controllers import ConsoleController, NetworkController


class Game:
    def __init__(self, is_server):
        self.player1 = ConsoleController(board=Board(), name="Player1")
        # self.player2 = NetworkController(board=Board(), name="Player2", is_server=is_server)
        self.player2 = ConsoleController(board=Board(), name="Player2")

        if is_server:
            self.player1, self.player2 = self.player2, self.player1
        self.player1.opponent = self.player2
        self.player2.opponent = self.player1

    def start(self):
        while True:
            
            self.player1.turn()
            self.player2.turn()

            if not self.player2.board.has_alive:
                self.player1.win()
                self.player2.loose()
                return

            if not self.player1.board.has_alive:
                self.player1.loose()
                self.player2.win()
                return
