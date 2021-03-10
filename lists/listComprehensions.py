# Let us create new lists based on sewuences or ranges
multiples = []

for x in range(1, 20):
    multiples.append(x*7)
print(multiples)

multiple = [x*7 for x in range(1,11)]
print(multiple)

winners = ["Abir", "Yusuf", "Mim"]

for index, person in enumerate(winners):
    print("{}. - {}".format(index+1, person))

# def mul(name):
#     res = []
#     for index, person in enumerate(name):
#          res.append ("{}".format(index+1, person))
#     return res

# print(nu)

