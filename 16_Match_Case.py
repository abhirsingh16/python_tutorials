
x = int(input("Enter the number: "))

match x:
    case 0:
        print("Number is 0")
    case 2:
        print("The number 2")
    case _ if x < 10:
        print("Number is greater than 2 and less than 10:",)
    case _ :
        print("Number is out of scope:", x)
