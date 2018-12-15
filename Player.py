from Image import *

size = 4

class Player:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.under_px = Pixel(0,0,0)
        self.color = Pixel(100,50,60)
