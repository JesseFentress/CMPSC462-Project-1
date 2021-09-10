from Stack import Stack
from Queue import Queue

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

