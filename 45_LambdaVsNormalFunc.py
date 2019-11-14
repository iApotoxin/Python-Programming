# Lambda vs normal function in same name

def func(x, y, z): 
    return x + y + z

func = lambda x, y, z: x - y - z

print("Calling Function :", func(2, 2, 2))
print("Calling Function :", func(2, 3, 4))

#เมื่อมีการประกาศฟังก์ชัน def และ lambda เหมือนกัน 
#python จะให้ความสำคัญกับ lambda มากกว่า