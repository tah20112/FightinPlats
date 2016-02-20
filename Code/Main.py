#!/bin/bash/python2.7

stepsPerRev = 200
stepsPerInch = 25.464
stepsPerDegree = 2.8703
stepsPerCoord = 1.193675
Heading = 0
servo_pin = 30

import random
import numpy as np
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)

servo = GPIO.PWM(servo_pin, 50)
servo.start(0)
servo.ChangeDutyCycle(5)

def goToWaypoint(next_x_coord, next_y_coord, curr_x, curr_y):

    dX = next_x_coord - curr_x
    dY = next_y_coord - curr_y

    dHead = np.arctan(dY/dX)
    dist = np.sqrt(dX^2 + dY^2)

    if(dHead < 0):
        turn_right(dHead)
    elif(dHead > 0):
        turn_left(dHead)
    else:

    HEADING = HEADING + dHead

    steps = np.round(stepsPerCoord*dist)
    moveForward(steps)



    return curr_position

def turnLeft(dHead):
    steps = stepsPerDegree*dHead
    stepper1Turn(steps)

def turnRight(dHead):
	steps = stepsPerDegree*dHead
	stepper2Turn(steps)

def moveForward(steps):
    for i in range (0, steps):
        stepper1Turn(1)
	stepper2Turn(1)




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


def movePen(command): # Takes string input
    if (command == "UP"):
        servo.ChangeDutyCycle(80)
    elif (command == "DN"):
        servo.ChangeDutyCycle(20)
    else:
        print "Servo cannot move to", command
