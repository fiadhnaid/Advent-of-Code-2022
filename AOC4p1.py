# section has id, each elf has a range of section ids, assignments overlap, in how many pairs does one range fully contain the other
# one would full contain the other if the start of one is less than the start of the other and the end of one is greater than the end of the other

inputFile = open("AOC4Example.txt", "r")
pairs=inputFile.readlines()
inputFile.close
answer=0
for pair in pairs:
    pair.rstrip()
    pairSplit=pair.split(",")
    pair1Lower=int(pairSplit[0].split("-")[0])
    pair1Upper=int(pairSplit[0].split("-")[1])
    pair2Lower=int(pairSplit[1].split("-")[0])
    pair2Upper=int(pairSplit[1].split("-")[1])
    if (pair1Lower <= pair2Lower and pair1Upper >= pair2Upper):
        print(pair)
        answer+=1
    elif (pair1Lower >= pair2Lower and pair1Upper <= pair2Upper):
        print(pair)
        answer+=1
else:
        print("no overlap")

print(answer)