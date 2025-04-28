

marks = [3,5,6,"These are marks",True,4,5,7,8,9 ]
print(marks)
print(type(marks))

print(marks[0])
print(marks[1])

print(marks[-3]) #negitive indexing

print(marks[len(marks)-3]) #positive indexing
print(marks[5-3])
print(marks[2])


if 7 in marks:
    print("Yes")
else:
    print("no")

if 5 in marks:
    print("Yes")
else:
    print("No")

if "6" in marks:
    print("Yes")
else:
    print("No")                   

if "are" in "These are marks":
    print("yes")
else:
    print("NO") 

print(marks[1:8])

print(marks[1:8:2])   #It will be printing 1:8 and skipping every 2nd value

print(marks[1:]) #will use len of marks 1:len(marks)

print(marks[:6]) #will use "0", 0:6


lst = [i for i in range(4)]   #creating a list
print(lst)

lst1 = [i*i for i in range(10)if i%2 == 0]
print(lst1)

