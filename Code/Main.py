#!/bin/bash/python2.7

import random

def goToWaypoint():
    pass

def getCoords():
    coord_options = {
        0: '../Coord-Files/amasonCoords.txt',
        1: '../Coord-Files/appleCoords.txt',
        2: '../Coord-Files/batmanCoords.txt',
        3: '../Coord-Files/cupCoords.txt',
        4: '../Coord-Files/deadpoolCoords.txt',
        5: '../Coord-Files/FORKCoords.txt',
        6: '../Coord-Files/HandCoords.txt',
        7: '../Coord-Files/makeMITCoords.txt',
        8: '../Coord-Files/plantCoords.txt',
        9: '../Coord-Files/platypusCoords.txt',

	}

    coord_file = coord_options[random.randint(0,9)]

    with open(coord_file) as text:
        coords = text.read().split()

    x_coords = coords[::3]
    y_coords = coords[1::3]
    z_coords = coords[2::3]

    return [x_coords, y_coords, z_coords]

