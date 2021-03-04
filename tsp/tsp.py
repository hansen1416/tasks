import networkx as nx

def distance(p, q):
    """Return the Euclidean distance between points p = (a, b) and q = (c, d)."""
    return ((p[0]-q[0])**2 + (p[1]-q[1])**2) ** 0.5


def kruskal(adjacency_list_sorted):
#####################################
#                                   #
#     return a list of all edges in #
#     the Minimum Spaning Tree(MST) #
#####################################

     nodes_color = {}
     color_nodes = {}
     colored_edges = []
     colors = 0

     for edge, weight in adjacency_list_sorted.items():
          # If neither of e's endpoints are colored, give them a new color. Give e the same color.
          if edge[0] not in nodes_color and edge[1] not in nodes_color:
               nodes_color[edge[0]] = colors
               nodes_color[edge[1]] = colors

               color_nodes[colors] = [edge[0], edge[1]]

               colors += 1
        # If precisely 1 endpoint is colored, give the other one and e the same color.
          elif edge[0] not in nodes_color and edge[1] in nodes_color:
               nodes_color[edge[0]] = nodes_color[edge[1]]

               color_nodes[nodes_color[edge[1]]].append(edge[0])

          elif edge[0] in nodes_color and edge[1] not in nodes_color:
               nodes_color[edge[1]] = nodes_color[edge[0]]

               color_nodes[nodes_color[edge[0]]].append(edge[1])

          # If both endpoints are colored
          elif edge[0] in nodes_color and edge[1] in nodes_color:
               # both endpoints are colored and have the same color, ignore and continue
               if nodes_color[edge[0]] == nodes_color[edge[1]]:
                    continue
               else:
                    # If both endpoints have different colors,
                    # change the color of the smallest tree,
                    # to the color of the largest one. Give e the same color.
                    if len(color_nodes[nodes_color[edge[0]]]) > len(color_nodes[nodes_color[edge[1]]]):
                         # change the color of small tree to the color of larger tree
                         color_nodes[nodes_color[edge[0]]] = \
                         color_nodes[nodes_color[edge[0]]] + \
                         color_nodes[nodes_color[edge[1]]]

                         deleted_color_nodes = color_nodes.pop(nodes_color[edge[1]], None)

                         for n in deleted_color_nodes:
                              nodes_color[n] = nodes_color[edge[0]]

                    else:
                         # change the color of small tree to the color of larger tree
                         color_nodes[nodes_color[edge[1]]] = \
                         color_nodes[nodes_color[edge[1]]] + color_nodes[nodes_color[edge[0]]]

                         deleted_color_nodes = color_nodes.pop(nodes_color[edge[0]], None)

                         for n in deleted_color_nodes:
                              nodes_color[n] = nodes_color[edge[1]]

          # aftered colored two nodes, add their edge to MST
          colored_edges.append(edge)

     return colored_edges


def hierholzer(unvisited_edges, existed_cycle=[]):
     # this statement shall never be true
     if len(unvisited_edges) == 0:
          return existed_cycle
     # if we found a cycle before, try find another edge that connected to this edge
     if len(existed_cycle):
          for edge in unvisited_edges:
               if edge[0] in existed_cycle:
                    start_edge = [edge[0], edge[1]]
                    break
               elif edge[1] in existed_cycle:
                    start_edge = [edge[1], edge[0]]
                    break

          unvisited_edges.remove(edge)
          # use the endpoint of the unvisited edge that connected to the existing cycle,
          # as the new start point of the cycle
          start_ind = existed_cycle.index(start_edge[0])
          existed_cycle = existed_cycle[start_ind:] + existed_cycle[:start_ind]
     else:
          # when we start, just pick a random node
          start_edge = unvisited_edges.pop()
     # find a cycle in the graph, there must be one, since all nodes has even degree
     cycle = find_cycle([start_edge[0], start_edge[1]], unvisited_edges)
     # concatenate the newly found cycle with old cycle
     if len(existed_cycle):
          cycle = existed_cycle + cycle
     # when unvisited edge exists, continue
     if len(unvisited_edges):
          return hierholzer(unvisited_edges, cycle)

     return cycle


