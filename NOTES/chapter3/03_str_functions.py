name="jerry"

print(len(name))
print(name.endswith("rry"))

print(name.startswith("Je"))

print(name.capitalize())



print(name.lower())# "hello"
print(name.upper()) # "HELLO"


#Removes whitespace (or specified characters) from both ends / left / right.
name1="  hello"   # "hello"
name2="  hello"   # "hello"
name3="hello  "   # "hello"

print(name1.strip())
print(name2.strip())
print(name3.strip())

#Replaces all occurrences of a substring.
a="hello world"
print(a.replace("world", "Python"))  # "hello Python"


# Finds the first occurrence of a substring. find() returns -1 if not found; index() raises an error.

b="hello"
print(b.find("e"))   # 1)
b="hello"
print(b.index("e"))  # 1


#Splits the string into a list by a delimiter.
a="a,b,c"
print(a.split(","))      # ['a', 'b', 'c']
print(a.rsplit(",", 1))  # ['a,b', 'c']



#Joins elements of an iterable into a string, using the string as a separator.
a=","
print(a.join(["a", "b", "c"]))  # "a,b,c"

