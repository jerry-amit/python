''' Can you change the self- parameter inside a class to something else (say "Harry"). Try changing self to "slf" or "Harry" and see the effects.

'''

    
from random import randint

class Train:
    
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(slf, fro, to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"Train no: {slf.trainNo} is running successfully and is on time.")

    def getFare(slf, fro, to):
        fare = randint(222, 555)
        print(f"Ticket fare in train no: {slf.trainNo} from {fro} to {to} is ₹{fare}")


# Example usage:
t = Train(12234)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")
