from Common import *

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

# Get the Captcha
captcha = input('Enter the captcha: ')

# Day 1 Part 1
result1 = checkCaptcha(captcha)
print('Result 1:',result1)

# Day 1 Part 2
result2 = checkCaptchaJump(captcha)
print('Result 2:',result2)