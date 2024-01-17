from .BinarySearch import BinarySearch
from .Graph import Graph
from itertools import chain

import matplotlib.pyplot as plt

class DistanceMatrix():
    mean: object
    
    matrix: list
    graphs: list
    
    left: float
    right: float
    precision: float

    def __init__(self, graphs, mean, left=0, right=1000, precision=1):
        self.graphs = graphs
        self.matrix = list()
        self.mean = mean
        
        self.left = left
        self.right = right
        self.precision = precision

    def to_list(self):
        return list(chain.from_iterable(self.matrix))

    def compute(self):
        for i in range(len(self.graphs)): 
            self.matrix.append(list())  
            
            for j in range(len(self.graphs)):
                
                # Check if iteration inside distance matrix. 
                if j <= i:    
                    g1, g2 = self.graphs[i], self.graphs[j]
                    
                    search = BinarySearch(g1, g2, left=self.left, right=self.right, precision=self.precision)
                    epsilon_a = search.search()
                    
                    search = BinarySearch(g2, g1, left=self.left, right=self.right, precision=self.precision)
                    epsilon_b = search.search()
                    
                    epsilon = self.mean(epsilon_a, epsilon_b)
                    self.matrix[i].append(epsilon)
                    
    def __str__(self):
        str_ = str()
        for i in self.matrix:
            str_ += str(i) + '\n'
        return str_