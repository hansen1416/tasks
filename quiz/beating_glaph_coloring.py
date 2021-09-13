import time
import random
def greedyColoring(adj, V):
    result = [-1] * V
    # Assign the first color to first vertex
    result[0] = 0;
    # A temporary array to store the available colors.
    # True value of available[cr] would mean that the
    # color cr is assigned to one of its adjacent vertices
    available = [False] * V
    # Assign colors to remaining V-1 vertices
    for u in range(1, V):
        # Process all adjacent vertices and
        # flag their colors as unavailable
        for i in adj[u]:
            # print(i, len(result))
            if (result[i] != -1):
                available[result[i]] = True
        # Find the first available color
        cr = 0
        while cr < V:
            if (available[cr] == False):
                break
            cr += 1
             
        # Assign the found color
        result[u] = cr
 
        # Reset the values back to false
        # for the next iteration
        for i in adj[u]:
            if (result[i] != -1):
                available[result[i]] = False
 
    # Pint the result
    return result
    # for u in range(V):
    #     print("Vertex", u, " --->  Color", result[u])

def addEdge(adj, v, w):
     
    adj[v].append(w)
     
    # Note: the graph is undirected
    adj[w].append(v) 
    return adj


g1 = [[] for i in range(5)]
g1 = addEdge(g1, 0, 1)
g1 = addEdge(g1, 0, 2)
g1 = addEdge(g1, 1, 2)
g1 = addEdge(g1, 1, 3)
g1 = addEdge(g1, 2, 3)
g1 = addEdge(g1, 3, 4)
# print("Coloring of graph 1 ")

def get_random_graph_b(n):
    edges = int(n*(n-2)/2)
    nodes = list(range(n))
    g1 = [[] for i in range(n)]
    for i in range(edges):
       i, j = random.sample(nodes, 2)
       g1 = addEdge(g1, i, j)
    return g1   



def solve(
    adj_lists: 'List[List[int]]',
    num_colors: int):
    res =  greedyColoring(adj_lists, len(adj_lists))
    return res
    if len(set(res))<= num_colors:
        return list(res)
    return []    


# adj_lists = [[1, 2], [0, 2, 3], [0, 1], [1]] 
# res = solve(adj_lists, 2)
# print(res)


# # n = 1000
# n_tests = 1000
# # g = get_random_graph_b(n)
# gs = [get_random_graph_b(n) for n in range(1,n_tests)]
# # print(g)
# print("here")
# tic = time.time()
# # res =  solve(g, n)
# [solve(gs[n-1], n) for n in range(1, n_tests)]

# toc = time.time()

# print(toc-tic)

