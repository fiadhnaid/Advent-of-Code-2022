inputFile = open("AOC6-input.txt", "r")
# inputFile = open("AOC6-example.txt", "r")
inputLines=inputFile.readlines()
inputFile.close

# find the first four letter grouping without a repeating character

def findNonRepeatingGroup():
    holder=''
    counter=0
    for character in inputLines[0]:
        # for p1:
        # if len(holder)<4:
        if len(holder)<14:
            counter+=1
            print('a',counter)
            holder+=character
        # for p1
        # elif len(set(holder)&set(holder))==4:
        elif len(set(holder)&set(holder))==14:
            print('b',set(holder)&set(holder))
            return counter
        else:
            counter+=1
            print('c', holder[0],counter)
            holder=holder[1:]+character

nonRepeatingGroup = findNonRepeatingGroup()
print('nonRepeatingGroup',nonRepeatingGroup)
print(set('h')&set('e')&set('l'))