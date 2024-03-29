from .FreeSpaceGraph import FreeSpaceGraph
from .Graph import Graph
class BinarySearch(FreeSpaceGraph):

    left: float
    right: float
    middle: float
    precision: float

    def __init__(self, g1=Graph(), g2=Graph(), left=0, right=1000, precision=1, log=False):
        self.left = left
        self.right = right
        self.precision = precision
        super().__init__(g1, g2, epsilon=float(), log=log)

    def search(self):    
 
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
