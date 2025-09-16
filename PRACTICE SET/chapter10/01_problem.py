# Create a class "programmer" for storing information of programmers working at Microsoft

class Programmer:
    
    
    comapany ="Microsoft"
    def __init__(self,name,salary,pincode):
        self.name=name
        self.salary = salary
        self.pincode = pincode
        
p = Programmer("harry", 12000, 832654)
j = Programmer("jerry", 12000, 832654)


print(p.name,p.salary,p.pincode, p.comapany)
print(j.name,j.salary,j.pincode, j.comapany)
