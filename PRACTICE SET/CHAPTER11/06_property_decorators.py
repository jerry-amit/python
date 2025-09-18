class Employee:
     a=1 
     @classmethod
     def show(cls):
         print(f"THE  class  value of a ia {cls.a}")
         
     @property
     def name(self):
         return f"{self.fname} {self.lname}"
     
     @name.setter
     def name (self,value):
         self.fname = value.split(" ")[0]
         self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Jerry khan"
print(e.fname, e.lname)

e.show()
         