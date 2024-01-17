from .BinarySearch import BinarySearch
from .Graph import Graph
from itertools import chain

import matplotlib.pyplot as plt

class DistanceMatrix(BinarySearch):
    matrix: list
    m: list
    n: list
    left_global: float
    right_global: float
    precision_global: float

    def __init__(self, m, n, left=0, right=1000, precision=1):
        self.m = m
        self.n = n
        self.matrix = list()
        self.left_global = left
        self.right_global = right
        self.precision_global = precision
        super().__init__(Graph(), Graph(), left=left, right=right, precision=precision)
        
    def __flush(self):
        self.left=self.left_global
        self.right=self.right_global
        self.precision=self.precision_global
        
    def to_list(self):
        return list(chain.from_iterable(self.matrix))

    def compute(self):
        for mi in self.m:
            self.matrix.append(list())    
            for ni in self.n:     
                self.__flush()
                self.g1, self.g2 = mi, ni
                epsilon_x = self.search()
                    
                self.__flush()
                self.g1, self.g2 = ni, mi
                epsilon_y = self.search()
                self.matrix[-1].append((epsilon_x, epsilon_y))
                                