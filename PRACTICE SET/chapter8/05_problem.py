## Write a Python function to print first N lines of the following pattern
'''
***
**
*  for n=3
'''


def pattern(n):
    
    if(n==0):
        return# return matlab baat khatam ab jao
    print("*" * n)
    pattern(n-1)
    
n= int(input("Enter the number :"))
pattern(n)    
