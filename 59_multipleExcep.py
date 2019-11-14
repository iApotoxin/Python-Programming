import sys

try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
except IOError:
    print("I/O error")
except ValueError:
    print("No valid integer in line.")
except:
    print("Unexpected error")

try:
    fh = open("testfile", "r")
    fh.write("This is my file for exception handling!!")
except(IOError, ValueError, SystemError):
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()