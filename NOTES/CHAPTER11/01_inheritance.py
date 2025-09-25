class Employee:
    company = "ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")
        
# class Programmer:

#      def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")
        
 
         
class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name}and he is good{self.language}language")
         
         
a = Employee()
b = Programmer()

print(a.company,b.company)