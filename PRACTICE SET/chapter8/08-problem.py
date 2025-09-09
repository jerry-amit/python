# write a Python function to print multiplication table of given number

def multiply(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
n=int(input("ENter the number for table :"))        
multiply(n)