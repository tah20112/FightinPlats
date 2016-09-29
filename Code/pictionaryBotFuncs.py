def getX( str ):
    arr = str.split(' ')
    print arr
    for i in range(len(arr)):
          if arr[i] == 'X':
            if arr[i+2] == '':
                return arr[i+3]
            elif arr[i+1] == '':
                return arr[i+2]
            else:
                return arr[i+1]
    return 0

def getY( str ):
    arr = str.split(' ')
    print arr
    for i in range(len(arr)):
          if arr[i] == 'Y':
            if i == len(arr) - 2:
                return arr[i+1]
            if arr[i+2] == '':
                return arr[i+3]
            elif arr[i+1] == '':
                return arr[i+2]
            else:
                return arr[i+1]
    return 0

def getZ( str ):
    arr = str.split(' ')
    print arr
    for i in range(len(arr)):
          if arr[i] == 'Z':
            if arr[i+2] == '':
                return arr[i+3]
            elif arr[i+1] == '':
                return arr[i+2]
            else:
                return arr[i+1]
    return 0

def readGCode( file ):
    newFile = open(file)
    stringFile = newFile.read()
    lineList = stringFile.split('\n')

    return lineList

def getXValues( Lines ):

    xList = []

    for i in range(len(Lines)):
        x = getX(Lines[i])

        x = int(float(x))
        xList.append(x)

    return xList

def getYValues( Lines ):

    yList = []

    for i in range(len(Lines)):
        y = getY(Lines[i])
        y = int(float(y))
        yList.append(y)

    return yList

def getZValues ( Lines ):

    zList = []

    for i in range(len(Lines)):
        z = getZ(Lines[i])
        z = float(z)
        zList.append(z)

    return zList

def normZVals(zVals):
    newZVals = []
    for i in range(len(zVals)):
        if zVals[i] > 0:
            newZVals.append(2)
        elif zVals[i] < 0:
            newZVals.append(1)
        else:
            newZVals.append(0)

    return newZVals

def checkForZeros(xVal, yVal):
	if xVal == 0 and yVal == 0:
				return True

def removeZeros(xVals, yVals, zVals ):
    newArray = []
    for i in range(len(xVals)):
        if not(checkForZeros(xVals[i], yVals[i])):	    
            newArray.append([xVals[i], yVals[i], zVals[i]])    
    return newArray

