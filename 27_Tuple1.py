# List vs Tuple 
# Conformable : สามารถเก็บข้อมูลต่างประเภทกันได้ในตัวแปรเดียวกันได้
# Difference : Tuple ใช้สาหรับเก็บข้อมูลที่มีค่าคงที่ไม่มีการเปลี่ยนแปลง ไม่สามารถเพิ่มหรือลบข้อมูลได้
# Tuple สามารถเข้าถึงข้อมูลได้เร็วกว่า List

myTuple1 = (50, 35.55)
print('Value of myTuple1: ', myTuple1)
print('Type of myTuple1: ',type(myTuple1))

#---------------------------------------------------------------
myTuple2 = ('Database', 'Data Warehouse')
print('Value of myTuple2: ', myTuple2)
print('Type of myTuple2: ',type(myTuple2))

#---------------------------------------------------------------
myTuple3 = (20, 15.75, 'Python Programming',"R Programming")
print('Value of myTuple3: ', myTuple3)
print('Type of myTuple3: ',type(myTuple3))

#---------------------------------------------------------------
myTuple4 = (myTuple1, myTuple2, myTuple3)
print('Value of myTuple4: ', myTuple4)
print('Type of myTuple4: ',type(myTuple4))

#---------------------------------------------------------------
myTuple5 = myTuple1 + myTuple2
print('Value of myTuple5: ', myTuple5)
print('Type of myTuple5: ',type(myTuple5))

#---------------------------------------------------------------
myTuple6 = ()   #Empty Tuple
print('Value of myTuple6: ', myTuple6)
print('Type of myTuple6: ',type(myTuple6))

#---------------------------------------------------------------
#Importance
myTuple7 = (50)
myTuple8 = (50,)

print('Value of myTuple7: ', myTuple7)
print('Type of myTuple7: ',type(myTuple7))

print('Value of myTuple8: ', myTuple8)
print('Type of myTuple8: ',type(myTuple8))

#---------------------------------------------------------------
myTuple9, myTuple10 = (100, 500)

print('Value of myTuple9: ', myTuple9)
print('Type of myTuple9: ',type(myTuple9))

print('Value of myTuple10: ', myTuple10)
print('Type of myTuple10: ',type(myTuple10))

#---------------------------------------------------------------
myTuple11, myTuple12 = (100, 500), (800, 900)

print('Value of myTuple11: ', myTuple11)
print('Type of myTuple11: ',type(myTuple11))

print('Value of myTuple12: ', myTuple12)
print('Type of myTuple12: ',type(myTuple12))

#---------------------------------------------------------------
myTuple13, myTuple14 = ((1, (2, (3, 4))), (((5, 6), 7), 8))

print('Value of myTuple13: ', myTuple13)
print('Type of myTuple13: ',type(myTuple13))

print('Value of myTuple14: ', myTuple14)
print('Type of myTuple14: ',type(myTuple14))

#---------------------------------------------------------------
myTuple15, myTuple16 = (100, 200, 300)

print('Value of myTuple15: ', myTuple15)
print('Type of myTuple15: ',type(myTuple15))

print('Value of myTuple16: ', myTuple16)
print('Type of myTuple16: ',type(myTuple16))

#ValueError: too many values to unpack
