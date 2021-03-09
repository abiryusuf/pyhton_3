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