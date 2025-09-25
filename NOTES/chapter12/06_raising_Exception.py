a = int(input("Enter  a number" ))
b = int(input("Enter  Second  number" ))

if(b==0):
    raise ZeroDivisionError("HEy our Program is not meant to divide Numbers by zero")

else:
    print(f" The divison a/b is {a/b}")
