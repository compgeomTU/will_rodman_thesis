import math
from decimal import Decimal

from FreeSpaceGraph import FreeSpaceGraph

class BinarySearch:

    left: float
    right: float
    middle: float
    precision: float
    distance: FreeSpaceGraph

    def __init__(self, distance, left=0, right=100, precision=1):
        if isinstance(distance, FreeSpaceGraph):
            self.left = left
            self.right = right
            self.precision = precision
            self.distance = distance

            self.distance.epsilon = self.right
            self.distance.DFSTraversalDist()
        else:
            raise TypeError(distance.__class__.__name__)
        
    def search(self):
        print(f"Check if epsilon is reachable:")
        print(f"| {self.left} -- {self.middle} -- {self.right} |")

        if self.distance.check_projection():
            if self.right - self.left <= self.precision:
                return self.middle          
            else:
                self.right = self.middle
                self.distance.epsilon = self.right
                self.distance.DFSTraversalDist()
                return self.search()
        else:
            self.left = self.middle
            self.distance.epsilon = self.left
            self.distance.DFSTraversalDist()
            return self.search()