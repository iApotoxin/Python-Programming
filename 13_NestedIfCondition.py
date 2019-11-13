certScore = int(input("Enter your certified score :"))

if certScore < 700:
    print("You not pass certified exam !!!")
    if certScore < 300:
        print("Please join to Training, Bootcamp and Book")
    elif certScore < 500:
        print("Please join to Bootcamp and Book")
    elif certScore < 700:
        print("Please join to Bootcamp")  
elif certScore < 900:
    print("You are Professional Level !!!")
else:
    print("You are Expert Level !!!")  