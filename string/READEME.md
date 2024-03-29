## STRING

We've covered a bunch of String class methods already, so let's keep building on those and run down some more advanced methods.
The string method lower will return the string with all characters changed to lowercase. The inverse of this is the upper method, which will return the string all in uppercase. Just like with previous methods, we call these on a string using dot notation, like "this is a string".upper(). This would return the string "THIS IS A STRING". This can be super handy when checking user input, since someone might type in all lowercase, all uppercase, or even a mixture of cases.
You can use the strip method to remove surrounding whitespace from a string. Whitespace includes spaces, tabs, and newline characters. You can also use the methods  lstrip and rstrip to remove whitespace only from the left or the right side of the string, respectively.
The method count can be used to return the number of times a substring appears in a string. This can be handy for finding out how many characters appear in a string, or counting the number of times a certain word appears in a sentence or paragraph.
If you wanted to check if a string ends with a given substring, you can use the method endswith. This will return True if the substring is found at the end of the string, and False if not.
The isnumeric method can check if a string is composed of only numbers. If the string contains only numbers, this method will return True. We can use this to check if a string contains numbers before passing the string to the int() function to convert it to an integer, avoiding an error. Useful!
We took a look at string concatenation using the plus sign, earlier. We can also use the join method to concatenate strings. This method is called on a string that will be used to join a list of strings. The method takes a list of strings to be joined as a parameter, and returns a new string composed of each of the strings from our list joined using the initial string. For example, " ".join(["This","is","a","sentence"]) would return the string "This is a sentence".
The inverse of the join method is the split method. This allows us to split a string into a list of strings. By default, it splits by any whitespace characters. You can also split by any other characters by passing a parameter.

String Formatting
 
You can use the format method on strings to concatenate and format strings in all kinds of powerful ways. To do this, create a string containing curly brackets, {}, as a placeholder, to be replaced. Then call the format method on the string using .format() and pass variables as parameters. The variables passed to the method will then be used to replace the curly bracket placeholders. This method automatically handles any conversion between data types for us. 
If the curly brackets are empty, they’ll be populated with the variables passed in the order in which they're passed. However, you can put certain expressions inside the curly brackets to do even more powerful string formatting operations. You can put the name of a variable into the curly brackets, then use the names in the parameters. This allows for more easily readable code, and for more flexibility with the order of variables.
You can also put a formatting expression inside the curly brackets, which lets you alter the way the string is formatted. For example, the formatting expression {:.2f} means that you’d format this as a float number, with two digits after the decimal dot. The colon acts as a separator from the field name, if you had specified one. You can also specify text alignment using the greater than operator: >. For example, the expression {:>3.2f} would align the text three spaces to the right, as well as specify a float number with two decimal places. String formatting can be very handy for outputting easy-to-read textual output.
String Reference Cheat Sheet
In Python, there are a lot of things you can do with strings. In this cheat sheet, you’ll find the most common string operations and string methods.
String operations
•	len(string) Returns the length of the string
•	for character in string Iterates over each character in the string
•	if substring in string Checks whether the substring is part of the string
•	string[i] Accesses the character at index i of the string, starting at zero
•	string[i:j] Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.
String methods
•	string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
•	string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
•	string.count(substring) Returns the number of times substring is present in the string
•	string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
•	string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
•	string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
•	string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
•	delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter


