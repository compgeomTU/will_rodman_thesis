from .FreeSpaceGraph import FreeSpaceGraph

class BinarySearch(FreeSpaceGraph):

    left: float
    right: float
    middle: float
    precision: float

    def __init__(self, g1, g2, log=False, left=0, right=50, precision=0.5):
        self.left = left
        self.right = right
        self.precision = precision
        super().__init__(g1, g2, log=log)

    def search(self):
        if self.right - self.left <= self.precision:
            print(f"Epsilon checks precision: {self.right}")
            return self.right 
        
        self.epsilon = (self.left + self.right) / 2
        self.cell_boundaries.clear()
        projection_check = self.DFSTraversalDist()

        print(f"Projeciton check if epsilon is reachable: {projection_check}")
        print(f"| {self.left} -- {self.epsilon} -- {self.right} |", '\n')

        if projection_check:
            self.right = self.epsilon
            return self.search()
        else:
            self.left = self.epsilon
            return self.search()
        

