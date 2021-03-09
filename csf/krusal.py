import random

def get_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1.0 / 2.0)

# Find set of vertex i 
def find(parent, i):
    while parent[i] != i: 
        i = parent[i] 
    return i
  
# Does union of i and j. It returns 
# false if i and j are already in same  
# set.  
def union(parent, i, j): 
    a = find(parent, i) 
    b = find(parent, j) 
    parent[a] = b 
  
# Finds MST using Kruskal's algorithm  
def kruskalMST(V, cost): 
    # mincost = 0 # Cost of min MST 
  
    # Initialize sets of disjoint sets 
    parent = {i:i for i in range(1, V+1)}
    # for i in range(V): 
    #     parent[i] = i 
  
    # Include minimum weight edges one by one  
    edge_count = 0
    mst = []

    while edge_count < V - 1: 
        mini = float('inf') 
        a = -1
        b = -1
        for i in range(1, V+1): 
            for j in range(1, V+1):
                if find(parent, i) != find(parent, j) and cost[i][j] < mini: 
                    mini = cost[i][j] 
                    a = i 
                    b = j 
        union(parent, a, b) 
        # print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, min)) 
        mst.append((a,b,mini))

        edge_count += 1
        # mincost += min
    
    # print("Minimum cost= {}".format(mincost)) 
    return mst

  
def build_graph(n, points):
    graph = {}

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                if i not in graph:
                    graph[i] = {}

                graph[i][j] = get_distance(points[i][0], points[i][1], points[j][0], points[j][1])

    return graph


n = 1001

x = list(range(1, n))
y = list(range(1, n))

random.shuffle(x)
random.shuffle(y)

points = [len(x)]
# print(points[0])
for i in range(n-1):
    points.append((x[i], y[i]))

cost = build_graph(points[0], points)

# print(cost)

# Print the solution  
mst = kruskalMST(points[0], cost)

print(mst)