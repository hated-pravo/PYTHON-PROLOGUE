s = {1,2,3}
print(s , type(s))

s.add(56)
print(s)

''' properties of sets
1) sets are unordered #element order doesn"t matter
2) sets are unindexed #cannot access the element
3) there is no way to change items in set
4) sets cannot contains duplicate values '''

print(len(s))
s.remove(56)
print(s)

s.clear()
print(s)

a = {1 , 2 ,3 ,4}
b = { 2, 5, 6}

print(a.union(b))
print(a.intersection(b))


c = a - b
print(c)

d = b - a
print(d)