# Dictionaries are used to store data values in key : value paries 
# A dictionries is collection which is ordered, changeable and does not allow duplicate values
info = {
    "Name": "Abir",
    "Age": 32,
    "Adress": "NY"
}

print(info)

# Index
x = info["Name"]
print(x)

# check 
y = "Age" in info
print(y)

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
# add 
toc ["Epilogue"] = 39
# change
toc["Chapter 3"] = 24
print(toc)

file_counts = {"jpg": 10, "text": 14, "csv": 2, "py": 23}
for x in file_counts:
    print(x)
# need to print with index
for ext, amount in file_counts.items():
    print("There are {} files with the .{} extention".format(amount, ext))


# just need to print values or keys
# using keys() method or values
file_counts.items()
print(file_counts)

# print values by values method
values = file_counts.values()
print(values)

for value in file_counts.values():
    print(value)

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}

for key, value in cool_beasts.items():
    print("{} have {}".format(key, value))

    
sen = "I aam Abir"
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result
print(count_letters(sen))

def count_word(n):
    res = {}
    for x in n:
        if x in res:
            res[x] += 1
        else:
            res[x] = 1
    return res
print(count_word(sen))