class Deque:

    def __init__(self):
        self.list = []

    def is_Empty(self):
        return self.list == []

    def size(self):
        return len(self.list)

    def addFront(self, item):
        self.list.append(item)

    def addRear(self, item):
        self.list.insert(0, item)

    def removeFront(self):
        return self.list.pop()

    def removeRear(self):
        return self.list.pop(0)


