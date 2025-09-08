#Write a Program to Find whether a given number is prime or not.

n=int(input("Enter a Number to check :"))

for i in range (2, n):
    if(n%i) == 0:
        print("number is not a prime")
        break
        
else:
    print("number is prime",n)
