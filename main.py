from Stack import Stack
from Queue import Queue
from Deque import Deque
from StackTower import StackTower
from BusLine import BusLine
from Student import Student
from Bus import Bus

##################################################################
# Part-1: Stack, Queue, and Deque class testing

# Stack class testing
print("##### Stack class testing ######")
s = Stack()
s.push('cat')
s.push('thunder')
s.push('okay')
print("Is the stack empty: ", end=" ")
print(s.is_Empty())
print("Popping top item: ", end=" ")
print(s.pop())
print("Current stack size: ", end=" ")
print(s.size())
print("Top item on stack: ", end=" ")
print(s.peek())
print("Current stack: ", end=" ")
print(s.list)
print()

# Queue class testing
print("##### Queue class testing ######")
q = Queue()
q.enqueue(33)
q.enqueue(4)
q.enqueue(58)
print("Current queue: ", end=" ")
print(q.list)
print("Dequeue first item: ", end=" ")
print(q.dequeue())
print("Queue size: ", end=" ")
print(q.size())
print("Is the queue empty: ", end=" ")
print(q.is_Empty())
print("Current queue: ", end=" ")
print(q.list)
print()

# Deque class testing
print("##### Deque class testing #####")
d = Deque()
d.addRear(57)
d.addRear(99)
d.addFront(231)
d.addRear(12)
d.addFront(89)
print("Removing element at rear of deque: ", end=" ")
print(d.removeRear())
print("Removing element at front of deque: ", end=" ")
print(d.removeFront())
print("Current deque: ", end=" ")
print(d.list)
print("Is the deque empty: ", end=" ")
print(d.is_Empty())
print("Deque size: ", end=" ")
print(d.size())
print()

##################################################################
# Part-2: Application
# A: Towers of Hanoi
##################################################################

print("Towers of Hanoi")
game = StackTower(5)
game.play()

##################################################################
# B: Students lining up to get on the bus for a field trip are boarded onto the bus using a FIFO order, like queue.
#    However, when getting off of the bus they are getting off using a LIFO order, like a stack.
##################################################################

line = BusLine()
bus = Bus()
studentA = Student("John")
studentB = Student("Maria")
studentC = Student("Mark")
studentD = Student("Rich")
studentE = Student("Sara")
line.getInLine(studentA)
line.getInLine(studentB)
line.getInLine(studentC)
line.getInLine(studentD)
line.getInLine(studentE)



def boarding(line, bus):

    while line.size() > 0:
        bus.getOnBus(line.getOutOfLine())


def exitting(bus):
    while bus.size() > 0:
        bus.getOffBus()

boarding(line, bus)
exitting(bus)
