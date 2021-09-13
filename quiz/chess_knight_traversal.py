from typing import List, Tuple


def isSafe(row, col, num_rows, num_cols, board):
    '''
        A utility function to check if i,j are valid indexes
        for N*N chessboard
    '''
    if(row >= 0 and col >= 0 and row < num_rows and col < num_cols and board[row][col] == -1):
        return True
    return False


def solve(
    num_rows: int,
    num_cols: int,
    start_row: int,
    start_col: int,
) -> 'List[Tuple[int, int]]':
    '''
        This function solves the Knight Tour problem using
        Backtracking. This function mainly uses solveKTUtil()
        to solve the problem. It returns false if no complete
        tour is possible, otherwise return true and prints the
        tour.
        Please note that there may be more than one solutions,
        this function prints one of the feasible solutions.
    '''

    # Initialization of Board matrix
    board = [[-1 for _ in range(num_cols)]for _ in range(num_rows)]

    # move_x and move_y define next move of Knight.
    # move_x is for next value of x coordinate
    # move_y is for next value of y coordinate
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Since the Knight is initially at the first block
    board[start_row][start_col] = 0

    moves = [None] * (num_rows * num_cols)
    moves[0] = (start_row, start_col)

    # Step counter for knight's position
    pos = 1

    # Checking if solution exists or not
    if(not solveKTUtil(num_rows, num_cols, board, start_row, start_col, move_x, move_y, pos, moves)):
        return []
    else:
        return moves


def solveKTUtil(num_rows, num_cols, board, curr_x, curr_y, move_x, move_y, pos, moves):
    '''
        A recursive utility function to solve Knight Tour
        problem
    '''
    # print(pos)
    if(pos == num_rows * num_cols):
        return True

    # Try all next moves from the current coordinate x, y
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if(isSafe(new_x, new_y, num_rows, num_cols, board)):
            board[new_x][new_y] = pos
            moves[pos] = (new_x, new_y)
            if(solveKTUtil(num_rows, num_cols, board, new_x, new_y, move_x, move_y, pos+1, moves)):
                return True

            # Backtracking
            board[new_x][new_y] = -1

    return False


if __name__ == "__main__":
    # num_rows = 8
    # num_cols = 8
    # start_row = 0
    # start_col = 0

    # res = solve(num_rows, num_cols, start_row, start_col)

    # print(res)

    num_rows = 50
    num_cols = 50
    start_row = 0
    start_col = 0

    res = solve(num_rows, num_cols, start_row, start_col)

    print(res)
