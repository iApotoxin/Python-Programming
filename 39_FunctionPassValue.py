def language(myList):
    myList.append(['Python','R','Java','SQL'])
    print ("Values Inside Function: ", myList)
    return

myList = ['Kotlin','Swift','React','Xamarin']

language(myList)
print ("Values Outside Function: ", myList)

#pass value to function in Python have "Pass by reference" Only
#Not support "Pass by value"

#keyword arguments