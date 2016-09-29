import pictionaryBotFuncs as pbf
import numpy as np
import matplotlib.pyplot as plt

def column(matrix, i):
    return [row[i] for row in matrix]

def getFile( i ):
	if i == 0:	
		return'../G-Code/amason.txt'
	if i == 1:
		return '../G-Code/apple.txt'
	if i == 2:
		return'../G-Code/batman.txt'
	if i == 3:
		return '../G-Code/cup.txt'
	if i == 4:
		return '../G-Code/deadpool.txt'
	if i == 5:
		return '../G-Code/FORK.txt'
	if i == 6:
		return '../G-Code/Hand.txt'
	if i == 7:
		return '../G-Code/dolphin.txt'
	if i == 8:
		return '../G-Code/plant.txt'
	if i == 9:
		return '../G-Code/platypus.txt'
	


for i in range(0, 10):
	lines = []
	xVals = []
	yVals = []
	zVals = []
	arr = []
	filename = getFile(i)
	lines = pbf.readGCode(filename)
	xVals = pbf.getXValues(lines)
	yVals = pbf.getYValues(lines)
	zVals = pbf.getZValues(lines)
	zVals = pbf.normZVals(zVals)
	
	

	arr = pbf.removeZeros(xVals, yVals, zVals)
	
	filename = filename[:-4]
	filename = filename[9:]
	np.savetxt(('../Coord-Files') + filename + ('Coords.txt'), zip(*arr))
	
	
	fig = plt.figure(i)
	plt.plot(column(arr, 0), column(arr, 1), color='red', lw=2)

	fig.show()





