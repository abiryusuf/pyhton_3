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