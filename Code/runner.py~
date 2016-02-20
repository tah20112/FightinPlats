import numpy as np
import pictionaryBotFuncs as pc
import time
import matplotlib.pyplot as plt


lines = pc.readGCode('../G-Code/dolphin.txt')
xVals = pc.getXValues(lines)
yVals = pc.getYValues(lines)
zVals = pc.getZValues(lines)
zVals = pc.normZVals(zVals)



arr = [xVals, yVals, zVals]

np.savetxt('../Coord-Files/dolphinCoords.txt', zip(*arr))

