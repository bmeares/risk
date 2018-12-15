class Pixel:
    def __init__(self, r, g, b):
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)
    def __str__(self):
        return str(self.r) + " " + str(self.g) + " " + str(self.b)

class Image:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.pixels = []
