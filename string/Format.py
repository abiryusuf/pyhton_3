
# We can not combaine string and int
# by using formate method we can combine str and int

# age = 32
# place = "nY"

# name = " I am Abir, and My age is {} and Living {}"

# print(name.format(age, place))

# q = 3
# item = 653
# price = 50.89

# myOrder = "I want to pay {2} dollars for {0} pieces of item {1}"
# print(myOrder.format(q, item, price))

name = "Abir"
number = len(name) * 3

print("Hello {}, Your lucky number is {}". format(name, number))

price = 8.5
with_tax = price * 1.09
print(price, with_tax)

print("Base Price: ${:.2f}. with Tax: ${:.2f}".format(price, with_tax))

def to_celsius(x):
    return (x-32)*5/9
for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
