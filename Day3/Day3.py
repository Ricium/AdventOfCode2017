from Common import *

value = int(input('Enter the Value (1): ') or 1)

layer = getLayer(value)

closestDif = 9999999999999
closestIndex = 0
isNegativeClose = False

for x in range(0, 8):
    dMax = diagonalMax(layer, x)

    if abs(dMax - value) < closestDif:
        closestDif = abs(dMax - value)
        closestIndex = x

        if(dMax - value) < 0:
            isNegativeClose = True
        else:
            isNegativeClose = False

diagonalIndex = isEven(closestIndex)

steps = 1
if diagonalIndex:
    if isNegativeClose:
        steps = (layer-1) * 2 + closestDif
    else:
        steps = (layer-1) * 2 - closestDif  
else:
    if isNegativeClose:
        steps = (layer-1) + closestDif
    else:
        steps = (layer-1) - closestDif

print('Steps', steps)
    