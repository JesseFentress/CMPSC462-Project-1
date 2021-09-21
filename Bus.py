from Stack import Stack
from Student import Student

class Bus:

    def __init__(self):
        self.seats = Stack()

    def getOnBus(self, student):
        self.seats.push(student)
        print(student.getName() + " has boarded the bus.")

    def getOffBus(self):
        print(self.seats.pop().getName() + " has gotten off of the bus.")

    def size(self):
        return self.seats.size()

