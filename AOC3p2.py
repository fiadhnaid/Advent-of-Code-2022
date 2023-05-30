# groups of 3, badge identifies group, item type of badge is the only one common to all 3 in group, find the common item to all 3 in group and convert to priority

inputFile = open("AdventofCode3-Example.txt", "r")
rucksacks=inputFile.readlines()
inputFile.close
# print(rucksacks)


def findRecurringItemInRucksacks(rucksack1, rucksack2, rucksack3):
    recurringItem=set(rucksack1).intersection(rucksack2, rucksack3)
    print('recurringItem', recurringItem)
    return list(recurringItem)[0]

def convertItemToPriority(item):
    print('item', item)
    if ord(item)>=97:
        return ord(item)-96
    else:
        return ord(item)-38

def findTotalPriority():
    groupOfRucksacks = []
    totalPriority = 0
    for rucksack in rucksacks:
        groupOfRucksacks.append(rucksack.rstrip())
        if len(groupOfRucksacks)==3:
            totalPriority += convertItemToPriority(findRecurringItemInRucksacks(groupOfRucksacks[0], groupOfRucksacks[1], groupOfRucksacks[2]))
            groupOfRucksacks = []
    return totalPriority

print(findTotalPriority())