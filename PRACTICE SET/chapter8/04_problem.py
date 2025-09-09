# Write a recursive function to calculate the sum of first N natural numbers.
'''

'''

def sum(n):
    if(n==1):#base condition
        return 1
    
    return sum(n-1) + n
print(sum(4))    