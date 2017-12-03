from Common import *

# Get the Captcha
captcha = input('Enter the captcha: ')

# Day 1 Part 1
result1 = checkCaptcha(captcha)
print('Result 1:',result1)

# Day 1 Part 2
result2 = checkCaptchaJump(captcha)
print('Result 2:',result2)