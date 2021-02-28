
# We can not combaine string and int
# by using formate method we can combine str and int

age = 32
place = "nY"

name = " I am Abir, and My age is {} and Living {}"

print(name.format(age, place))

q = 3
item = 653
price = 50.89

myOrder = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myOrder.format(q, item, price))