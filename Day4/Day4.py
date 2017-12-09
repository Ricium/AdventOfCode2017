from Common import *
from Reading import *

# Get the file name or default 
filename = input('Enter the Filename (input.txt): ') or 'input.txt'

# Read File
phrases = ReadTextFile(filename)
#phrases = ['aa bb cc dd ee'
#         ,'aa bb cc dd aa'
#         ,'aa bb cc dd aaa']

count = 0
for phrase in phrases:
    phrase_words = getWordsInString(phrase)
    unique_words = getUniqueWords(phrase_words)
    if checkPhrase(phrase_words, unique_words):
        count = count + 1

print('There are', count, 'valid passphrases')

count = 0
for phrase in phrases:
    phrase_words = getWordsInString(phrase)
    unique_words = getUniqueWords(phrase_words)
    if checkPhrase(phrase_words, unique_words):
        isValid = True
        for x in range(0, len(unique_words)):
            if checkPhraseForAnagram(x, unique_words[x], unique_words):
                isValid = False
                break
        if isValid:
            count = count + 1

print('There are', count, ' advance valid passphrases')