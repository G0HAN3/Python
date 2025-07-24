# Numeric data: int, float, complex
# int: 3, -8, 0
# float: 7.349, -9.0, 0.0000001
# complex: 6 + 2i

a = complex(8, 2)
print("The type of", a, "is", type(a))
b = True
print("The type of", b, "is", type(b))
c = "Harry"
print("The type of", c, "is", type(c))
d = None
print("The type of", d, "is", type(d))

print()

# list: A list is an ordered collection of data with elements separated by a 
# comma and enclosed within square brackets. Lists are mutable and can be modified after creation.
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
# outer brackets tell python that u r creating a list
print(list1)
print()

# Tuple: A tuple is an ordered collection of data with elements separated by a 
# comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"), 50)
tuple2 = "parrot", "sparrow", 50  # also a tuple!
print(tuple1)
print()

# Mapped data: dict
# dict: A dictionary is an unordered collection of data containing a 
# key:value pair. The key:value pairs are enclosed within curly brackets.
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
print()
