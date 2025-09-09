# Write a python program using function to covert Celsius to Fahrenhite


def f_to_c(f):
   
#   c=5*(f-32)/9
    return 5*(f-32)/9  # or return c
    
f = int(input("Enter temprature in F :"))

c=f_to_c(f)
print(f"{ round(c,2)} °C")