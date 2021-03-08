import math
import random
import networkx as nx

def tsp(data):

    if data[0] <= 100:

        min_tw = float('inf')
        min_path = []
        
        for i in range(3):
            tw, path = tsp_nx(data)

            if tw < min_tw:
                min_tw = tw
                min_path = path

        return min_path

    # build a graph
    G = build_graph(data[0], data)
    # print("Graph: ", G)

    # build a minimum spanning tree
    MSTree = minimum_spanning_tree(G)
    # print("MSTree: ", MSTree)

    # find odd vertexes
    odd_vertexes = find_odd_vertexes(MSTree)
    # print("Odd vertexes in MSTree: ", odd_vertexes)

    # add minimum weight matching edges to MST
    minimum_weight_matching(MSTree, G, odd_vertexes)
    # print("Minimum weight matching: ", MSTree)

    # find an eulerian tour
    eulerian_tour = find_eulerian_tour(MSTree, G)

    # print("Eulerian tour: ", eulerian_tour)

    start_i = eulerian_tour.index(1)
    path = []
    visited = [False] * len(eulerian_tour)
    visited[0] = True

    # length = 0

    for v in eulerian_tour[start_i:] + eulerian_tour[:start_i]:
        if not visited[v]:
            path.append(v)
            visited[v] = True

            # length += G[current][v]
            current = v

    path.append(path[0])

    best = two_opt(path, G)

    # print(path, best)
    # print("Result path: ", path)

    return best

def cost_change(G, n1, n2, n3, n4):
    return G[n1][n3] + G[n2][n4] - G[n1][n2] - G[n3][n4]

def two_opt(route, G):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):

                if j - i == 1: continue
                if cost_change(G, best[i - 1], best[i], best[j - 1], best[j]) < -1:
                    best[i:j] = best[j - 1:i - 1:-1]
                    improved = True

        route = best
    return best

def get_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1.0 / 2.0)


def build_graph(n, points):
    graph = {}
    # n = len(data)

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                if i not in graph:
                    graph[i] = {}

                graph[i][j] = get_distance(points[i][0], points[i][1], points[j][0], points[j][1])

    return graph


class UnionFind:
    def __init__(self):
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def __iter__(self):
        return iter(self.parents)

    def union(self, *objects):
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r], r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest


def minimum_spanning_tree(G):
    tree = []
    subtrees = UnionFind()
    for W, u, v in sorted((G[u][v], u, v) for u in G for v in G[u]):
        if subtrees[u] != subtrees[v]:
            tree.append((u, v, W))
            subtrees.union(u, v)

    return tree


def find_odd_vertexes(MST):
    tmp_g = {}
    vertexes = []
    for edge in MST:
        if edge[0] not in tmp_g:
            tmp_g[edge[0]] = 0

        if edge[1] not in tmp_g:
            tmp_g[edge[1]] = 0

        tmp_g[edge[0]] += 1
        tmp_g[edge[1]] += 1

    for vertex in tmp_g:
        if tmp_g[vertex] % 2 == 1:
            vertexes.append(vertex)

    return vertexes


def minimum_weight_matching(MST, G, odd_vert):
    
    random.shuffle(odd_vert)

    while odd_vert:
        v = odd_vert.pop()
        length = float("inf")
        u = 1
        closest = 0
        for u in odd_vert:
            if v != u and G[v][u] < length:
                length = G[v][u]
                closest = u

        MST.append((v, closest, length))
        odd_vert.remove(closest)


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

def cost_change_nx(G, n1, n2, n3, n4):
    return G.get_edge_data(n1, n3)['weight'] + G.get_edge_data(n2, n4)['weight'] - \
        G.get_edge_data(n1, n2)['weight'] - G.get_edge_data(n3, n4)['weight']

def two_opt_nx(route, G):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):

                if j - i == 1: continue
                if cost_change_nx(G, best[i - 1], best[i], best[j - 1], best[j]) < -1:
                    best[i:j] = best[j - 1:i - 1:-1]
                    improved = True

        route = best
    return best

def tsp_nx(points):
    G = nx.Graph()

    n = points[0]

    li = list(range(1, n+1))
    random.shuffle(li)

    for i in li:
        for j in li:
            if i < j:
                G.add_edge(i, j, weight=get_distance(points[i][0], points[i][1], points[j][0], points[j][1]))
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
    max_w = 99999999999

    for edge in list(odd_node_sub.edges(data=True)):
        # G.add_edge(i, j, weight=distance(points[i], points[j]))
        odd_node_sub_rev.add_edge(edge[0], edge[1], weight=(max_w - edge[2]['weight']))

    # print(odd_node_sub_rev.edges(data=True))

    mpm = nx.algorithms.matching.max_weight_matching(odd_node_sub_rev, maxcardinality=True)

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

    result = two_opt_nx(hamiltonian_cycle, G)

    tw = 0

    for i in range(0, n):
        tw += G.get_edge_data(result[i], result[i+1])['weight']
        # print(result[i], result[i+1], G.get_edge_data(result[i], result[i+1])['weight'])

    # print(result)

    return tw, result