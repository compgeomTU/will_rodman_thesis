"""
    Author: 
        Will Rodman 
        wrodman@tulane.edu
"""

import sys
from Graph import Graph
from FreeSpaceGraph import FreeSpaceGraph
from visualize import Visualize
from binarysearch import BinarySearch

if __name__ == "__main__":

    # argument parse 
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    
    # class declaration 
    g1 = Graph(filename1)
    g2 = Graph(filename2)

    if '-l' in sys.argv:
        log = True
    else:
        log = False

    if '-b' in sys.argv:
        distance = BinarySearch(g1, g2, log=log)
        epsilon = distance.search()

    if '-g1_ids' in sys.argv and '-g2_ids' in sys.argv:
        arg1 = sys.argv[sys.argv.index('-g1_ids')+1]
        arg2 = sys.argv[sys.argv.index('-g2_ids')+1]
        g1_ids = [eval(i) for i in arg1.split(',')]
        g2_ids = [eval(i) for i in arg2.split(',')]
    else:
        g1_ids, g2_ids = None, None

    if '-p' in sys.argv:
        epsilon = int(sys.argv[sys.argv.index('-p')+1])
        distance = Visualize(g1, g2, epsilon, log=log)
        projection_check = distance.DFSTraversalDist()
        distance.plot(g1_ids=g1_ids, g2_ids=g2_ids)

    print("\n-- Epsilon --")
    print(f"     {epsilon}")

    print("\n-- Sample Graphs --")
    print(f"     No. edges in {filename1}:", g1.numberOfEdges)
    print(f"     No. vertices in {filename1}:", g1.numberOfNodes)
    print(f"     No. edges in {filename2}:", g2.numberOfEdges)
    print(f"     No. vertices in {filename2}:", g1.numberOfNodes)

    print("\n -- Running Traversal Distance --")
    print("     DFS Function Calls:", distance.DFS_calls)
    print("     DFS FS CBs computed:", len(distance.cell_boundaries))
    print("     Total Possible CBs:", distance.cb_count)
