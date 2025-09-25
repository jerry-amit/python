class Employee:
    company = "ITC"
    name = "default name"
    def show(self):
        print(f"the name is {self.name} and the company is {self.company}")
        
        
class coder:
    language = "python"
    def  printLanguages(self):
        print(f"Out off all the languages here is your language: {self.language}")
    
        
# class Programmer:

#      def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")
        
 
         
class Programmer(Employee, coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company}and he is good{self.language}language")
         
         
# a = Employee()
b = Programmer()

# print(a.company,b.company)
b.show()
b.showLanguage()
b.printLanguages()