#Write a Program to print multiplication table of n using for loops in reversed order. 

n= int(input("Enter a number:"))
for i in range(1,11):
    print(f" {n} X {i}= {n*i}",end="  ")
    print(f" {n} X {11-i}= {n*(11-i)}")
    