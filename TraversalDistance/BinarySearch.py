from .FreeSpaceGraph import FreeSpaceGraph
from .Graph import Graph
class BinarySearch(FreeSpaceGraph):

    left: float
    right: float
    middle: float
    precision: float

    def __init__(self, g1=Graph(), g2=Graph(), log=False, left=0, right=100, precision=1):
        self.left = left
        self.right = right
        self.precision = precision
        super().__init__(g1, g2, epsilon=float(), log=log)

    def search(self):    
        # check if graphs are equal
        if self.g1 == self.g2:
            return 0.0
            
        # check if precision threshold is met
        if self.right - self.left <= self.precision:
            return self.right 
        
        self.epsilon = (self.left + self.right) / 2

        # trying to compute traversal distance, if fails, return non-distance value        
        try:
            projection_check = self.DFSTraversalDist()
        except Exception as error:
            print(f"Exception: {error}.")
            return -1.0
        
        if projection_check:
            self.right = self.epsilon
            return self.search()
        else:
            self.left = self.epsilon
            return self.search()
