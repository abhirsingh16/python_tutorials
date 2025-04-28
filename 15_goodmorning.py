import time

# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestampH =int( time.strftime('%H'))
# print(timestampH)
# timestampM = int(time.strftime('%M'))
# print(timestampM)
# type(timestamp)

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