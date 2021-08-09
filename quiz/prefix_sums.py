def perform_queries(array, queries):
    c = []
    # your code here
    prefix_sum = [0]
    for item in array:
        prefix_sum.append(prefix_sum[-1] + item)

    # print(prefix_sum)
    for query, l_i, r_i in queries:
        c.append(prefix_sum[r_i] - prefix_sum[l_i])

    return c

# MAIN -------------------------------------------------------------------------


def main(input):
    output = perform_queries(input[0], input[1])
    return output


if __name__ == '__main__':
    # main(input)

    array = [10, 2, 3, 4, 5]

    queries = [('get_sum', 0, 1), ('get_sum', 0, 5), ('get_sum', 2, 5)]

    res = perform_queries(array, queries)

    print(res)
