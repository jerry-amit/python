class Employee:
    name="Jerry" #this is a class atrribute
    language = "py"
    salary = "120000"
    
    #dunder method which is automatically called
    def __init__(self,name,salary,language): # init is an dunder method in python  which starts with underscore underscore
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object ")
    
    def getinfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")
        
    @staticmethod
    def greet():
        print(" Good morning Boss")
    
#jerry = Employee()
#jerry.language = "javascript" # instance attributes are more valuable than class attributes

jerry = Employee("Jerry",132500,"Javascript")
print(jerry.name,jerry.salary,jerry.language)

rohan =  Employee("amit",132500,"Javascript")
print(rohan.name,rohan.salary,rohan.language)
#Employee.getinfo(jerry)
