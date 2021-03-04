print("cat" + "Cat")

def userName(username):
    if len(username) < 3:
        print("Invalied username")
    else:
        print("Valid User Name")
userName("ab")   

def evenNum(num):
    if(num % 2 == 0):
        print("It is even number")
    else:
        print(" it is odd number")    

evenNum(9)

# if else
a = 40
b = 50

if(a>b):
    print("a is greater than b")
elif a == b:
     print("a and b is equel")   
else:
    print("a is less than b")

print((2**2) == 4)

number = 10
if number > 11: 
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)


print(11%5)