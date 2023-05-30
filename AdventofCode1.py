# Part 1
# inputFile = open("AdventofCode1-Input.txt", "r")
# inputLines=inputFile.readlines()
# inputFile.close
# counter = 0
# maxCalories = 0
# for inputLine in inputLines:
#     if (inputLine == '\n'):
#         if (counter > maxCalories):
#             maxCalories = counter
#         counter = 0
#     else:
#         inputLine.rstrip()
#         counter = int(inputLine) + counter

# print(maxCalories)

# Part 2

inputFile = open("AdventofCode1-Input.txt", "r")
# maxCalories is in ascending order
maxCalories = [0, 0, 0]

elves_batches = inputFile.read().split("\n\n")

for elf in elves_batches:
    elfCals=elf.split("\n")
    elfCalsints=[eval(i) for i in elfCals]
    sumElfCals=sum(elfCalsints)
  
    if (sumElfCals > maxCalories[0]):
        maxCalories.append(sumElfCals)
        maxCalories.sort()
        maxCalories.remove(maxCalories[0])
        
print(maxCalories)
print(sum(maxCalories))