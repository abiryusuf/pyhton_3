# Tuple
# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round bracke

# using format
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
char = 0

for animal in animals:
    char += len(animal)
print("Total characters: {}, Average Length: {}".format(char, char/len(animal)))