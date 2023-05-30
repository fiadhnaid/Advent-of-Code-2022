inputFile = open("AdventofCode3-Example.txt", "r")
rucksacks=inputFile.readlines()
inputFile.close
print(rucksacks)

# each rucksack 2 compartments
# all items of a type into one compartment
# not true for one item type per rucksack
# item type by letter
# items for a rucksack are on one license
# first half in first comp, second half in second

def findRecurringItemInRucksack(rucksack):
    set1, set2 = split_string(rucksack)
    return list(set1 & set2)[0]


def split_string(string):
    middle = len(string) // 2  # Find the middle index
    set1 = set(string[:middle])  # First half of the string as a set
    set2 = set(string[middle:])  # Second half of the string as a set
    return set1, set2


def convertItemToPriority(item):
    print('item', item)
    if ord(item)>=97:
        return ord(item)-96
    else:
        return ord(item)-38

def findTotalPriority():
    totalPriority = 0
    for rucksack in rucksacks:
        totalPriority += convertItemToPriority(findRecurringItemInRucksack(rucksack))
    return totalPriority

print(findTotalPriority())