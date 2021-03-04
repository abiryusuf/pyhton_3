
# Function is block of codes and it will execute when it is called

# def is keyword for python function
def myFunction():
    print("Hello Funtion ")

myFunction()

# Number of arguments 
def argFunction(fName, lName, age):
    return("First Name " + fName + " Last Name " + lName + " age " + str(age))

print (argFunction("Abir", "Yusuf", 32))
print(argFunction("Mim", "Madiha", 4))

# Arbitrary arguments: If I don't know how many arguments that will pass, I can
# use (* arg) before parametars. 
def name(*child):
    print("The total children is " + child[3])
 
name("abir", "yusuf", "mukter", "arafat")

def calculate(d):
    q = 3.14
    z = q *(d**2)
    print(z)

calculate(5)

fruits = ["apple", "banna", "cherry"]
def my_function(food):
    for x in food:
        print(x)
my_function(fruits)

# def convert_distance(miles):

#  km = miles * 1.6  # approximately 1.6 km in 1 mile
# return km
# miles = 55   
# km = convert_distance(miles)
# print("The distance in kilometers is: " + str(km))
# print("The round-trip in kilometers is: " + str(km * 2))

def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))