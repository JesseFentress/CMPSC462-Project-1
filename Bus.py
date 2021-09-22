from Stack import Stack
from Student import Student


# Class that uses a stack  to simulate a bus

class Bus:

    def __init__(self):
        self.seats = Stack()

    # Encapsulates the stack push() function to put students on the bus
    def getOnBus(self, student):
        self.seats.push(student)
        print(student.getName() + " has boarded the bus.")

    # Encapsulates the stack pop() function to take students off of the bus
    def getOffBus(self):
        print(self.seats.pop().getName() + " has gotten off of the bus.")

    # Encapsulates the stack size() function
    def size(self):
        return self.seats.size()
