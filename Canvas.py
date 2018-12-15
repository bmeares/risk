from copy import *
import colors
import Player
import config
from Image import *
import sys
import os
import globals

def draw():
    clear()
    build_map(globals.current_img)
    print(colors.MAP)

def clear():
    os.system("clear")

def move_player(to_r, to_c):
    # globals.current_img = deepcopy(globals.original_img)
    reset_pixels()
    globals.player.row, globals.player.col = to_r, to_c
    globals.player.under_px = deepcopy(globals.current_img.pixels[to_r][to_c])
    for i in range(int(Player.size / 2)):
        if to_r - i > 0:
            globals.current_img.pixels[to_r - i][to_c] = globals.player.color

    for i in range(int(Player.size / 2)):
        if to_r + i < globals.current_img.height:
            globals.current_img.pixels[to_r + i][to_c] = globals.player.color

    for i in range(int(Player.size / 2)):
        if to_c - i > 0:
            globals.current_img.pixels[to_r][to_c - i] = globals.player.color

    for i in range(int(Player.size / 2)):
        if to_c + i < globals.current_img.width:
            globals.current_img.pixels[to_r][to_c + i] = globals.player.color

def reset_pixels():
    from_r, from_c = globals.player.row, globals.player.col
    for i in range(int(Player.size / 2)):
        if from_r - i > 0:
            globals.current_img.pixels[from_r - i][from_c] = globals.original_img.pixels[from_r - i][from_c]

    for i in range(int(Player.size / 2)):
        if from_r + i < globals.current_img.height:
            globals.current_img.pixels[from_r + i][from_c] = globals.original_img.pixels[from_r + i][from_c]

    for i in range(int(Player.size / 2)):
        if from_c - i > 0:
            globals.current_img.pixels[from_r][from_c - i] = globals.original_img.pixels[from_r][from_c - i]

    for i in range(int(Player.size / 2)):
        if from_c + i < globals.current_img.width:
            globals.current_img.pixels[from_r][from_c + i] = globals.original_img.pixels[from_r][from_c + i]

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


if __name__ == "__main__":
    main()
