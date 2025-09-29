''' Write a list comprehension to print a list which contains the multiplication table of a user inter number.'''

n = int(input("Enter your Number:"))

table = [n*i for i in range(1,11)]
print(table)
