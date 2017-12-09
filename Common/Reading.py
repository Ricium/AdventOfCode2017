import csv

# summary: Reads a tabdelimited file
# returns: A 2D Array consiting of the rows/lines of the file, and the integer values of each column in the row/line
def ReadTabDelimitedFile(filename, hasHeadings):
    values = []
    with open(filename,'r') as f:
        if hasHeadings:
            next(f)   
        reader=csv.reader(f,delimiter='\t')
        count = -1
        for row in reader:
            count = count + 1
            length = len(row)
            row_val = []
            for i in range(0, length):
                row_val.append(int(row[i]))
            values.append(row_val)
    return values

def ReadTextFile(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    return content
