''' Store the multiplication tables generated in problem 3 in afilenamedtables.Txt'''

n = int(input("Enter your Number:"))

table = [n*i for i in range(1,11)]
with open("tablex.txt", "a") as f:
    f.write(f" Table of {n} {str(table)}  \n")
