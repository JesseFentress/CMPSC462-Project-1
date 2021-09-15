from Stack import Stack
from Queue import Queue
from Deque import Deque
from StackTower import StackTower

###################################################################
# Part-1: Stack, Queue, and Deque class testing

# Stack class testing
s = Stack()
print(s.is_Empty())
s.push('cat')
s.push('thunder')
s.push('okay')
print(s.pop())
print(s.size())
print(s.peek())
print(s.list)

# Queue class testing
q = Queue()
q.enqueue(33)
q.enqueue(4)
q.enqueue(58)
print(q.list)
print(q.dequeue())
print(q.size())
print(q.is_Empty())
print(q.list)

# Deque class testing
d = Deque()
d.addRear(57)
d.addRear(99)
d.addFront(231)
d.addRear(12)
d.addFront(89)
print(d.removeRear())
print(d.removeFront())
print(d.list)
print(d.is_Empty())
print(d.size())

###################################################################
# Part-2: Application
# Towers of Hanoi
###################################################################

print("Towers of Hanoi")
game = StackTower(5)
game.play()
