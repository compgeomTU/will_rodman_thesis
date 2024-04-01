from .BinarySearch import BinarySearch
from collections import Counter
from multiprocessing import Pool

class KNeighborsClassifier():
    mean: object
    
    n_neighbors: int

    X: list
    y: list
    
    left: float
    right: float
    precision: float
    
    __log: list

    def __init__(self, n_neighbors, mean='arithmetic', left=0, right=1000, precision=1):
        self.n_neighbors = n_neighbors
                
        self.left = left
        self.right = right
        self.precision = precision
        
        self.__log = list()
        
        match mean:
            case 'arithmetic':
                self.mean = self.__arithmetic
            case 'harmonic':
                self.mean = self.__harmonic
            case 'max':
                self.mean = self.__max
            case _:
                raise ValueError("Invalid mean defined.")

    @staticmethod
    def __arithmetic(a, b):
        return (a + b) / 2
    
    @staticmethod
    def __harmonic(a, b):
        return (2 * a * b) / (a + b)
    
    @staticmethod
    def __max(a, b):
        return max(a, b)
    
    def __metric(self, ga, gb):
        search = BinarySearch(ga, gb, left=self.left, right=self.right, precision=self.precision)
        epsilon_a = search.search()
                    
        search = BinarySearch(gb, ga, left=self.left, right=self.right, precision=self.precision)
        epsilon_b = search.search()
            
        return self.mean(epsilon_a, epsilon_b)     
    
    def __compute(self, x_pred):
        distances = list()
                
        # Computing distances. 
        for x in self.X:
            distance = self.__metric(x_pred, x)
            distances.append(distance)
            
        # Sorting distances. 
        sorted_indices = sorted(enumerate(distances), key=lambda x: x[1])
        
        # Indices of the n smallest distances. 
        n_indices = [index for index, _ in sorted_indices[:self.n_neighbors]]

        # Create a sublist of classifications using indices.
        n_classifications = [self.y[i] for i in n_indices]
        
        # Most common classifications in list => prediction. 
        y_hat, _ = Counter(n_classifications).most_common(1)[0]
        
        self.__log.append((y_hat, n_classifications))
        
        return y_hat
    
    def fit(self, X, y):
        self.X = X
        self.y = y
       
    def bad_predict(self, X):        
        return list(map(self.__compute, X)), self.__log
    
    # does not work. 
    def multi_predict(self, X, n_processes=1):        
        k, m = divmod(len(X), n_processes)
        batches = list(X[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n_processes))

        def task(batch):
            return [self.__compute(x) for x in batch]
        
        with Pool(processes=n_processes) as pool:
            results = pool.map(task, batches)
            
        predictions = [item for sublist in results for item in sublist]
        
        return predictions, self.__log