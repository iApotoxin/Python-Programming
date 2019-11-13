Language = {'Kotlin', 'Java', 'Kotlin', 'Swift', 'Java', 'React'}
print(Language)
print(type(Language))

#------------------------------------------------------------------

setA = set('welcome to python programming')
setB = set('tizcomm')
setC = set('122546555788941')

print(setA)
print(setB)
print(setC)

#------------------------------------------------------------------

S1 = set((1,1,2,3,5,8,13,15))
S2 = set((2,3,5,7,11,13))

# Union
print("Set S1 :",S1)
print("Set S2 :",S2)
print("Set S1 | S2 :",S1|S2)

# Intersection
print("Set S1 :",S1)
print("Set S2 :",S2)
print("Set S1 & S2 :",S1&S2)

#Difference - สมาชิกซ้ายทั้งหมดที่ไม่อยู่ในขวา
print("Set S1 :",S1)
print("Set S2 :",S2)
print("Set S1 - S2 :",S1-S2)

#Symmetric Difference - สมาชิกซ้ายและขวาทั้งหมด ที่ไม่ intersection กัน หรือไม่ซ้ำกัน
print("Set S1 :",S1)
print("Set S2 :",S2)
print("Set S1 ^ S2 :",S1^S2)

#------------------------------------------------------------------
# Set Comparison Operators

mySet1 = {1, 2, 3, 5, 8, 13} 
mySet2 = {2, 3, 5, 7, 11, 13}
mySet3 = {1, 2, 3, 5, 8, 13}
mySet4 = {5,8}

print("In Operators :", 3 in mySet1)
print("Not In Operators :", 7 not in mySet1)

print("mySet1 < mySet2 :", mySet1 < mySet2)
print("mySet1 > mySet2 :", mySet1 > mySet2)
print("mySet1 = mySet2 :", mySet1 == mySet2)

print("mySet1 < mySet3 :", mySet1 < mySet3)
print("mySet1 > mySet3 :", mySet1 > mySet3)
print("mySet1 = mySet3 :", mySet1 == mySet3)

print("mySet1 > mySet4 :", mySet1 > mySet4)