# Total Number from list
number = [1, 4, 5, 6]
def totalSum(n):
    sum = 0
    avg = 0
    for value in n:
        sum += value
        avg += 1
    return sum
print("Total {}".format(totalSum(number)))
print("Total {}".format(totalSum(number/avg)))


# Total with dictionary
groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99,
 "bread": 4.59, "coffee": 6.99, "milk": 3.39, "eggs": 2.98, 
 "cheese": 5.44}

def total(n):
     sum = 0

     for value in n:
         sum += n[value]
     return round(sum, 2)
x = total(groceries)
print("Total " + str(x))

# duplicate value 
number = [1, 3, 4, 5, 5, 6, 6]
def duplicate(n):
    dup = []
    seen = set()

    for x in n:
        if x not in seen:
            dup.append(x)
            seen.add(x)
    return dup

print("Not allow duplicate value {}".format(duplicate(number)))

# 5 = 1 + 2 + 3 + 4 + 5 = 15
# using loop with range 

def sumAdd(n):
    sum = 0
    avg = 0

    for x in range(1, n + 1):
        sum += x
        avg += 1
    return sum
print("Total of number {}".format(sumAdd(5)) )

def factorial(n):
    sum = 1

    for x in range(1, n + 1):
        sum = sum * x
    return sum

print("Factorial {}".format(factorial(5)))