def find_cycle(cycle_path, edge_list):
     # if end node is start node, we have a cycle
     # there should always a cycle, since all nodes have even degree
     if cycle_path[0] == cycle_path[-1]:
          return cycle_path

     i = 0
     #
     while i < len(edge_list):
          # if we found a edge connect the last node in the unfinished cycle path, we take it
          if edge_list[i][0] == cycle_path[-1]:
               cycle_path.append(edge_list[i][1])
               # remove the edge took
               del edge_list[i]
               # if there are unvisited nodes, continue
               if len(edge_list):
                    return find_cycle(cycle_path, edge_list)
               else:
                    return cycle_path

               break
          # if we found a edge connect the last node in the unfinished cycle path, we take it
          if edge_list[i][1] == cycle_path[-1]:
               cycle_path.append(edge_list[i][0])
               # remove the edge took
               del edge_list[i]
               # if there are unvisited nodes, continue
               if len(edge_list):
                    return find_cycle(cycle_path, edge_list)
               else:
                    return cycle_path

               break

          i += 1


def tsp(points):
     """Return one of the shortest tours that touches all points.

     Input:  A list of the form [n, (x_1, y_1), ..., (x_n, y_n)],
            where n is the number of points on a plane and (x_i, y_i) are their coordinates.
            We assume the Euclidean distance between the points (see the distance function below).
     Output: A list of point indices that corresponds to one of the shortes tours
            that start and end at point (x_1, y_1) and goe through each other point exactly once.

     """
     n = points[0]
     adjacency_list = {}

     for i in range(1, n+1):
          for j in range(i+1, n+1):
               # if these two points are not equal
               if points[i] != points[j]:
                    # compare x-axis first, put point with samller x-axis at first position
                    # if x-axis are equal, compare y-axis
                    if points[i][0] < points[j][0] or (points[i][0] == points[j][0] and points[i][1] < points[j][1]):
                         adjacency_list[(points[i], points[j])] = distance(points[i], points[j])
                    else:
                         adjacency_list[(points[j], points[i])] = distance(points[i], points[j])

     # adjacency_list is a dict like {(points0, points1): distance} 
     # {((0, 0), (1, 1)): 1.4142135623730951, ((0, 0), (0, 1)): 1.0, ((0, 1), (1, 1)): 1.0}
     # print(adjacency_list)#, len(adjacency_list), adjacency_list.keys())

     # sort `adjacency_list` by distances, so we can run kruskal algorithm on it 
     adjacency_list_sorted = {k: v for k, v in sorted(adjacency_list.items(), key=lambda item: item[1])}

     # we don't need the unsorted dict anymore
     del adjacency_list
     # print('adjacency_list_sorted', adjacency_list_sorted)

     # compute minimal weight spanning tree 
     spanning_tree = kruskal(adjacency_list_sorted)
     
     # spanning_tree is a list of tuples, tuple represent an edge connect two points,  [(points0, points1), ....]
     # [((0, 0), (0, 1)), ((0, 1), (1, 1))]
     # print('spanning_tree', spanning_tree)

     points_degree = {}
     # calculate degrees of nodes in spanning tree
     for edge in spanning_tree:
          if edge[0] not in points_degree:
               points_degree[edge[0]] = 0

          if edge[1] not in points_degree:
               points_degree[edge[1]] = 0

          points_degree[edge[0]] += 1
          points_degree[edge[1]] += 1

     # points_degree is a dict of {points: degree, }
     # the degree of points in the spanning tree
     # print(points_degree)
     
     spanning_tree_odd_nodes = []
     ind = 0
     # find nodes of odd degree in spanning tree 
     # compute a points <-> index mapping
     for p, d in points_degree.items():
          if d % 2 == 1:
               spanning_tree_odd_nodes.append(p)
               ind += 1

     del points_degree

     # spanning_tree_odd_nodes is a list of tuples (points) [points0, points1, ...]
     # [(0, 0), (1, 1)]
     # print('spanning_tree_odd_nodes', spanning_tree_odd_nodes)
     
     # length of odd degree nodes in spanning tree 
     ston_len = len(spanning_tree_odd_nodes)
     # build a adjacency matrix with the nodes of odd degree in spanning tree
     odd_nodes_admatrix = [[0 for _ in range(ston_len)] for _ in range(ston_len)]

     # odd_nodes_admatrix is a adjacency matrix, initial it with 0 2-d array
     # 2-d array, contains distances (edge weights) between points.
     # print(odd_nodes_admatrix)

     edge_max_weight = 0

     for i1, p1 in enumerate(spanning_tree_odd_nodes):
          for i2, p2 in enumerate(spanning_tree_odd_nodes):
               if p1 != p2:
                    # this how we store the adjacency_list
                    if p1[0] < p2[0] or (p1[0] == p2[0] and p1[1] < p2[1]):
                         odd_nodes_admatrix[i1][i2] = adjacency_list_sorted[(p1, p2)]
                         odd_nodes_admatrix[i2][i1] = adjacency_list_sorted[(p1, p2)]

                         if adjacency_list_sorted[(p1, p2)] > edge_max_weight:
                              edge_max_weight = adjacency_list_sorted[(p1, p2)]

     edge_max_weight = edge_max_weight + 1

     # 2-d array, contains distances (edge weights) between points. all 0 on diagonal (no edges connect node itself)
     # [[0, 1.4142135623730951], [1.4142135623730951, 0]]
     # print(odd_nodes_admatrix)
     
     ######## use networkx algorithm for perfect matching
     G = nx.Graph()

     G.add_nodes_from(range(ston_len))
     # list of weighted edges, [(point0_index, point1_index, weight)]
     weighted_edges = []

     for i in range(ston_len):
          for j in range(i+1, ston_len):
               weighted_edges.append((i, j, edge_max_weight - odd_nodes_admatrix[i][j]))

     # print(weighted_edges)

     G.add_weighted_edges_from(weighted_edges)

     perfect_matching = nx.algorithms.matching.max_weight_matching(G, maxcardinality=True)

     # print('odd_nodes_admatrix', odd_nodes_admatrix)
     # calculate a perfect mathing with the nodes of odd degree in spanning tree
     # perfect_matching = find_minimum_weight_matching(odd_nodes_admatrix)

     ######## use networkx algorithm for perfect matching


     # `perfect_matching` contains points index which is index of spanning_tree_odd_nodes
     # transfer posints_index back to points in euclidean plane
     perfect_matching_points = []

     # find_minimum_weight_matching return a list of index of points, 
     # here we convert index back to points
     for edge in list(perfect_matching):
          p1 = spanning_tree_odd_nodes[edge[0]]
          p2 = spanning_tree_odd_nodes[edge[1]]
          if p1[0] < p2[0] or (p1[0] == p2[0] and p1[1] < p2[1]):
               perfect_matching_points.append((p1, p2))
          else:
               perfect_matching_points.append((p2, p1))

     # `perfect_matching_points` is a list of tuples, [(point0, point1), ....], point is a tuple of coordinates
     # print('perfect_matching', perfect_matching_points)

     # compute the union of perfect matching and spanning tree
     union_spanning_tree_matching = []
     # convert the points to index
     for edge in spanning_tree:
          pi1 = points.index(edge[0])
          pi2 = points.index(edge[1])

          if pi1 < pi2:
               union_spanning_tree_matching.append((pi1, pi2))
          else:
               union_spanning_tree_matching.append((pi2, pi1))

     # convert the points to index
     for edge in perfect_matching_points:
          pi1 = points.index(edge[0])
          pi2 = points.index(edge[1])
          
          if pi1 < pi2 and (pi1, pi2) not in union_spanning_tree_matching:
               union_spanning_tree_matching.append((pi1, pi2))
          else:
               union_spanning_tree_matching.append((pi2, pi1))

     # `union_spanning_tree_matching` is a list of tuple,
     # tuples are two points index, represent an edge
     # print('union_spanning_tree_matching', union_spanning_tree_matching)

     # compute a eulerian cycle on the union, there must be one, since all nodes have even degree
     eulerian_cycle = hierholzer(union_spanning_tree_matching)
     # a list of point index, may contain duplicate index
     # print('eulerian_cycle', eulerian_cycle)

     start_index = eulerian_cycle.index(1)

     hamiltonian_cycle = []
     # remove repeated nodes, we start from node 1
     for node in eulerian_cycle[start_index:] + eulerian_cycle[:start_index]:
          if node not in hamiltonian_cycle:
               hamiltonian_cycle.append(node)

     # make it a cycle
     hamiltonian_cycle.append(hamiltonian_cycle[0])
     # print('hamiltonian_cycle', hamiltonian_cycle)
     
     return hamiltonian_cycle

def main(input):
    output = solve_tsp(input)
    return output

if __name__ == '__main__':
    main(input)
