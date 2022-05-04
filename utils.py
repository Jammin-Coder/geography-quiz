import os

def get_continents(path='static/maps'):
    continents = []
    dir_contents = os.scandir(path)
    for item in dir_contents:
        if os.path.isdir(item):
            continents.append(item.name)
    return continents

