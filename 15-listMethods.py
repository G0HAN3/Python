l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
# l.append(7)
# l.sort(reverse=True)
# l.reverse()
# print(l.index(1))
# print(l.count(1))
# m = l.copy()
# m[0] = 0
# l.insert(1, 899)
m = [900, 1000, 1100]
k = l + m
# print(k)
# l.extend(m)
print(l)


a = [1,5,10,15,20,25]
print(a)

c = a.copy() #this actually creates a copy of the list in memory
c[0]=0
print(a)

b = a   #this just adds another reference to the same list in memory
a[0] = 0
print(a)