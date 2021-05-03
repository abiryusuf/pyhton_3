def common_element(a, b):
    num1 = 0 
    num2 = 0
    res = []

    while num1 < len(a) and num2 < len(b):
        if a[num1] == b[num2]:
            res.append(a[num1]) and res.append(b[num2])
            num1 += 1
            num2 += 1
        elif a[num1] < b[num2]:
            num1 += 1
        else:
            num2 += 1
    return res
print(common_element([1,3,4,5], [1,3,4,6]))