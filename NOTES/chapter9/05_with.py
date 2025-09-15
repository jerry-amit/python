# f = open("file.txt")
# data= f.read()
# print(data)
# f.close()


# The sam can be written using with statement  like this:

with open("file.txt","r") as f:
     text=f.read()

print(f.read())
# print(text)

# you dont have to explicitly close the file
    