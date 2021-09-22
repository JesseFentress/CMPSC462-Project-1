from Queue import Queue

# Class that uses queue to simulate a bus line, first students in the line should be the first out


class BusLine:

    def __init__(self):
        self.line = Queue()

    # Encapsultes the queue enqueue() function to put students in line
    def getInLine(self, student):
        self.line.enqueue(student)
        print(student.getName() + " has gotten in line for the bus.")

    # Encapsulates the queue dequeue() function to take students out of line
    def getOutOfLine(self):
        s = self.line.dequeue()
        print(s.getName() + " has gotten out of line.")
        return s

    # Encapsulates the queue size() function
    def size(self):
        return self.line.size()
