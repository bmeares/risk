RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

BLOCK = "█"
MAP = ""

def rgb_ansi(r,g,b,text):
    return "\x1b[38;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m" + text + "\x1b[0m"
