#!/bin/bash/python2.7

import random
import numpy as np
import StepMotor as sm

stepsPerRev = 200
stepsPerInch = 25.464
stepsPerDegree = 2.8703
stepsPerCoord = 1.193675
def goToWaypoint(next_x_coord, next_y_coord, next_z_coord, curr_x, curr_y):

    dX = next_x_coord - curr_x
    dY = next_y_coord - curr_y
	
    dHead = np.arctan(dX/Y)
    dist = np.sqrt(dX^2 + dY^2)
    angleSteps = dHead*stepsPerDegree
    if(dHead > 0):
        leftMotorTurn(angleSteps)
    elif(dHead < 0):
        rightMotorTurn(-angleSteps)
    else:
	
    HEADING = HEADING + dHead

    steps = np.round(stepsPerCoord*dist)
    moveForward(steps)



    return curr_position



def moveForward(steps):
    for i in range (0, steps):
        leftMotorTurn(1)
	rightMotorTurn(1)




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



