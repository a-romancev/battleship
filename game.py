from board import Board
from controllers import ConsoleController, BotController


class Game:
    def __init__(self):
        player1_board = Board()
        player2_board = Board()
        self.player1 = ConsoleController(my_board=player1_board, target_board=player2_board, name="Player1")
        self.player2 = BotController(my_board=player2_board, target_board=player1_board, name="Player2")

    def start(self):
        while True:
            self.player1.turn()
            self.player2.turn()

            if not self.player1.target_board.has_alive:
                self.player1.win()
                self.player2.loose()
                return

            if not self.player2.target_board.has_alive:
                self.player1.loose()
                self.player2.win()
                return
