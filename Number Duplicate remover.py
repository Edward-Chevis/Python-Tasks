myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList = []
for i in range (len(myList)):
    if myList[i] not in newList:
        newList.append(myList[i])
print("The list with unique elements only:")
print(newList)
