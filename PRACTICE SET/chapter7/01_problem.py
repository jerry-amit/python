#Write a program to print multiplication table of a given number using for

n= int(input("Enter a number :"))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")  #f is used for multiple print variables