# A for loop is used for iterating over a sequence (that is either a list, a tuple)

# With the for loop we can execute a set of statements.

color = ["Red", "Black", "Yellow", "Green"]

for x in color:
    print(x)

# Looping Through a String
for y in "abir":
    print("String the loop " + str(y))

# With break statement we can stop the loop before it has looped through all the items

for z in color:
    print("Break: " + str(z))
    if z == "Yellow":
        break
    # print(z) # print before the condition item

# continue statement we can stop the current iteration of the loop and continue the next

for c in color:
    if c == "Yellow":
        continue
    print("Continue: " + str(c))


# Range
# It is possible to specify the starting value by adding a parameter

for t in range(1, 3):
    print("The starting value: " + str(t))

#it is possible to specify the increment value by adding a third parameter

for x in range(1,10,2):
    print(x)

# else 
for x in range(1,8):
    if x == 3:
        break
    print(x)
else:
    print("Finished")

# def square(n):
#     return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += n * n
    return sum

print(sum_squares(10)) # Should be 285

values = [23, 54, 56, 37, 48]
sum1 = 0
length = 0
for value in values:
    sum1 += value
    length += 1
print("Total sum: " + str(sum1) + " - Average: " + str(sum1/length))

# using format
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
char = 0
for animal in animals:
     char += len(animal)
print("Total characters: {}, Average length: {}".format(char, char/len(animal)))
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

# To quickly recap the range() function when passing one, two, or three parameters:

# One parameter will create a sequence, one-by-one, from zero to one less than the parameter.
# Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.
# Three parameters will create a sequence starting with the first parameter and stopping before the second parameter, but this time increasing each step by the third parameter.