myDict = {'Name': 'Sompong', 'Age': 45, 'Class': 'First'}
print("Original Dictionary :",myDict)

del myDict['Class']; 
print("After Removed 'Class' :",myDict)

myDict.clear(); 
print("After Cleared All :",myDict)

del myDict ; 
print("After Deleted in Memory :",myDict)