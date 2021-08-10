def squared(x):
    return pow(x, 2)


class SegmentTree():

    def __init__(self, array):

        n = len(array) - 1

        n |= n >> 1
        n |= n >> 2
        n |= n >> 4
        n |= n >> 8
        n |= n >> 16

        n += 1

        self.arr_len = n

        tree = [0] * (n-1) + array + [0] * (n - len(array))

        for i in range(n-2, -1, -1):
            # tree[i] = sum(tree[i*2 + 1: i*2 + 2])
            tree[i] = sum(tree[i*2 + 1: i*2 + 3])

        self.tree = tree

        # self.multiply_cache = {}

        # squared_array = list(map(squared, array))

        squared_tree = [0] * (n-1) + list(map(squared, array)) + \
            [0] * (n - len(array))

        for i in range(n-2, -1, -1):
            # tree[i] = sum(tree[i*2 + 1: i*2 + 2])
            squared_tree[i] = sum(squared_tree[i*2 + 1: i*2 + 3])

        self.squared_tree = squared_tree

    def get_sum(self, l, r):
        # get leaf with value 'l'
        l += self.arr_len - 1
        # get leaf with value 'r'
        r += self.arr_len - 2

        sum = 0

        while (l <= r):
            # print(l, r)
            if ((l % 2) == 0):
                # it means l is a right child
                sum += self.tree[l]
                # print("+ item:", self.tree[l])

                # move l to right by 1, so it becomes a left child and find its parent
                l = (l + 1 - 1) // 2
            else:
                # when l is a left child, when just find its parent
                l = (l - 1) // 2

            if ((r % 2) == 1):
                # it means r is a left chid
                sum += self.tree[r]
                # print("+ item:", self.tree[r])

                # move r to left by 1, so it becomes a right child and find its parent
                r = (r - 1 - 2) // 2
            else:
                # when r is a right child
                r = (r - 2) // 2

        return sum

    def get_squared_sum(self, l, r):
        # get leaf with value 'l'
        l += self.arr_len - 1
        # get leaf with value 'r'
        r += self.arr_len - 2

        sum = 0

        while (l <= r):
            # print(l, r)
            if ((l % 2) == 0):
                # it means l is a right child
                sum += self.squared_tree[l]
                # print("+ item:", self.tree[l])

                # move l to right by 1, so it becomes a left child and find its parent
                l = (l + 1 - 1) // 2
            else:
                # when l is a left child, when just find its parent
                l = (l - 1) // 2

            if ((r % 2) == 1):
                # it means r is a left chid
                sum += self.squared_tree[r]
                # print("+ item:", self.tree[r])

                # move r to left by 1, so it becomes a right child and find its parent
                r = (r - 1 - 2) // 2
            else:
                # when r is a right child
                r = (r - 2) // 2

        return sum

    def update(self, i, value):

        node = self.arr_len - 1 + i

        self.tree[node] = value
        self.squared_tree[node] = value ** 2

        while node > 0:
            node = (node - 1) // 2

            left_child = node * 2 + 1
            right_child = node * 2 + 2

            self.tree[node] = self.tree[left_child] + self.tree[right_child]
            self.squared_tree[node] = self.squared_tree[left_child] + \
                self.squared_tree[right_child]

        # print(self.tree)

    def multiply_range(self, l, r, k):

        # get leaf with value 'l'
        l += self.arr_len - 1
        # get leaf with value 'r'
        r += self.arr_len - 2

        while l >= 0:

            if l > self.arr_len:
                for i in range(l, r+1):
                    self.tree[i] = self.tree[i] * k
                    # self.tree[i] already multiplyed by k
                    self.squared_tree[i] = self.tree[i] ** 2
            else:
                for i in range(l, r+1):
                    # print(i, l, r)
                    self.tree[i] = self.tree[i*2+1] + self.tree[i*2+2]
                    self.squared_tree[i] = \
                        self.squared_tree[i*2+1] + self.squared_tree[i*2+2]

            if l % 2 == 0:
                l = (l-2) // 2
            else:
                l = (l-1) // 2

            if r % 1 == 0:
                r = (r - 1) // 2
            else:
                r = (r - 2) // 2

            # print(l, r)

        # print(self.tree)

    def get_variance(self, l, r):

        n = r-l
        range_sum = self.get_sum(l, r)
        range_squared_sum = self.get_squared_sum(l, r)
        range_mean = range_sum / n

        return (range_squared_sum - 2 * range_mean * range_sum + range_mean ** 2 * n) / n

    def print_trees(self):
        print(self.tree)
        print(self.squared_tree)


def perform_queries(array, queries):

    tree = SegmentTree(array)
    a = []

    # tree.print_trees()

    for query in queries:

        # Use tree to respond to queries
        if query[0] == 'get_sum':
            a.append(tree.get_sum(query[1], query[2]))
        elif query[0] == 'update':
            tree.update(query[1], query[2])
        elif query[0] == 'multiply_range':
            tree.multiply_range(query[1], query[2], query[3])
        elif query[0] == 'get_variance':
            a.append(tree.get_variance(query[1], query[2]))

            # print(dict(enumerate(tree.tree)))

    # tree.print_trees()

    return a


def main(input):
    output = perform_queries(input[0], input[1])
    return output


if __name__ == "__main__":

    # main(input)

    array = [10, 2, 3, 4, 5]
    # array = [10, 2, 3, 10, 5, 7, 8, 9, 10]

    queries = [('get_sum', 0, 2), ('update', 3, 10), ('get_sum', 2, 5)]
    queries = [('get_sum', 2, 8)]
    queries = [('multiply_range', 3, 5, 10)]
    queries = [('get_sum', 0, 2), ('multiply_range', 3, 5, 10),
               ('update', 3, 10), ('get_sum', 2, 5)]
    queries = [('get_variance', 0, 2), ('multiply_range', 3, 5, 10),
               ('update', 3, 10), ('get_variance', 2, 5)]

    res = perform_queries(array, queries)

    print(res)
