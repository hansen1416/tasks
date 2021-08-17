from typing import List
from heapq import heappop, heappush


def words_diff(word1, word2):
    """
    all words are of the same length
    """
    diff = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff += 1

    return diff


def solve(
    all_words: List[str],
    begin_word: str,
    end_word: str,
) -> int:

    if begin_word not in all_words:
        all_words.append(begin_word)

    if end_word not in all_words:
        all_words.append(end_word)

    n = len(all_words)
    adj_matrix = [[float('inf')] * n for _ in range(n)]

    for i, w1 in enumerate(all_words):
        if w1 == begin_word:
            src_node = i

        if w1 == end_word:
            dst_node = i

        for j, w2 in enumerate(all_words):
            adj_matrix[i][j] = words_diff(w1, w2)

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

    score = 0
    prev_word = None

    for p in path[::-1]:
        if prev_word is not None:
            score += words_diff(prev_word, all_words[p]) ** 2

        prev_word = all_words[p]

    return score  # , path[::-1]


if __name__ == "__main__":
    all_words = ['vice', 'noon', 'mick', 'hear']
    begin_word = 'kick'
    end_word = 'nice'

    res = solve(all_words, begin_word, end_word)

    print(res)
