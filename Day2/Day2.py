from Common import *
from Reading import *

# summary: Gets the checksum for Day 2 Part 1
def checksum(data):
    res = 0
    for row in data:
        min, max = getMinMax(row)     
        res = res + (max - min)
    print('Checksum Part 1:', res) 

# summary: Gets the checksum for Day 2 Part 2
def checksumModulo(data):
    res = 0
    for row in data:
        a, b = getModuloPairs(row)
        res = res + (a/b)
    print('Checksum Part 2:', res) 

# Get the file name or default 
filename = input('Enter the Filename (input.tsv): ') or 'input.tsv'

# Read the file
rows = ReadTabDelimitedFile(filename, False)

# Get the checksum part 1
checksum(rows)

# Get the checksum part 2
checksumModulo(rows)