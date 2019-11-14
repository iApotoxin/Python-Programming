total = 0;    # Global Variable

def sum(arg1, arg2):
    total = arg1 + arg2  #Local Variable
    print ("Total of Local Variable inside Function : ", total)
    return total

sum(5, 10)

print ("Total of Global Variable outside Function : ", total)