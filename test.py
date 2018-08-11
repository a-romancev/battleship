from random import randint
from ship import Ship


shippy = Ship(randint(0, len(board_in) - 1), randint(0, len(board_in) - 1))
shippy_2 = Ship(randint(0, len(board_in) - 1), randint(0, len(board_in) - 1))

while shippy != shippy_2:
    shippy = Ship(randint(0, len(board_in) - 1), randint(0, len(board_in) - 1))
    shippy_2 = Ship(randint(0, len(board_in) - 1), randint(0, len(board_in) - 1))

print(shippy.x, shippy.y, shippy_2.x, shippy_2.y)