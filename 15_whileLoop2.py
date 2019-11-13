Counter = 1
Summary = 0.0

print(" ::: Please Type 0 or 0.0 for Exit Program :::")

Num = float(input("Enter a Number :"))

while Num != 0 or Num != 0.0:
    Summary += Num
    Average = Summary / Counter
    Counter += 1
    print("Average Value is : ", Average)
    Num = float(input("Enter a Number :"))   

print("End of Program")