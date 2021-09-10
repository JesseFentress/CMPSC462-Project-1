class Stack:

    def __init__(self):
        self.list = []

    def is_Empty(self):
        return self.list == []

    def size(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if self.is_Empty():
            print("You cannot pop an empty stack")
        else:
            return self.list.pop()

    def peek(self):
        return self.list[-1]