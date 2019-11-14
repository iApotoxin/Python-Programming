while True:
    try:
        n = int(input("Please Enter an Integer: "))
        break
    except ValueError:
        print("No Valid Integer! Please try again ...")
print("Great, you successfully entered an integer!")

#ValueError (ข้อมูลผิดประเภท)