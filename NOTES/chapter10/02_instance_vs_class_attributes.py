class Employee:
    name="Jerry" #this is a class atrribute
    language = "py"
    salary = "120000"
    
jerry = Employee()
jerry.language = "javascript" # instance attributes are more valuable than class attributes
print(jerry.name,jerry.language,jerry.salary)
