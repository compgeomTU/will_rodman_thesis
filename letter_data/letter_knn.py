# python3 letter_knn.py 
### PARAMS
N_SAMPLE = 20
IS_SAMPLE = True
K_FOLD = 5
K_NEIGHBORS = 7
LOG_DATE = '04_24'

# standard library
import sys, json
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# 3rd party library
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.metrics import precision_score, recall_score

# local classes
sys.path.append('../')
from TraversalDistance.Graph import Graph
from TraversalDistance.FreeSpaceGraph import FreeSpaceGraph
from TraversalDistance.KNeighborsClassifier import KNeighborsClassifier
sys.path.append('../')

def json_to_graph(json_data):    
    graph = Graph()
    graph.name = json_data['gxl']['graph'][0]['$']['id'][0]
    
    for node_data in json_data['gxl']['graph'][0]['node']:
        node_id = int(node_data['$']['id'][1:])
        x_coord = float(node_data['attr'][0]['float'][0])
        y_coord = float(node_data['attr'][1]['float'][0])
        graph.addNode(node_id, x_coord, y_coord)

    for i, edge_data in enumerate(json_data['gxl']['graph'][0]['edge'], 1):
        from_node = int(edge_data['$']['from'][1:])
        to_node = int(edge_data['$']['to'][1:])
        graph.connectTwoNodes(i, from_node, to_node)
        
    return graph, graph.name

def graph_data():
    file_names = os.listdir("LOW")
    X, y = [], []

    for index, file_name in enumerate(file_names):
        if file_name.endswith('.json'):
            try:         
                json_graph = json.load(open(f"LOW/{file_name}"))
                graph, name = json_to_graph(json_graph)      
                graph.id = index         
                X.append(graph)
                y.append(name)
                                        
            except Exception as error: 
                print(f"AssertionError {error}: Fail to parse {file_name}.")
                
    return X, y

def k_fold_test(X_train, X_test, y_train, y_test, fold):
    print(" \n *** Stating Fold Test #:", fold, "Train len:", len(y_train), "Test len:", len(y_test), "***")

    model = KNeighborsClassifier(n_neighbors=K_NEIGHBORS, mean='max', left=0, right=3, precision=0.001)  

    model.fit(X_train, y_train)
    y_pred, log = model.predict(X_test, fold=fold)
    
    filename = f'logs/knn_log_{LOG_DATE}_fold_{fold}.csv'
    with open(filename, 'w') as f:
        for i, (y_hat, n_classifications) in enumerate(log):
            row = [y_test[i], y_hat] + n_classifications
            f.write(','.join(row) + '\n')
    
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro') 
    return precision, recall

def process_fold(X, y, train_index, test_index, fold_number):
    X_train, X_test = [X[i] for i in train_index], [X[i] for i in test_index]
    y_train, y_test = [y[i] for i in train_index], [y[i] for i in test_index]

    precision, recall = k_fold_test(X_train, X_test, y_train, y_test, fold_number)
    return (precision, recall)

def main():
    X, y = graph_data()
    
    if IS_SAMPLE: 
        X, y = X[:N_SAMPLE], y[:N_SAMPLE]
        
    kf = KFold(n_splits=K_FOLD, shuffle=True, random_state=42)

    scores = []

    with ProcessPoolExecutor() as executor:

        for fold, (train_index, test_index) in enumerate(kf.split(X)):
            future = executor.submit(process_fold, X, y, train_index, test_index, fold+1)
            scores.append(future.result())

    df = pd.DataFrame(scores, columns=["precision", "recall"])
    df.to_csv('logs/knn_log_{LOG_DATE}.csv', index=False)
    
if __name__ == '__main__':
    main()