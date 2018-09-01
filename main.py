#! /usr/bin/python3
from game import Game

size = 0
ships = 1

while (size < ships) or (size < 1):
    size = int(input("Size of the board?: "))
    if size < 2:
        print("You cant have a board that small.")
    else:
        ships = int(input("How many ships do you want?: "))
        if ships > size:
            print("Too many ships, you can place a maximum of ", size, ".")
        else:
            Game(size, ships).start()


