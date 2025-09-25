class Employee:
     a=1 
     @classmethod
     def show(cls):
         print(f"THE  class  value of a ia {cls.a}")
         
e = Employee()
e.a = 45

e.show()
         