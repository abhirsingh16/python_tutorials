num = int(input("Enter the number: "))

if(num < 0):
    print("The number is less than 0")
elif(num > 0):
    if(num <=10):
        print("The number is between 0-10")
    elif(num > 10 and num <=20):
        print("The number is between 10-20")
    else:
        print("The number is greater than 20")
else:
    print("The number is 0")                
    