# with the while loop we can execute a set of statement as long as a condition is true
i = 1

while i < 6:
    print(i)
    if i == 4:
        # Break statement we can stop the loop even if the while condition is true
     break
    i += 1
i = 0
while i < 8:
    i += 1
    if i == 9:
        continue
    print("continue " + str(i))

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt: " +str(x))
        x += 1
    print("Done")    

attempts(5)

x = 1
sum = 0

while x < 10:
    sum += x
    x += 1
    print(sum)

product = 1
x = 1
while x < 10:
    product = product * x
    x += 1
    print(product)

def print_range(start, end):
    n = start
    while(n<=end):
        print(n)
        n += 1

print_range(5, 1)

