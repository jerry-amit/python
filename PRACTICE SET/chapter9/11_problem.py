''' Write a Python program to rename a file to "renamed_by_Python.txt'''


with open("old.txt") as f:
    content = f.read()
    
with open("renamed_by_python.txt","w") as f:
    f.write(content)
    

