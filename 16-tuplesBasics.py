a = 1, 2, 3, 4, 5
b = [6, 7, 8, 9, 10]
c = (21, 22, 23, 24, 25)

print(a , type(a))
print(b , type(b))
print(c , type(c))


tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if  342 in tup:
  print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)

#Operations in Tuples

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(311)
# res = tuple1.index(3, 4, 8)
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)