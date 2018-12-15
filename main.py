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
        Canvas.move_player(20,col)
        Canvas.draw()
        input()
        col -= 1

def init_game():
    globals.original_img = Canvas.read_image()
    globals.current_img = deepcopy(globals.original_img)

if __name__ == "__main__":
    main()
