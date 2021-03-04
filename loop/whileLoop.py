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
    if i == 3:
        continue
    print("continue " + str(i))