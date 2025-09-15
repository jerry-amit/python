'''Write a program to find out the line number where python is present from ques 6.'''

 
#  #1st way
# line = 1
# with open("log.txt") as f:
#     line = f.readline()
    
    
#     if("python" in line):
#         print(f"yes python is present.Line no:{line}")
        
#     else:
#         print("No python is not present")


# 2nd way

with open("log.txt") as f:
    lines = f.readlines()
    
lineno = 1
for line in lines:
    if("python" in line):
        print(f"yes python is present.Line no:{lineno}")
        break
    
    lineno += 1

else:
    print("No python is not present")