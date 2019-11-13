myList1 = [1,2,3,4,5]
myList2 = [9,8,7,6,5]
myList3 = [9,8,7,6,5]
myList4 = [8,9,7,6,5]
myList5 = [8,9,6,7,5]
myList6 = [5,10]

print("myList1 = myList2 :", myList1 == myList2)
print("myList1 < myList2 :", myList1 < myList2)
print("myList2 >= myList1 :", myList2 >= myList1)

print("myList2 == myList3 :",myList2 == myList3)
print("myList3 == myList4 :",myList3 == myList4)
print("myList3 > myList4 :",myList3 > myList4)

print("myList4 == myList5 :",myList4 == myList5)
print("myList4 > myList5 :",myList4 > myList5)

print("Operation - in :", 3 in myList6)
print("Operation - not in :", 3 not in myList6)