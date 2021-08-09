from typing import List


def solve(
    adj_lists: 'List[List[int]]',
    num_colors: int,
) -> List[int]:
    colored = [None for _ in range(len(adj_lists))]

    current_color = 0

    for node, adj_nodes in enumerate(adj_lists):
        # node is not colored yet
        if colored[node] is None:
            colored[node] = current_color

        # check neighbor of current node,
        # if one of it's neighbor has the same color, return empty list
        # otherwise continue to next node
        for adj_node in adj_nodes:
            if current_color == colored[adj_node]:
                return []

        current_color += 1

        if current_color >= num_colors:
            current_color = 0

    return colored


if __name__ == "__main__":

    adj_lists = [[1, 2], [0, 2, 3], [0, 1], [1]]
    n = 3

    res = solve(adj_lists, n)
    print(res)

    adj_lists = [[1, 2], [0, 2, 3], [0, 1], [1]]
    n = 2

    res = solve(adj_lists, n)
    print(res)
