def modifyVar1():
    var1, var2 = 10, 20
    print("Local variables of modifyVar1 are var1 ",(var1))
    print("Local variables of modifyVar1 are var2 ",(var2))
print(modifyVar1())

#--------------------------------------------------------------
def modifyVar2(var1, var2):
    var1 = 50
    print("Local variables of modifyVar2 are var1 ",(var1))
    print("Local variables of modifyVar2 are var2 ",(var2))
print(modifyVar2(5, 10))

#-------------------------------------------------------------
var1, var2 = 5, 5

def modifyVar3(var1):
    global var2
    var2 = 3
    return var1 * var2

print("Var1 and Var2 in main program = %d, %d"%(var1, var2))
modifyVar3(var1)
print("Var1 and Var2 in main program = %d, %d"%(var1, var2))

#-------------------------------------------------------------

def modifyVar4():
    global var1
    var1 = var1 ** 2
    return

modifyVar4()
print("Var1 and Var2 in main program = %d, %d"%(var1, var2))
