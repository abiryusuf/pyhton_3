# The format_address function separates out parts of the address string into new strings: house_number and street_name, 
# and returns: "house number X on street named Y". 
# The format of the input string is: numeric house number, followed by the street name which may contain numbers, 
# but never by themselves, and could be sever
# For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.

def format_address(address_string):
  # Declare variables
  house_number = ' '
  street_number = " "
  # Separate the address string into parts
  x = address_string.split()
  # Traverse through the address parts
  for y in x:
    # Determine if the address part is the
    if y.isdigit():
    # house number or part of the street name
       house_number = y
  # Does anything else need to be done 
    else:
      street_number += y
      street_number += " "
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(house_number, street_number)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

# 2
# The highlight_word function changes the given word in a sentence to its upper-case version. 
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line?
def highlight_word(sentence, word):
	return(sentence.replace(word, word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


# 3
# A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom.
#  Drew was the first one to note which students arrived, and then Jamie took over. 
# After the class, they each entered their lists into the computer and emailed them to the professor, 
# who needs to combine them into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order. Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.

def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  new_list = list2
  for name in reversed(range(len(list1))):
    new_list.append(list1[name])
  return new_list
  
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))




# Question 7
# Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or punctuation.
#  Upper case should be considered the same as lower case. For example, count_letters("This is a sentence.") 
# should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    if letter not in result:
      result[letter.lower()] = 1
    # Add or increment the value in the dictionary
    else:
      result[letter.lower()] += 1
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}