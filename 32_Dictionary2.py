numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9); 
chars = ('A', 'B', 'C', 'D', 'E', 'F'); 

myDict = {}; 
myDict['001'] = 'John'; 
print("One to One Dictionary :",myDict)

myDict['001'] = numbers; 
print("One to Many Dictionary :", myDict)

myDict = {}
myDict[numbers] = 'Python'; 
print("Many to One Dictionary :", myDict)

myDict[numbers] = chars; 
print("Many to Many Dictionary :", myDict)