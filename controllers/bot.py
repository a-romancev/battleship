from controllers.base import BaseController


class BotController(BaseController):
    def turn(self):
        self.target_board.shoot_random()
