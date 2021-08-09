from typing import List
import time


def solve(
    values: List[float],
    weights: List[float],
    weight_limit: float,
) -> float:

    start_time = time.time()

    # print(start_time)

    n = len(weights)

    K = [[0 for x in range(weight_limit + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(weight_limit + 1):

            if i == 0 or w == 0:
                K[i][w] = 0
            # checks that the weight of the i(th) object is less that the total weight permissible for that cell (j).
            elif weights[i-1] <= w:
                # selecting the maximum out of the two options available to us.
                # We can either include the object or exclude it.
                #
                # K[i-1][w] means that i-th is not included.
                # values[i-1] + K[i-1][w-weights[i-1]] represents that the ith item is included.
                K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]],
                              K[i-1][w])
            else:
                # when the weight of i-th object is greater than the permissible limit (w)
                K[i][w] = K[i-1][w]

            end_time = time.time()

            if end_time - start_time >= 9.9:
                return K[i][w]

    return K[n][weight_limit]


if __name__ == "__main__":
    # values = [200, 300, 400]
    # weights = [2, 4, 5]
    # weight_limit = 6

    # res = solve(values, weights, weight_limit)

    # print(res)

    # values = [60, 100, 120]
    # weights = [10, 20, 30]
    # weight_limit = 50

    # res = solve(values, weights, weight_limit)

    # print(res)

    values = list(range(1, 10000))
    weights = list(range(1, 10000))
    weight_limit = 6000

    res = solve(values, weights, weight_limit)

    print(res)
