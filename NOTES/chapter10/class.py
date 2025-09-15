class Employee:
    name="Jerry" #this is a class atrribute
    language = "py"
    salary = "120000"
    
jerry = Employee()
print(jerry.name,jerry.language,jerry.salary)

rohan = Employee()
rohan.name = "rohan"# this is a object/ instance attribute
print(rohan.name,rohan.salary,rohan.language)