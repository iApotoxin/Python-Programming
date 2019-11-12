# Integer
print(type(500))
print(type(200*3))
print(type(0xAB3))

#-----------------------------------------------

# Float
print(type(5.5))
print(type(100/5))

#-----------------------------------------------

# Complex
complexNum = 90.5 + 2.5j
print (complexNum)
print (type(complexNum))

#-----------------------------------------------

# Forcing a Number Type - to Integer
numInt1 = int("20")
numInt2 = int(5.75)

print(numInt1)
print(type(numInt1))

print(numInt2)
print(type(numInt2))

numResultInt = numInt1 * numInt2
print("Result of Forcing to Integer is : ",numResultInt)
print(type(numResultInt))

#-----------------------------------------------

# Forcing a Number Type - to Float
numFloat1 = float("20.5")
numFloat2 = float(5)

print(numFloat1)
print(type(numFloat1))

print(numFloat2)
print(type(numFloat2))

numResultFloat = numFloat1 + numFloat2
print("Result of Forcing to Float is : ",numResultFloat)
print(type(numResultFloat))