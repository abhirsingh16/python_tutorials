
l = [10,9,8,1,2,3,4,5]
print(l)

l.append(14)
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

print(l.index(1))

print(l.count(1))

m = l.copy()

m[0] = 0
print(l)

print(m)

l.insert(1,999)
print(l)

n = [900,122,131]

l.extend(n)
print(l)

a=[1,2,3]
b=[5,6,7]

k = a+b
print(k)