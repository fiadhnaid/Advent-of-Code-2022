# section has id, each elf has a range of section ids, assignments overlap, in how many pairs does one range fully contain the other
# one would full contain the other if the start of one is less than the start of the other and the end of one is greater than the end of the other

# how many sections overlap
inputFile = open("AOC4Example.txt", "r")
pairs=inputFile.readlines()
inputFile.close
answer=0
for pair in pairs:
    pair.rstrip()
    pairSplit=pair.split(",")
    pair1=[int(pairSplit[0].split("-")[0]),int(pairSplit[0].split("-")[1])]
    pair2=[int(pairSplit[1].split("-")[0]),int(pairSplit[1].split("-")[1])]
    lowerPair=min(pair1[0], pair2[0])
    if (pair1[0] <= pair2[0]) and (pair1[1] >= pair2[0]):
        answer+=1
    # find which has a lower lower, if it ends greater than or equal to the other's lower, it overlaps
    elif (pair2[0] <= pair1[0]) and (pair2[1] >= pair1[0]):
        answer+=1
   
print(answer)