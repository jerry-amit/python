#Write a class Train which has methods to book a ticket, get status (number of seats)  and get fare information of train running under Indian Railways.

'''
from random import randint #instead of random.randint

class Train:
    
      def __init__(self,trainNo):
        self.trainNo = trainNo
    
    def book(self, fro,to):
        print(f"Ticket is booked in train no:{self.trainNo} from{fro} to {to} ")
    
        
        
    def getStatus(self):
         print(f" train no:{self.trainNo} is running succesfully on time ")#from{fro} to {to} ")
    
    
    def getFare(self, fro, to):
         print(f"Ticket fare in train no:{self.trainNo} from{fro} to {to} is {randint(222,555)} ")
         
         
t = Train(12234)
t.book("Rampur","Delhi")
t.getStatus()
t.getFare("Rampur","Delhi")
    
    
    '''
    
from random import randint

class Train:
    
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running successfully and is on time.")

    def getFare(self, fro, to):
        fare = randint(222, 555)
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is ₹{fare}")


# Example usage:
t = Train(12234)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")
