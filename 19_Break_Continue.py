# for i in range(12):
#     if(i==10):
#         break
#     print("5 X ",i+1,"=",5*(i+1))
# print("Table of 5")       



# Break means exit the loop
# Continue means exit the iteration

for i in range(12):
    if(i==10):
        print("Skip 5 X", (i+1)) 
        continue
    print("5 X ",i+1,"=",5*(i+1))



# Do while loop for python------------------

i = 0
while True:
    print(i)
    i = i+1
    if(i > 10):
        break