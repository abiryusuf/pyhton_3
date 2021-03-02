
# Function is block of codes and it will execute when it is called

# def is keyword for python function
def myFunction():
    print("Hello Funtion ")

myFunction()

# Number of arguments 
def argFunction(fName, lName):
    return(fName + " " + lName)

print(argFunction("Abir", "Yusuf"))

# Arbitrary arguments: If I dont knoe how many arguments that will pass, I can
# use (* arg) before parametars. 
def name(*child):
    print("The total children is " + child[3])
 
name("abir", "yusuf", "mukter", "arafat")

def calculate(d):
    q = 3.14
    z = q *(d**2)
    print(z)

calculate(5)