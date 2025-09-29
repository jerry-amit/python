''' Write a program to find the maximum of the numbers in a list using the reduce function'''

from functools import reduce

l = [1,2,325,54,5587875,8,8,888,477,454]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))