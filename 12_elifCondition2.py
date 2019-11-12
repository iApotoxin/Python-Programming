score = float(input("Enter your score :"))
grade = "Grade : "

if score >= 80:
    print(grade + "A")
elif score >= 70:
    print(grade + "B")
elif score >= 60:
    print(grade + "C")
elif score >= 50:
    print(grade + "D")
else:
    print(grade + "F") 
