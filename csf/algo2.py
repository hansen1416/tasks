import math
import random
import time

def tsp(data):

    s0 = time.time()

    # build a graph
    G = build_graph(data[0], data)
    # print("Graph: ", G)

    if (data[0] > 2000):
        path = list(range(1, data[0]+1))
        path.append(path[0])

        return two_opt(path, G, limit_time=True, start_time = s0)

    # s1 = time.time()
    # print('build graph', s1-s0)

    # build a minimum spanning tree
    MSTree = minimum_spanning_tree(G)
    # print("MSTree: ", MSTree)

    # s2 = time.time()
    # print('mst', s2-s1)

    # find odd vertexes
    odd_vertexes = find_odd_vertexes(MSTree)
    # print("Odd vertexes in MSTree: ", odd_vertexes)

    # s3 = time.time()
    # print('odd vertices', s3-s2)

    # add minimum weight matching edges to MST
    minimum_weight_matching(MSTree, G, odd_vertexes)
    # print("Minimum weight matching: ", MSTree)

    # s4 = time.time()
    # print('mwm', s4-s3)

    # find an eulerian tour
    eulerian_tour = find_eulerian_tour(MSTree)
    # print("Eulerian tour: ", eulerian_tour)

    # s5 = time.time()
    # print('et', s5-s4)

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

    # s6 = time.time()
    # print('build path', s6-s5)

    best = two_opt(path, G)

    # s7 = time.time()
    # print('2 opt', s7-s6)

    # print(path, best)
    # print("Result path: ", path)

    return best

def cost_change(G, n1, n2, n3, n4):
    return G[n1][n3] + G[n2][n4] - G[n1][n2] - G[n3][n4]

def two_opt(route, G, limit_time=False, start_time=0):
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

        if limit_time:
            spent = time.time()
            if spent - start_time > 28:
                break

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
