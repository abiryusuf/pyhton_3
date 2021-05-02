def reverseString(str):
    res = ""
    str1 = str.replace(" ", "").lower()

    for reverse in str1:
        if reverse not in res:
            res = reverse + res
    return res
print(reverseString("abir"))

# def reverseSentence(str):
#     return " ".join(reversed(str.split()))
# print(reverseSentence("I am abir"))

def reverseSentence(str):

    word = []
    lenght = len(str)
    spaces = [" "]
    i = 0

    while i < lenght:
        if str[i] not in spaces:
            start = i
            while i < lenght and str[i] not in spaces:
                i += 1
            word.append(str[start:i])
        i += 1
    return "".join(reversed(str.lower()))
print(reverseSentence("I am abir"))

num = [1, 4, 5, 6, 7, 8]
def skip_element(n):
    elements = []
    i = 0
    for x in n:
        if i % 2 == 0:
            elements.append(x)
        i += 1
    return elements
print(skip_element(num))

