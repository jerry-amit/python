#Write a program to calculate the Factorial of a given number using for loop
n= int(input("ENter the number: "))

product=1

for i in range(1,n+1):
    product = product*i
    
print(f"the factorial of {n} is {product}")