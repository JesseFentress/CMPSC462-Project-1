import itertools

from Stack import Stack


class StackTower:

    def __init__(self, size):
        self.start = Stack()
        self.end = Stack()
        self.aux = Stack()
        self.size = size
        self.fill(size)

    def fill(self, size):

        # Iterates for a the given size starting with the larger values of i, i represents the size of the disks, so
        # iterating backwards preserves the "disk cannot be placed over a smaller disk" rule
        for i in reversed(range(1, size + 1)):
            self.start.push(i)  # Pushes the values onto the stack

    def legal_move(self, s1, s2):

        # Disks can only be moved if a destination stack is empty or the destination stack has a smaller disk on top
        # Stacks must be checked for being empty first or there will be an error thrown by the peek() function
        if s2.is_Empty():  # s2 is the destination stack if empty
            s2.push(s1.pop())
        elif s1.is_Empty():  # s1 is the destination stack if empty
            s1.push(s2.pop())
        elif s1.peek() < s2.peek():  # s2 is the destination stack if its top value is less than the top value of s1
            s2.push(s1.pop())
        elif s2.peek() < s1.peek():  # s1 is the destination stack if its top value is less than the top value of s2
            s1.push(s2.pop())

    def simulation(self):

        print("#####################################################")

        # I found this method for iterating through multiple lists on geeksforgeeks, itertools.zip_longest takes
        # all the lists as arguments and will iterate through them all until they are all exhausted, the final
        # argument fillvalue will replace any empty indices for an exhausted list, this is purely for printing purposes
        for (s, a, e) in itertools.zip_longest(reversed(self.start.list), reversed(self.aux.list), reversed(self.end.list), fillvalue="|"):
            print(s, a, e)

    def play(self):

        self.simulation()  # Print the starting stacks

        # ToH requires (2^n) - 1 steps to be solved (O(2^n) complexity with iteration), where n is the number of disks
        # the size variable made with the constructor is used to hold the number of disks for this calculation
        # ToH also has a specific disk movement pattern that is followed when being solved so we can use this number
        # to know what move we are on
        total_moves = (2 ** self.size) - 1

        # ToH with an even number of disks requires different disk movement pattern than an odd number of disks
        if self.size % 2 == 0:  # Even number of disk movement algo

            # Movement patterns have 3 steps (1, 2, 3) so iterating through the number of total moves will reveal which
            # step needs to be done to keep solving, starting with moving a disk from start stack to aux stack
            for move in range(1, total_moves + 1):
                if move % 3 == 1:  # If the move number % 1 == 1 then we are on step 1
                    self.legal_move(self.start, self.aux)  # Step 1 requires a disk to be moved between start/aux stack
                    self.simulation()
                elif move % 3 == 2:  # If the move number % 3 == 2 then we are on step 2
                    self.legal_move(self.start, self.end)  # Step 2 requires a disk to be moved between start/end stack
                    self.simulation()
                elif move % 3 == 0:  # If the move number % 3 == 0 then we are on step 3
                    self.legal_move(self.aux, self.end)  # Step 3 requires a disk to be moved between aux/end stack
                    self.simulation()
        else:  # Odd number of disk movement algo

            # Movement pattern once again has 3 steps (1, 2, 3) so a similar solution can be used, but this time since
            # the number of disks are odd the disks move in a different order
            for move in range(1, total_moves + 1):
                if move % 3 == 1:  # If the move number % 1 == 1 then we are on step 1
                    self.legal_move(self.start, self.end)  # Step 1 requires a disk to be moved between start/end stack
                    self.simulation()
                elif move % 3 == 2:  # If the move number % 3 == 2 then we are on step 2
                    self.legal_move(self.start, self.aux)  # Step 2 requires a disk to be moved between start/aux stack
                    self.simulation()
                elif move % 3 == 0:  # If the move number % 3 == 0 then we are on step 3
                    self.legal_move(self.end, self.aux)  # Step 3 requires a disk to be moved between end/aux stack
                    self.simulation()
