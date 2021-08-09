from sys import maxsize
from itertools import permutations
V = 4

# implementation of traveling Salesman Problem


def travellingSalesmanProblem(graph):

    s = 0

    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

    return min_path


if __name__ == "__main__":
    points = [4, (0, 0), (1, 1), (0, 1), (1, 0)]

    dist_lists = [[0, 10, 40, 20], [20, 0, 30, 50],
                  [20, 70, 0, 25], [120, 30, 55, 0]]

    res = travellingSalesmanProblem(dist_lists)

    print(res)
