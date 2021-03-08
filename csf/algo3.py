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
    random.shuffle(li)

    for i in li:
        for j in li:
            if i < j:
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

    # tw = 0

    # for i in range(1, n):
    #     info = G.get_edge_data(hamiltonian_cycle[i], hamiltonian_cycle[i+1])
    #     tw += info['weight']

    # # print(tw)

    # return tw, hamiltonian_cycle

if __name__ == "__main__":

    def get_length(path, points):
        """Return the length of the path.
        
        Input:  path is a list of point indices;
                points is a list of the form [n, (x_1, y_1), ..., (x_n, y_n)],
                where n is the number of points on a plane and (x_i, y_i) are their coordinates. 
        Output: The length of the input path
                assuming the coordinates specified in the input
                and the Euclidean distance between the points.
        """
        return sum(distance(points[path[i]], points[path[i+1]]) for i in range(len(path) - 1))
            

    def test(points, baseline_path, short_path):
        """Test the tsp function on points.
        
        baseline_path is the length of a simple solution.
        short_path is the length of a good solution.
        
        Your solution should run for at most 30 seconds
        and should return a path of length less than than baseline_path
        (the only exception is when baseline_path is almost equal to short_path;
        in this case, it is OK to return a path of similar length).
        The score you get depends on how short your path is. The score is the returned value of the function.
        
        """
        print("Baseline path: ", baseline_path)
        print("Short path: ", short_path)
        n = points[0]

        path = tsp(points)
        
        assert len(path) == n + 1, "The route must contain n + 1 points."
        assert path[0] == 1 == path[-1], "The route should start and end at point 1."
        assert set(path) == set(range(1, n + 1)), "The route must contain all n points."

        length = get_length(path, points)
        print("Your path: ", length)
        if length <= short_path + 0.00001: # If your path is just slightly longer than short_path or shorter, you get 10. 
            return 10.0    
        if length >= baseline_path: # If it is the same as the baseline or longer, you get 1.
            return 1
        # Otherwise, the number of points you get depends on how close your path is to short_path.
        return math.ceil((baseline_path-length) / (baseline_path-short_path) * 10)

        # Square 1 x 1. Your algorithm is expected to find a shortest tour, e.g., [1, 3, 2, 4, 1].
        points = [4, (0, 0), (1, 1), (0, 1), (1, 0)]
        length = get_length([1, 3, 2, 4, 1], points)
        assert test(points, length, length) == 10


        # Line y = x + 1. Your algorithm is expected to find a shortest tour, e.g., [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1].
        points = [10, (1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20)]
        length = get_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1], points)
        assert test(points, length, length) == 10

    points = [25,
            (6139, -9327),
            (7524, 9018),
            (-8201, -4582),
            (5277, -13042),
            (2541, 156),
            (-6748, 14001),
            (12371, 6187),
            (-3191, 3754),
            (-14173, 11185),
            (1725, 14670),
            (-14467, 12589),
            (-703, -13791),
            (6151, -7013),
            (1367, 14568),
            (-13867, 14509),
            (405, -6256),
            (6185, -13240),
            (7325, 5230),
            (845, 339),
            (7181, -2898),
            (-2921, -4544),
            (10395, 808),
            (11313, 2696),
            (-5320, 11409),
            (3790, 10442)
            ]

    baseline = get_length(
        [1, 13, 20, 22, 23, 7, 18, 2, 25, 10, 14, 24, 6, 15, 11, 9, 8, 19, 5, 16, 21, 3, 12, 4, 17, 1],
        points)
    short = get_length(
        [1, 17, 4, 12, 3, 21, 16, 5, 19, 8, 9, 11, 15, 6, 24, 14, 10, 25, 2, 18, 7, 23, 22, 20, 13, 1],
        points)

    test(points, baseline, short)

    points = [45,
            (175, 17),
            (134, 299),
            (244, 76),
            (17, 61),
            (111, 273),
            (195, 170),
            (155, 209),
            (57, 251),
            (57, 47),
            (100, 176),
            (182, 251),
            (272, 126),
            (213, 232),
            (131, 52),
            (174, 201),
            (239, 281),
            (8, 40),
            (142, 14),
            (298, 244),
            (28, 121),
            (151, 101),
            (40, 203),
            (70, 105),
            (290, 99),
            (294, 27),
            (221, 153),
            (182, 78),
            (186, 60),
            (70, 52),
            (151, 70),
            (218, 122),
            (58, 8),
            (240, 134),
            (178, 40),
            (71, 20),
            (153, 299),
            (25, 125),
            (6, 148),
            (245, 14),
            (177, 41),
            (237, 116),
            (94, 16),
            (158, 107),
            (3, 21),
            (194, 47)
            ]

    baseline = get_length(
        [1, 34, 40, 45, 28, 27, 30, 14, 18, 42, 35, 32, 9, 29, 23,
        20, 37, 38, 22, 8, 5, 2, 36, 11, 13, 15, 7, 6, 26, 33, 41,
        31, 3, 24, 12, 25, 39, 43, 21, 10, 4, 17, 44, 16, 19, 1],
        points)
    short = get_length(
        [1, 39, 25, 3, 24, 12, 33, 41, 31, 26, 6, 15, 7, 11, 13,
        19, 16, 36, 2, 5, 8, 22, 10, 38, 37, 20, 23, 29, 9, 4, 17,
        44, 32, 35, 42, 18, 14, 30, 21, 43, 27, 28, 45, 40, 34, 1],
        points)

    test(points, baseline, short)