
# A = Rock (1)
# B = Paper (2)
# C = Scissors (3)

# Score = score for your choice + score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).



def winOrLose(myChoice, theirChoice):
    theirChoice=convert(theirChoice)
    
    match (myChoice, theirChoice):
        case ('X', 'X') | ('Y', 'Y') | ('Z', 'Z'):
            return 3
        case ('X', 'Y') | ('Y', 'Z') | ('Z', 'X'):
            return 0
        case ('X', 'Z') | ('Y', 'X') | ('Z', 'Y'):
            return 6
    
    # if myChoice==theirChoice:
    #     return 3
    # elif myChoice=='X' and theirChoice=='Y':
    #     return 0
    # elif myChoice=='X' and theirChoice=='Z':
    #     return 6
    # elif myChoice=='Y' and theirChoice=='X':
    #     return 6
    # elif myChoice=='Y' and theirChoice=='Z':
    #     return 0
    # elif myChoice=='Z' and theirChoice=='X':
    #     return 0
    # elif myChoice=='Z' and theirChoice=='Y':
    #     return 6    


def convert(theirChoice):
    match theirChoice:
        case 'A':
            return 'X'
        case 'B':
            return 'Y'
        case _:
            return 'Z'

    # if (theirChoice == 'A'):
    #     return 'X'
    # elif (theirChoice == 'B'):
    #     return 'Y'
    # else:
    #     return 'Z'

def convertChoiceToPoints(myChoice):
    match myChoice:
        case 'X':
            return 1
        case 'Y':
            return 2
        case _:
            return 3

    # if (myChoice == 'X'):
    #     return 1
    # elif (myChoice == 'Y'):
    #     return 2
    # else:
    #     return 3


# with open("AdventofCode2.txt", "r") as inputFile:
#     inputLines = inputFile.readlines()
# counter = 0
# for inputLine in inputLines:
#     [first, second] = inputLine.rstrip().split(' ')
#     counter += convertChoiceToPoints(second) + winOrLose(second, first)
# print(counter)  


# Part 2

def calculateYourChoice(theirChoice, outcome):
    theirChoice=convert(theirChoice)
    match (theirChoice, outcome):
        case ('X', 'X') | ('Y', 'Z') | ('Z', 'Y'):
            return 'Z'
        case ('X', 'Y') | ('Y', 'X') | ('Z', 'Z'):
            return 'X'
        case ('X', 'Z') | ('Y', 'Y') | ('Z', 'X'):
            return 'Y'

with open("AdventofCode2.txt", "r") as inputFile:
    inputLines = inputFile.readlines()
counter = 0
for inputLine in inputLines:
    [first, second] = inputLine.rstrip().split(' ')
    yourChoice = calculateYourChoice(first, second)
    print(yourChoice,first)
    counter += convertChoiceToPoints(yourChoice) + winOrLose(yourChoice, first)
print(counter)  
