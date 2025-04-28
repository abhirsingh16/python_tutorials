
# def average(a=9,b=1):
#     print("The average is ", (a+b)/2)

# average()

# average(3,4)

# average(b=4)

# average(b=11, a =22)


# def avg(*num):     #  '*' for converting name in tuple
#     print(type(num))
#     sum = 0
#     for i in num:
#         sum = sum + i
#     print("Averge is", sum/len(num))    

# avg(5,6)    
# avg(10,11,12)

# def name(**name):         # '**' for converting name in dict  
#     print(type(name))
#     print("Hello,", name["fname"],name["mname"],name["lname"])

# name(mname = "Honey",fname="YO YO",lname="Singh")



def avg(*num):     #  '*' for converting name in tuple
    print(type(num))
    sum = 0
    for i in num:
        sum = sum + i
    return sum/len(num)

z = avg(5,6)    
print(z)

x = avg(10,11,12)
print(x)
