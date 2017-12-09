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
    
def diagonalMax(layer, y):
    val = 1;
    for x in range(1, layer):
        val = val + (8 * x) - y;
    return val
    
def layerSeed(seed):
    return seed + 2

def getLayer(val):
    temp = 0
    count = 0

    seed = 1
    while temp < val:
        count = count + 1
        temp = seed * seed
        seed = layerSeed(seed)

    return count
        
def isEven(val):
    if val % 2 == 0:
        return True
    else:
        return False

def getWordsInString(str):
    return str.split(' ')

def getUniqueWords(words):
    unique = list(set(words))
    return unique

def getCount(unique, word):
    count = 0
    for letter in word:
       if letter == unique:
           count = count + 1
    return count 

def isAnagram(a, b):
    if len(a) == len(b):
        letters_a = list(a)
        letters_b = list(b)

        unique_a = getUniqueWords(letters_a)
        unique_b = getUniqueWords(letters_b)

        if len(unique_a) == len(unique_b):
            if unique_a.sort() == unique_b.sort():
                isSame = True
                for letter in unique_a:
                    count_a = getCount(letter, a)
                    count_b = getCount(letter, b)
                    if count_a != count_b:
                        isSame = False
                        break
                return isSame
            else:
                return False
        else:
            return False
    else:
        return False

def checkPhrase(phrase, words):
    if len(phrase) == len(words):
        return True
    else:
        return False;

def checkPhraseForAnagram(index, word, phrase):
    foundAnagram = False
    for x in range(0, len(phrase)):
        if x != index:            
            foundAnagram = isAnagram(word, phrase[x])
            if foundAnagram:
                break
    return foundAnagram