from Deque import Deque

# Class simulates very basic chess where you are allowed to make moves and undo moves


class Chess:

    def __init__(self):
        self.history = Deque()

    # Moves are passed as tuples and pushed on the front of the deque
    def move(self, tup):
        self.history.addFront(tup)
        print("Move " + tup[0] + " to " + tup[1])

    # Undone moves are removed from the front of the deque and added to the rear
    def undo(self):
        self.history.addRear(self.history.removeFront())
        print("Move was undone.")

    # Redo moves are moves that were previously undone, redoing a move removes it from the rear of deque and adds
    # the move back to the front of the deque
    def redo(self):
        self.history.addFront((self.history.removeRear()))
        print("The move was redone.")
