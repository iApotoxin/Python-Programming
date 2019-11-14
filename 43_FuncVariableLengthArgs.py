#Variable-length arguments คือ อาร์กิวเมนต์ที่สามารถบรรจุข้อมูลไว้ได้แบบไม่จำกัดจำนวน

def printinfo(arg1, *vartuple):
    print ("Output of formal arg is : ", arg1)
    for var in vartuple:
        print ("Output of virtuple arg is : ",var)
    return

printinfo(10)
printinfo(70, 60, 50)