import math as m

# summary: Compare if two values are equal
# returns: If values are equal, return the value as int
#          If value are not equal, return 0
def compare(a, b):
    if a == b:
        return int(a)
    else:
        return 0

# summary: Get the median index of a string
# note: Expects string of even length, if uneven median index is calculated return floor value
# returns: Median index
def getMedian(str):
    length = len(str)
    return m.floor(length/2);

# summary: Gets the next index based on a step size assuming the string is circular
# returns: Step Index
def getStepIndex(index, step, max):
    next = index + step
    if next > max:
        next = (next - max) - 1
    return next

# summary: Gets the min and max values in an array of values
# returns: min - Smallest value
#          max - Greatest value
def getMinMax(row):
    min = 99999999999
    max = -9999999999
    for cell in row:
        if cell > max:
            max = cell

        if cell < min:
            min = cell

    return min, max

def getModuloPairs(row):
    a = -1
    b = -1
    for x in row:
        for y in row:
            if x % y == 0 and x != y:
                a = x  
                b = y
    
    if a == -1 or b == -1:
        for x in row:
            for y in row:
                if y % x == 0 and x != y:
                    b = x  
                    a = y

    return a, b
    