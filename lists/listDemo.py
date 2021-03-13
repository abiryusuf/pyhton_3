items = ['rice', 'suger', 'salt', 'fish']
# Add by using append method that will add end of the list
items.append('milk')
print(items)
# add item by insert method that will add based on the index 
items.insert(3, 'banana')
print(items)

print(len(items))

# index
print(items[3])

# range 
print(items[1:3])

# check
x = 'rice' in items
print(x)

# add new item by using append method
y = items.append("milk")
print(y)

def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing


def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for x in elements:
		# Does this element belong in the resulting list?
		if i%2==0:
			# Add this element to the resulting list
			new_list = new_list + [x]
		# Increment i
		i+=1

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


