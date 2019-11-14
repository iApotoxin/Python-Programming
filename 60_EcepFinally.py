try:
    fh = open("myfile", "r")
    fh.write("This is my file for exception handling!!")
except:
    print("IO Error with File")
else:
    print("Written content in the file successfully")
finally:
    print("This file is closed completely")
   