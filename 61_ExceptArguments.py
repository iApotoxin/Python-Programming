def temp_convert(var):
    try:
        return int(var)
    except ValueError as Args:
        print ("Argument doesn’t contain numbers\n", Args.args)

temp_convert("xyz")