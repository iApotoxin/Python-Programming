#String

varString1 = 'Welcome to'

print ("varString1[0]: ", varString1[0])
print ("varString1[1]: ", varString1[1])
print ("varString1[2]: ", varString1[2])
print ("varString1[3]: ", varString1[3])
print ("varString1[4]: ", varString1[4])
print ("varString1[5]: ", varString1[5])
print ("varString1[6]: ", varString1[6])
print ("varString1[7]: ", varString1[7])
print ("varString1[8]: ", varString1[8])
print ("varString1[9]: ", varString1[9])

#IndexError: string index out of range
#print ("varString1[10]: ", varString1[10])

#-----------------------------------------------

varString2 = "Python Programming"

print ("varString2[1:5]: ", varString2[1:5])
print ("varString2[0:8]: ", varString2[0:8])

#-----------------------------------------------

varString3 = "Python"

print ("varString3[-1]: ", varString3[-1])
print ("varString3[-2]: ", varString3[-2])
print ("varString3[-3]: ", varString3[-3])
print ("varString3[-4]: ", varString3[-4])
print ("varString3[-5]: ", varString3[-5])
print ("varString3[-6]: ", varString3[-6])

print("String Array Value 1: ", varString3[2])
print("String Array Value 2: ", varString3[3:5])
print("String Array Value 3: ", varString3[3:6])

#Start at 0 to 5 and step 2
print("String Array Value 4: ", varString3[0:5:2])

#Start to 5
print("String Array Value 5: ", varString3[:5])

#Start 2 to End
print("String Array Value 6: ", varString3[2:])

#Start Start to End , step 2
print("String Array Value 7: ", varString3[::2])

#Start End to Start , step 2
print("String Array Value 8: ", varString3[::-2])