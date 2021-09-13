from Stack import Stack
from Queue import Queue
from Deque import Deque

s = Stack()
print(s.is_Empty())
s.push('cat')
s.push('thunder')
s.push('okay')
print(s.pop())
print(s.size())
print(s.peek())
print(s.list)


q = Queue()
q.enqueue(33)
q.enqueue(4)
q.enqueue(58)
print(q.list)
print(q.dequeue())
print(q.size())
print(q.is_Empty())
print(q.list)

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
