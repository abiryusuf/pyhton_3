x = ["Now", "we", "are", "Cooking"]

print(type(x))

# check the length
print(len(x))

# check the text
y = "are" in x
print(y)

# check the index
print(x[2])

# slincing
print(x[1:3])

def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

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


