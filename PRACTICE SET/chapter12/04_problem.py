''' Write a program to display a/b where A and B are integers. if B = 0, display infinite by handling the 'zeroDivisionError'
'''

try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print(a/b)
except ZeroDivisionError as v:
    print("infinite")
    