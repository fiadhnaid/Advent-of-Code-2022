# what crates end up on top of each stack?
# CMZ

# inputFile = open("AOC5Example.txt", "r"
inputFile = open("AOC5Input.txt", "r")
inputLines=inputFile.readlines()
inputFile.close
i=0
grid=[]
instructions=[]

def formatInput():
    for inputLine in inputLines:
        if (inputLine[0]=='[' or inputLine[0]==' ') and inputLine[1] and not inputLine[1].isdigit():
            currentLine=inputLine.rstrip('\n')
            row=[currentLine[i+1:i+2] for i in range(0, len(currentLine), 4)]
            grid.append(row)
        elif inputLine[0]=='m':
            instruction=(inputLine.rstrip('\n')).split(' ')
            instructions.append([instruction[1],instruction[3],instruction[5]])
        else:
            continue

formatInput()        
# print('grid',grid)
# print('instructions',instructions)

def moveBoxes(instruction):
    for i in range(int(instruction[0])):
        boxToMove=''
        # take first non empty row for that column
        for row in grid:
            if row[int(instruction[1])-1] != ' ':
                boxToMove=row[int(instruction[1])-1]
                row[int(instruction[1])-1]=' '
                break
            else:
                continue
            # now need to deposit box in the instructed column - find first empty row of that column and put it there
        for row in grid[::-1]:
            if row[int(instruction[2])-1] == ' ':
                row[int(instruction[2])-1]= boxToMove
                break
            elif row == grid[0]:
                newRow = [' ' for i in range(len(row))]
                newRow[int(instruction[2])-1]= boxToMove
                grid.insert(0, newRow)

                break
            else:
                continue


def returnTopBoxOfEachColumn(grid):
    topBoxes = [' ' for i in range(len(grid[0]))]
    for row in grid[::-1]:
        for i in range(len(row)):
            # print('row',row)
            if row[i] != ' ':
                # print('row[i]',row[i])
                topBoxes[i]=row[i]
                continue
            else:
                continue
    return topBoxes


for instruction in instructions:
    moveBoxes(instruction)

print('grid',grid)

print('top boxes',''.join(returnTopBoxOfEachColumn(grid)))
