def functionName(level):
    if level < 1:
        raise ("Invalid level!", level)
        print("The code would not be executed")
    print("End Program")

functionName(5)
functionName(0)