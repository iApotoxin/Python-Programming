# Modified List

mySubject = ['Java', 'Swift', 'C#', 'React']

print ("Old Value [0] : ",mySubject[0])
mySubject[0] = 'Kotlin'
print ("New Value [0] : ",mySubject[0])

print("List Changed : ", mySubject)

del mySubject[2]   # delete element
print("List Deleted : ", mySubject)

print("mySubject[0] : ",mySubject[0])
print("mySubject[1] : ",mySubject[1])
print("mySubject[2] : ",mySubject[2])

del mySubject      # delete all element
print(mySubject)
