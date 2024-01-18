from .BinarySearch import BinarySearch

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
        
    def compute(self):
        for i in range(len(self.graphs)): 
            self.matrix.append(list())  
            
            for j in range(len(self.graphs)):
                
                # Check if iteration inside distance matrix. 
                if j <= i:    
                    ga, gb = self.graphs[i], self.graphs[j]
                    
                    search = BinarySearch(ga, gb, left=self.left, right=self.right, precision=self.precision)
                    epsilon_a = search.search()
                    
                    search = BinarySearch(ga, gb, left=self.left, right=self.right, precision=self.precision)
                    epsilon_b = search.search()
                    
                    epsilon = self.mean(epsilon_a, epsilon_b)
                    self.matrix[i].append(epsilon)
                    
    def __str__(self):
        str_ = str()
        for row in self.matrix:
            row = [f"{element:.2f}" for element in row]
            str_ += str(row) + '\n'
        return str_