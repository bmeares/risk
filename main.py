from copy import *
import colors
import Player
import config
from Image import *
import sys
import os
import globals
import Canvas

def main():
    config.read_config()
    init_game()
    col = globals.current_img.width - 1
    while col > 0:
        # Canvas.move_player(20,col)
        Canvas.america()
        Canvas.draw()
        input()
        Canvas.mexico()
        Canvas.draw()
        input()
        col -= 1

def init_game():
    globals.original_img = Canvas.read_image(config.MAP_LOCATION)
    globals.current_img = deepcopy(globals.original_img)
    globals.america_img = Canvas.read_image(config.AMERICA_LOCATION)
    globals.mexico_img = Canvas.read_image(config.MEXICO_LOCATION)

if __name__ == "__main__":
    main()
