
listItems = ["Ab", "Cd", "Ff", 39]

print(listItems)

# add new item from END
listItems.append("DD")
print(listItems)

# add new item with index number 
listItems.insert(4, True)
print(listItems)

secondList = ["r","y"]

addTwoList = listItems.extend(secondList)
print(addTwoList)