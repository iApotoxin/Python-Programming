numA = 20
numB = 20
numC = 30

if (numA is numB):
    print("True: numA and numB have same identity")
else:
    print("False: numA and numB not have same identity")

#------------------------------------------------------------

if (numB is numC):
    print("True: numB and numC have same identity")
else:
    print("False: numB and numC not have same identity")

#------------------------------------------------------------

if (numA is not numC):
    print("True: numA and numC not have same identity")
else:
    print("False: numA and numC have same identity")