import math

def tsp(data):
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

    # print("Result path: ", path)
    # print("Result length of the path: ", length)

    return path


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
    import random
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


def find_eulerian_tour(MatchedMSTree, G):
    print('MatchedMSTree', MatchedMSTree)
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
    print('EP', EP)
    return EP


def remove_edge_from_matchedMST(MatchedMST, v1, v2):

    for i, item in enumerate(MatchedMST):
        if (item[0] == v2 and item[1] == v1) or (item[0] == v1 and item[1] == v2):
            del MatchedMST[i]

    return MatchedMST

if __name__ == "__main__":

    def distance(p, q):
        """Return the Euclidean distance between points p = (a, b) and q = (c, d)."""
        return ((p[0]-q[0])**2 + (p[1]-q[1])**2) ** 0.5

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

    # x = [point[0] for point in points[1:]]
    # y = [point[1] for point in points[1:]]

    # ppl.scatter(x,y)

    # short = [1, 39, 25, 3, 24, 12, 33, 41, 31, 26, 6, 15, 7, 11, 13,
    #     19, 16, 36, 2, 5, 8, 22, 10, 38, 37, 20, 23, 29, 9, 4, 17,
    #     44, 32, 35, 42, 18, 14, 30, 21, 43, 27, 28, 45, 40, 34, 1]

    # for i in range(len(short)-1) :
    #     a = points[short[i]]
    #     b = points[short[i+1]]
    #     ppl.plot([a[0], b[0]], [a[1], b[1]],'black')

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