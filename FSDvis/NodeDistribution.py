
from traversalDistance.Graph import Graph
from Curve import Curve

def graph_node_distribution(graph, n_distributions):
    sigma_graph = Graph()
    node_id_gen = lambda i, n0id, n1id: int(f"{i+1}000{n0id}000{n1id}")
    edge_id_gen = lambda i, eid: int(f"{i}000{eid}")

    for edge_id, edge in graph.edges.items():

        # declaring edge informaion
        node_id_0, node_id_1 = edge[0], edge[1]
        node_0, node_1 = graph.nodes[node_id_0], graph.nodes[node_id_1]

        # adding node 1 to new graph
        node_id_init = node_id_gen(0, node_id_0, node_id_1)
        sigma_graph.addNode(node_id_init, node_0[0], node_0[1])

        # functions for new nodes across edge
        domain = node_1[0] - node_0[0]
        if domain == 0.0: domain = 1
        slope = (node_1[1] - node_0[1]) / domain
        delta = domain / (n_distributions - 1)
        x = lambda i: delta * i + node_0[0]
        y = lambda i: slope * delta * i + node_0[1]

        # adding nodes across old edge for n_distributions:
        for i in range(1, n_distributions):
            node_id_i = node_id_gen(i, node_id_0, node_id_1)
            node_id_im1 = node_id_gen(i-1, node_id_0, node_id_1)
            edge_id_i = edge_id_gen(i, edge_id)

            sigma_graph.addNode(node_id_i, x(i), y(i))
            sigma_graph.connectTwoNodes(edge_id_i, node_id_im1, node_id_i)

    return sigma_graph

def curve_node_distribution(curve, n_distributions):
    sigma_curve = Curve()
    node_id_idx = 0
    edge_id_idx = 0

    # adding init node to new graph
    sigma_curve.addNode(node_id_idx, curve.nodes[0][0], curve.nodes[0][1])
    node_id_idx += 1;

    for edge_id, edge in curve.edges.items():

        # declaring edge informaion
        node_id_0, node_id_1 = edge[0], edge[1]
        node_0, node_1 = curve.nodes[node_id_0], curve.nodes[node_id_1]

        # functions for new nodes across edge
        domain = node_1[0] - node_0[0]
        if domain == 0.0: domain = 1
        slope = (node_1[1] - node_0[1]) / domain
        delta = domain / (n_distributions - 1)
        x = lambda i: delta * i + node_0[0]
        y = lambda i: slope * delta * i + node_0[1]

        # adding nodes across old edge for n_distributions:
        for i in range(1, n_distributions):
            #if edge_id == 0 and i == 0: continue
            sigma_curve.addNode(node_id_idx, x(i), y(i))
            sigma_curve.connectTwoNodes(edge_id_idx, node_id_idx-1, node_id_idx)
            node_id_idx += 1;
            edge_id_idx += 1;

    # adding last edge and node to new graph
    #sigma_curve.addNode(node_id_idx, curve.nodes[node_id_idx][0], curve.nodes[node_id_idx][1])
    #sigma_curve.connectTwoNodes(edge_id_idx, node_id_idx-1, node_id_idx)

    sigma_curve.compute_vertex_dists()

    return sigma_curve
