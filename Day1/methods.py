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

# summary: Get the Captcha result for Day 1 Part 1
# returns: Result of Captcha
def checkCaptcha(captcha):
    # get length
    length = len(captcha)    
    # make circular
    circCaptcha = captcha + captcha[0]    
    # initialize sum
    sum = 0
    # loop and sum
    for x in range(0, length):
        sum = sum + compare(circCaptcha[x], circCaptcha[x+1])
    return sum

# summary: Get the Captcha result for Day 1 Part 2
# returns: Result of Capctha
def checkCaptchaJump(captcha):
    length = len(captcha)
    step = getMedian(captcha)    
    # initialize sum
    sum = 0
    # loop and sum
    for x in range(0, length):
        sum = sum + compare(captcha[x], captcha[getStepIndex(x, step, length-1)])    
    return sum