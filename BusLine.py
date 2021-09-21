from Queue import Queue
from Student import Student


class BusLine():

    def __init__(self):
        self.line = Queue()

    def getInLine(self, student):
        self.line.enqueue(student)
        print(student.getName() + " has gotten in line for the bus.")

    def getOutOfLine(self):
        s = self.line.dequeue()
        print(s.getName() + " has gotten out of line.")
        return s

    def size(self):
        return self.line.size()