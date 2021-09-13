
from sys import maxsize
from itertools import permutations
from random import seed, randrange, random
 
# implementation of traveling Salesman Problem

def cal_length(r, euclidean_map):
    c = 0
    for i in range(len(r) - 1):
        j = i + 1
        c += euclidean_map[r[i]][r[j]]
    c += euclidean_map[r[0]][r[-1]]
    return c

def travellingSalesmanProblem(graph, s, e):
 
    # store all vertex apart from source vertex
    vertex = []
    for i in range(len(graph)):
        if i != s and i!= e:
            vertex.append(i)
 
    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation=permutations(vertex)
    res = None
    for i in next_permutation:
 
        # store current Path weight(cost)
        # current_pathweight = 0
 
        # # compute current path weight
        # k = s
        # for j in i:
        #     current_pathweight += graph[k][j]
        #     k = j
        # current_pathweight += graph[k][s]
        current_pathweight = cal_length([s] + list(i) + [e], graph )
        # update minimum
        if current_pathweight < min_path:
            min_path = current_pathweight
            res = i

        min_path = min(min_path, current_pathweight)
         
    return [s] + list(res) + [e]


def greedy_rotate(euclidean_map):
    # print("finding a greedy path...")
    globalTourLength = None
    globalTourRoute = []
    for p in range(len(euclidean_map)):
        unvisitedNodes = [i for i in range(len(euclidean_map))]
        tourLength = 0
        tourRoute = []
        currentNode = p
        while unvisitedNodes:
            unvisitedNodes.remove(currentNode)
            tourRoute.append(currentNode)
            neighbourLength = []
            for j in unvisitedNodes:
                neighbourLength.append((euclidean_map[currentNode][j], j))
            if len(neighbourLength) > 0:
                minNeighbourLength = neighbourLength[0][0]
                minNeighbour = neighbourLength[0][1]
                for i in neighbourLength:
                    if i[0] < minNeighbourLength:
                        minNeighbourLength = i[0]
                        minNeighbour = i[1]
                tourLength += minNeighbourLength
                currentNode = minNeighbour
            else:
                tourLength += euclidean_map[currentNode][p]
                currentNode = p
                tourRoute.append(currentNode)
                break
        if globalTourLength is None or tourLength < globalTourLength:
            globalTourLength = tourLength
            globalTourRoute = tourRoute
    return globalTourLength, globalTourRoute   

def randpos(route_len):
    return randrange(route_len)

def biased_flip(p):
    return True if random() < p else False


def cal_length(r, euclidean_map):
    c = 0
    for i in range(len(r) - 1):
        j = i + 1
        c += euclidean_map[r[i]][r[j]]
    c += euclidean_map[r[0]][r[-1]]
    return c

def two_opt(existing_route, euclidean_map):
    new_route = existing_route
    route_len = len(existing_route)-2
    randpos1 = randpos(route_len)
    randpos2 = randpos(route_len)
    t = new_route[randpos1]
    new_route[randpos1] = new_route[randpos2]
    new_route[randpos2] = t
    return new_route

def get_greedy_path(dist_lists):
    n = len(dist_lists)
    path = [0]
    available = [True] * n
    available[0] = False
    available[1] = False
    for _ in range(n - 2):
        i = min(range(n), key=lambda x: dist_lists[path[-1]][x] if available[x] else float('inf'))
        path.append(i)
        available[i] = False
    # path = two_opt(path, dist_lists)
    path.append(1)
    return path


def solve(
    dist_lists: 'List[List[float]]') -> 'List[int]':
    # return [0,3,2,1]
    # path = tsp(dist_lists)
    if len(dist_lists) <15:
        path = travellingSalesmanProblem(dist_lists, 0, 1)
        return path
    path = get_greedy_path(dist_lists)
    # path = travellingSalesmanProblem(dist_lists, 0, 1)
    # length = cal_length(path, dist_lists)
    # # length ,path= greedy_rotate(dist_lists)
    # path = two_opt(path, dist_lists)
    # print(greedy_rotate(dist_lists))
    return path


# dist_lists = [[0, 10, 40, 20], [20, 0, 30, 50], [20, 70, 0, 25], [120, 30, 55, 0]]


# print(solve(dist_lists))


# cal_length([0,2,3,1], dist_lists)
# cal_length([0,3,2,1], dist_lists)

# build_graph(dist_lists)