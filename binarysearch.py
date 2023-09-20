from FreeSpaceGraph import FreeSpaceGraph

class BinarySearch(FreeSpaceGraph):

    left: float
    right: float
    middle: float
    precision: float

    def __init__(self, g1, g2, log=False, left=0, right=100, precision=1):
        self.left = left
        self.right = right
        self.precision = precision
        super().__init__(g1, g2, self.right, log)

    def search(self):

        if self.right - self.left <= self.precision:
            print(f"Epsilon checks precision: {self.right}")
            return self.right 
        
        self.epsilon = (self.left + self.right) / 2

        print(f"Check if epsilon is reachable:")
        print(f"| {self.left} -- {self.epsilon} -- {self.right} |", '\n')

        if self.DFSTraversalDist():
            self.right = self.epsilon
            return self.search()
        else:
            self.left = self.epsilon
            return self.search()
        

