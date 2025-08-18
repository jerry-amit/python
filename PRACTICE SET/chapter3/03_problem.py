# Write a program to detect double space in a string
name = "jerry   is   a   good   boy"

print(name.find("   ")) # double space detector if(-1) it means not found
print(name.find("goo"))# we can find index number by this


name = "jerry   is   a   good   boy"

print(name.find("    "))