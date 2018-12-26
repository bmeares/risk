MAP_LOCATION = ""
AMERICA_LOCATION = ""
MEXICO_LOCATION = ""

def read_config():
    global MAP_LOCATION, AMERICA_LOCATION, MEXICO_LOCATION
    file = open("config.txt", "r")
    MAP_LOCATION = file.readline().strip("\n")
    AMERICA_LOCATION = file.readline().strip("\n")
    MEXICO_LOCATION = file.readline().strip("\n")
    file.close()
