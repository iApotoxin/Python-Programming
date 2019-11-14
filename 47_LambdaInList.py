myList = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]

for f in myList:
    print(f(3))

print(myList[0](5))
print(myList[1](5))
print(myList[2](5))