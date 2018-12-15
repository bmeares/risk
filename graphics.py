import colors
import config
from Image import *
import sys
import os

def build_map(img):
    colors.MAP = ""
    ts = os.get_terminal_size()
    w_ratio = img.width / ts.columns
    h_ratio = img.height / ts.lines
    for row in range(ts.lines):
        # if row % 2 == 0:
        for col in range(ts.columns):
            r,g,b = img.pixels[int(row * h_ratio)][int(col * w_ratio)].r, img.pixels[int(row * h_ratio)][int(col * w_ratio)].g, img.pixels[int(row * h_ratio)][int(col * w_ratio)].b
            colors.MAP += colors.rgb_ansi(r,g,b, colors.BLOCK)
        colors.MAP += "\n"

def read_image():
    file = open(config.MAP_LOCATION, "r")
    file.readline() # ignore magic number
    wh = file.readline().split()
    while "#" in wh: # skip comments
        wh = file.readline().split()
    file.readline() # ignore color depth
    w,h = int(wh[0]), int(wh[1])
    img = Image(w,h)
    for row in range(h):
        img.pixels.append([])
        for col in range(w):
            # r,g,b = 0, 100, 255
            r,g,b = int(file.readline()), int(file.readline()), int(file.readline())
            img.pixels[row].append(Pixel(r,g,b))
    file.close()
    return img

def write_image(img):
    out = open("OUT.ppm", "w")
    out.write("P3\n" + str(img.width) + " " + str(img.height) + " " + str(255) + "\n")
    for r in range(img.height):
        for c in range(img.width):
            # print(img.pixels[r][c])
            out.write(str(img.pixels[r][c]) + "\n")
