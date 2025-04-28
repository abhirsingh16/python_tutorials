#Strings are immutable

a = "!!!!!!Singh  !!!!!!!!Singh"

print(len(a))

print(a.upper())     #-------prints in capital

print(a.lower())     #-------prints in lower case

print(a.rstrip("!"))   #--------removes ! from ending

print(a.replace("Singh","Abhi"))

print(a.split(" "))

blog = "intro to PY"

print(blog.capitalize())

print(blog.center(25))

print(a.count("Singh"))

print(a.endswith("!!"))

print(a.endswith("h",5,11))    #the strin ends with "h"

print(a.find("i"))

print(a.index("g"))

b="123Abhi"

print(b.isalnum())

print(b.isalpha())

print(a.isprintable())

print(a.isspace())

print(b.istitle())

print(b.title())