# https://github.com/PankajJ08/DataStructure/blob/master/knight_tour_warnsdorf.py

"""Solution of Knight tour problem using Warnsdorf's rule."""

import sys

# sys.setrecursionlimit(10000)            # use this for larger values of N
sys.setrecursionlimit(50000)   

# N = 8
# x_initial, y_initial = 0, 0


def is_safe(board, x, y, num_rows, num_cols):
    return 0 <= x < num_rows and 0 <= y < num_cols and board[x][y] == -1


def solve_tour(num_rows, num_cols, start_row, start_col):
    """Function to find one of the feasible knight tours."""
    board = [[-1 for _ in range(num_cols)] for _ in range(num_rows)]
    board[start_row][start_col] = 0

    # all 8 possible moves of knight at any given position
    jumps = ((-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1))
    z = find_tour(board, start_row, start_col, 1, jumps)
    if not z:
        # print("No solution exist!")
        return None
    return board



def find_tour(board, x, y, move_k, jumps):
    """Recursive function that return whether a solution exist from the given position."""
    num_rows = len(board)
    num_cols = len(board[0])
    if move_k == num_rows * num_cols:
        # for i in range(N):
        #     for j in range(N):
        #         print("%3d" % board[i][j], end=" ")
        #     print()
        return True

    sorted_moves = min_degree(board, x, y, jumps)

    for x_next, y_next in sorted_moves:
        board[x_next][y_next] = move_k

        if find_tour(board, x_next, y_next, move_k + 1, jumps):
            return True

        board[x_next][y_next] = -1          # backtrack

    return False


def min_degree(board, x, y, jumps):
    """Function that return the list of sorted moves in increasing order of degree."""
    num_rows = len(board)
    num_cols = len(board[0])
    empty_neighbours = []

    for jump in jumps:
        x_next = x + jump[0]
        y_next = y + jump[1]

        if is_safe(board, x_next, y_next, num_rows, num_cols):
            empty_neighbours.append([x_next, y_next])

    sorted_moves = sorted(empty_neighbours, key=lambda c: sum(
        [is_safe(board, c[0] + j[0], c[1] + j[1], num_rows, num_cols) for j in jumps]))
    return sorted_moves



def solve(num_rows, num_cols, start_row, start_col):
  
    board = solve_tour(num_rows, num_cols, start_row, start_col)
    if board is None:
        return []
    res = [0]*(num_rows*num_cols)
    for i in range(num_rows):
        for j in range(num_cols):
            # print(i, j)
            # print(i, j, board[i],  board[i][j])
            # print(i, j, board[i][j], len(res), len(board), len(board[0]))
            res[board[i][j]] = (i,j)
    return res          

    
def main(input):
    res = solve(input[0], input[1],input[2], input[3])
    return res

# N = 11
# M = 8
# res = solve(N,M,0,0)
# print(res, len(res))
# res = solve(3,3,0,0)
# print(res, len(res))
# if __name__ == "__main__":
#     solve_tour()

