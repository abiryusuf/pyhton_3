
thisList = ["apple", "banana", "cherry", "orange", "melon", "mango"]

print("first Item " + thisList[1])
# From last item
print("Last item " + thisList[-1])

#Range
print(thisList[2:6])

if "apple" in thisList:
    print("Yes")


# The insert() method inserts an item at the specified index, we can insert new items without index
thisList.insert(2,"watermelon")
print(thisList)