#Write a program to print the follwing star pattern:

'''
  *
 ***
***** 
for n=3'''
n= int(input("Enter the number :"))

for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="")
    print("")

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print(" "*(2*i-1),end="")
