class Queue:

    def __init__(self):
        self.list = []

    def is_Empty(self):
        return self.list == []

    def size(self):
        return len(self.list)

    def enqueue(self, item):
        self.list.append(item)

    def dequeue(self):
        if self.is_Empty():
            print("Cannot dequeue an empty queue.")
        else:
            return self.list.pop(0)
