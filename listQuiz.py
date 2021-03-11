
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames =[]
for name in filenames:
    if name.endswith(".hpp"):
        name = name.replace("hpp", "h")
        newfilenames.append(name)
    else:
        newfilenames.append(name)
print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# 2nd way list comprenhension 
newfilenames = [name.replace("hpp", "h") if name.endswith("hpp") else name for name in filenames]
print(newfilenames)