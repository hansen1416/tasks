def get_max_value_greedy(value_weight_pairs, weight_limit):
    sum_ws = 0
    sum_vs = 0
    for v, w in sorted(value_weight_pairs, key=lambda p: -p[0] / p[1]):
        if sum_ws + w <= weight_limit:
            sum_ws += w
            sum_vs += v
    return sum_vs


def solve(
    n: int,
    weight_limit: float
) -> 'List[Tuple[float, float]]':

    """
    produce a set of items where the greedy approach will fail to achieve the maximal value.
    """

    value_weight_pairs = []
    optim_weight = weight_limit / (n-1)

    while n > 0:

        if n > 1:
            value_weight_pairs.append((1, optim_weight))
        else:
            value_weight_pairs.append((1.5, optim_weight + 0.1 * optim_weight))

        n -= 1

    return value_weight_pairs
    

if __name__ == "__main__":

    n = 3
    weight_limit = 2

    value_weight_pairs = solve(n, weight_limit)

    print(value_weight_pairs)

    res = get_max_value_greedy(value_weight_pairs, weight_limit)

    print(res)