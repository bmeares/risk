MAP_LOCATION = ""

def read_config():
    global MAP_LOCATION
    file = open("config.txt", "r")
    MAP_LOCATION = file.readline().strip("\n")
    file.close()
