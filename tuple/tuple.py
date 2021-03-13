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

# def animal_function(n):
# 	for x in n:
# 		char += len(x)
# 	return "Total characters: {}, Average length: {}".format(char, char/len(x))
# print(animal_function(animals))
# print the list with index

winners = ["Abir", "Yusuf", "Mim"]

for index, person in enumerate(winners):
    print("{} - {}".format(index+1, person))

# Try out the enumerate function for yourself in this quick exercise. 
# Complete the skip_elements function to return every other element from the list,
# this time using the enumerate function to check if an element is on an even position or an odd position.
def skip_elements(elements):
	# code goes here
	ele = []
	for index, element in enumerate(elements):
		if index % 2 == 0:
			ele.append("{}".format(element))
	return ele

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


def fullName(people):
	result = []
	for email, name in people:
		result.append("{} <{}>".format(name, email))
	return result
print(fullName([("abir@gmail.com", "abir")]))