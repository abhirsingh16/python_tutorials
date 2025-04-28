s1 = {1,2,5,6}
s2 = {3,4,7}

# Union s1 & s2
print(s1.union(s2))

print(s1, s2)

s1.update(s2)

print(s1)

print(s1.intersection(s2))

# symmetric diff

s3 = s1.symmetric_difference(s2)
print(s3)

s1 = {1,2,5,6}
s2 = {3,4,7}

print(s1.isdisjoint(s2))

print(s1.issuperset(s2))

s1.add(10)

print(s1)

s1.remove(1)

print(s1)

s1.discard(1)

print(s1)

s3 = s1.pop()

print(s3)

del(s3)

print(s3)
