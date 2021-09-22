# I used the same Deque() example that was given in the book, and kept the front/back the same; however, it would
# personally make more sense for me to have the rear be the right side of the deque and the front be the left side
# of the deque.

class Deque:

    def __init__(self):
        self.list = []

    def is_Empty(self):
        return self.list == []

    def size(self):
        return len(self.list)

    # Adds elements to the right end, or the front, of the deque using built in append() funciton
    def addFront(self, item):
        self.list.append(item)

    # Adds elements to the left end, or the rear, of the deque using built in insert() function with the first index
    # as an argument
    def addRear(self, item):
        self.list.insert(0, item)

    # Removes elements from the right end, or the front, of the deque using pop()
    def removeFront(self):
        return self.list.pop()

    # Removes elements from the left end, or the rear, of the deque using pop() with the first index as an argument
    def removeRear(self):
        return self.list.pop(0)

    def p(self):
        return self.list


