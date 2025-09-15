class Employee:
    name="Jerry" #this is a class atrribute
    language = "py"
    salary = "120000"
    
    def getinfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")
        
    @staticmethod
    def greet():
        print(" Good morning Boss")
    
jerry = Employee()
#jerry.language = "javascript" # instance attributes are more valuable than class attributes
#print(jerry.name,jerry.language,jerry.salary)
jerry.greet()
jerry.getinfo()
#Employee.getinfo(jerry)
