#Write a Program Using Functions to FInd Greater of Three numbers.


def greatest(a, b, c):
    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b
    #else:
    elif(c>b or c>a):
        return c
a =int(input("Enter the number")) 
b =int(input("Enter the number")) 
c =int(input("Enter the number")) 

# a=1
# b=2
# c=3
print(greatest(a,b,c))
