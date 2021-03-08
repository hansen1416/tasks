import math
import random
import networkx as nx

def distance(p, q):
    """Return the Euclidean distance between points p = (a, b) and q = (c, d)."""
    return ((p[0]-q[0])**2 + (p[1]-q[1])**2) ** 0.5

# def hierholzer(unvisited_edges, existed_cycle=[]):
#     # this statement shall never be true
#     if len(unvisited_edges) == 0:
#         return existed_cycle
#     # if we found a cycle before, try find another edge that connected to this edge
#     if len(existed_cycle):
#         for edge in unvisited_edges:
#             if edge[0] in existed_cycle:
#                 start_edge = [edge[0], edge[1]]
#                 break
#             elif edge[1] in existed_cycle:
#                 start_edge = [edge[1], edge[0]]
#                 break

#         unvisited_edges.remove(edge)
#         # use the endpoint of the unvisited edge that connected to the existing cycle,
#         # as the new start point of the cycle
#         start_ind = existed_cycle.index(start_edge[0])
#         existed_cycle = existed_cycle[start_ind:] + existed_cycle[:start_ind]
#     else:
#         # when we start, just pick a random node
#         start_edge = unvisited_edges.pop()
#     # find a cycle in the graph, there must be one, since all nodes has even degree
#     cycle = find_cycle([start_edge[0], start_edge[1]], unvisited_edges)
#     # concatenate the newly found cycle with old cycle
#     if len(existed_cycle):
#         cycle = existed_cycle + cycle
#     # when unvisited edge exists, continue
#     if len(unvisited_edges):
#         return hierholzer(unvisited_edges, cycle)

#     return cycle


# def find_cycle(cycle_path, edge_list):
#     # if end node is start node, we have a cycle
#     # there should always a cycle, since all nodes have even degree
#     if cycle_path[0] == cycle_path[-1]:
#         return cycle_path

#     i = 0
#     #
#     while i < len(edge_list):
#         # if we found a edge connect the last node in the unfinished cycle path, we take it
#         if edge_list[i][0] == cycle_path[-1]:
#             cycle_path.append(edge_list[i][1])
#             # remove the edge took
#             del edge_list[i]
#             # if there are unvisited nodes, continue
#             if len(edge_list):
#                 return find_cycle(cycle_path, edge_list)
#             else:
#                 return cycle_path

#             break
#         # if we found a edge connect the last node in the unfinished cycle path, we take it
#         if edge_list[i][1] == cycle_path[-1]:
#             cycle_path.append(edge_list[i][0])
#             # remove the edge took
#             del edge_list[i]
#             # if there are unvisited nodes, continue
#             if len(edge_list):
#                 return find_cycle(cycle_path, edge_list)
#             else:
#                 return cycle_path

#             break

#         i += 1

def find_eulerian_tour(MatchedMSTree):
    # print('MatchedMSTree', MatchedMSTree)
    # find neigbours
    neighbours = {}
    for edge in MatchedMSTree:
        if edge[0] not in neighbours:
            neighbours[edge[0]] = []

        if edge[1] not in neighbours:
            neighbours[edge[1]] = []

        neighbours[edge[0]].append(edge[1])
        neighbours[edge[1]].append(edge[0])

    # print("Neighbours: ", neighbours)

    # finds the hamiltonian circuit
    start_vertex = MatchedMSTree[0][0]
    EP = [neighbours[start_vertex][0]]

    while len(MatchedMSTree) > 0:
        for i, v in enumerate(EP):
            if len(neighbours[v]) > 0:
                break

        while len(neighbours[v]) > 0:
            w = neighbours[v][0]

            remove_edge_from_matchedMST(MatchedMSTree, v, w)

            del neighbours[v][(neighbours[v].index(w))]
            del neighbours[w][(neighbours[w].index(v))]

            i += 1
            EP.insert(i, w)

            v = w
    # print('EP', EP)
    return EP

def remove_edge_from_matchedMST(MatchedMST, v1, v2):

    for i, item in enumerate(MatchedMST):
        if (item[0] == v2 and item[1] == v1) or (item[0] == v1 and item[1] == v2):
            del MatchedMST[i]

    return MatchedMST

def cost_change(G, n1, n2, n3, n4):
    return G.get_edge_data(n1, n3)['weight'] + G.get_edge_data(n2, n4)['weight'] - \
        G.get_edge_data(n1, n2)['weight'] - G.get_edge_data(n3, n4)['weight']


def two_opt(route, G):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):

                # if j-i == 1: continue # changes nothing, skip then
                # new_route = route[:]
                # new_route[i:j] = route[j-1:i-1:-1] # this is the 2woptSwap
                # if get_length(new_route, points) < get_length(best, points):  # what should cost be?
                #         best = new_route
                #         improved = True

                if j - i == 1: continue
                if cost_change(G, best[i - 1], best[i], best[j - 1], best[j]) < -1:
                    best[i:j] = best[j - 1:i - 1:-1]
                    improved = True

        route = best
    return best

def tsp(points):
    G = nx.Graph()

    n = points[0]

    li = list(range(1, n+1))
    # random.shuffle(li)

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # if i < j:
            G.add_edge(i, j, weight=distance(points[i], points[j]))
                # print(i, j, distance(points[i], points[j]))

    del li

    mst = nx.minimum_spanning_tree(G)
    sub_nodes = []

    for d in mst.degree:
        if d[1] % 2 == 1:
            sub_nodes.append(d[0])
        # print(d[0], d[1])

    # random.shuffle(sub_nodes)

    odd_node_sub = G.subgraph(sub_nodes)

    del sub_nodes
    # print(odd_node_sub.edges(data=True))
    # print("=======")

    odd_node_sub_rev = nx.Graph()
    max_w = 9999999999

    for edge in list(odd_node_sub.edges(data=True)):
        # G.add_edge(i, j, weight=distance(points[i], points[j]))
        odd_node_sub_rev.add_edge(edge[0], edge[1], weight=(max_w - edge[2]['weight']))

    # print(odd_node_sub_rev.edges(data=True))

    mpm = nx.algorithms.matching.max_weight_matching(odd_node_sub_rev, maxcardinality=False)

    union = list(mst.edges()) + list(mpm)

    del mst, odd_node_sub, odd_node_sub_rev

    # print(union)

    # eulerian_cycle = hierholzer(union[:])

    eulerian_cycle = find_eulerian_tour(union)

    # print(eulerian_cycle)

    start_index = eulerian_cycle.index(1)

    hamiltonian_cycle = []
    # remove repeated nodes, we start from node 1
    for node in eulerian_cycle[start_index:] + eulerian_cycle[:start_index]:
        if node not in hamiltonian_cycle:
            hamiltonian_cycle.append(node)

    # make it a cycle
    hamiltonian_cycle.append(hamiltonian_cycle[0])
    # print('hamiltonian_cycle', hamiltonian_cycle)

    result = two_opt(hamiltonian_cycle, G)

    return result

#     tw = 0

#     for i in range(0, n):
#         tw += G.get_edge_data(result[i], result[i+1])['weight']
#         # print(result[i], result[i+1], G.get_edge_data(result[i], result[i+1])['weight'])

#     # print(result)

#     return tw, result

# def tsp(points):

#     min_tw = float('inf')
#     min_path = []

#     it = 3
#     if points[0] >= 400:
#         it = 2
#     if points[0] >= 800:
#         it = 1
    
#     for i in range(it):
#         tw, path = csf(points)

#         if tw < min_tw:
#             min_tw = tw
#             min_path = path

#     return min_path