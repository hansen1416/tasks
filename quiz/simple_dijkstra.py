from heapq import heappop, heappush

def solve(
    adj_node_weight_lists: 'List[List[Tuple[int, float]]]',
    src_node: int,
    dst_node: int,
) -> float:

    n = len(adj_node_weight_lists)
    adj_matrix = [[float('inf')] * n for _ in range(n)]

    for i, weight_list in enumerate(adj_node_weight_lists):
        for (j, weight) in weight_list:
            # print(i, j, weight)
            adj_matrix[i][j] = weight
    
    # graph, n = adj_matrix, len(adj_matrix)
    # HINT: use a parent array to store a parent for each vertice
    heap, path = [], []
    used = [False for i in range(n)]
    
    # YOUR CODE GOES HERE
    distance = [float("inf") for i in range(n)]
    parent = [-1] * n

    heappush(heap, (0, src_node))
    distance[src_node] = 0
    parent[src_node] = src_node

    
    while len(heap) > 0:
        d, v = heappop(heap)
        used[v] = True
        
        if distance[v] < d:
            continue
            
        for u in range(n):
            if not used[u] and adj_matrix[v][u] != float('inf') and distance[u] > (d + adj_matrix[v][u]):
                distance[u] = d + adj_matrix[v][u]
                heappush(heap, (distance[u], u))
                parent[u] = v
    
    if distance[dst_node] == float('inf'):
        return -1

    path.append(dst_node)

    while dst_node != src_node:
        path.append(parent[dst_node])
        dst_node = parent[dst_node]

    distance = 0
    prev_node = None

    for p in path[::-1]:
        if prev_node is not None:
            distance += adj_matrix[prev_node][p]

        prev_node = p
    
    return distance #, path[::-1]


if __name__ == "__main__":
    adj_node_weight_lists = [[(1, 10), (2, 40)], [(0, 10), (2, 20)], [(0, 40), (1, 20)]]
    src_node = 0
    dst_node = 2

    res = solve(adj_node_weight_lists, src_node, dst_node)

    print(res)