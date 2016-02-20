import numpy as np
import pictionaryBotFuncs as pc
import time
import matplotlib.pyplot as plt


lines = pc.readGCode('Out_1.txt')
xVals = pc.getXValues(lines)
yVals = pc.getYValues(lines)
zVals = pc.getZValues(lines)
zVals = pc.normZVals(zVals)

for i in range(len(zVals)):
    zVals[i] = int(zVals[i])

xArray = np.transpose(np.asarray(xVals))
yArray = np.transpose(np.asarray(yVals))
zArray = np.transpose(np.asarray(zVals))

for i in range(len(xVals)):
	if pc.checkForZeros(xVals[i], yVals[i], zVals[i]) == True:
		xVals[i] = xVals[i-1]
		yVals[i] = yVals[i-1]
		zVals[i] = zVals[i-1]

fig = plt.figure()

ax1 = fig.add_subplot(211)
line, = ax1.plot(xArray, yArray, color='blue', lw=2)
		

plt.show()

