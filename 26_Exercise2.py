


timestampH = int(input("Enter the time in hours: "))
print(timestampH)

if(timestampH > 0 and timestampH < 12):
    print("Good Morning")
elif(timestampH>=12 and timestampH<=16):
    print("Good afternoon")
elif(timestampH>16 and timestampH <=21):
    print("Good Evening")
else:
    print("Good Night")        