import algo1
import algo2
import math

g1 = [[1380, 939], [2848, 96], [3510, 1671], [457, 334], [3888, 666], [984, 965], [2721, 1482], [1286, 525],
            [2716, 1432], [738, 1325], [1251, 1832], [2728, 1698], [3815, 169], [3683, 1533], [1247, 1945], [123, 862],
            [1234, 1946], [252, 1240], [611, 673], [2576, 1676], [928, 1700], [53, 857], [1807, 1711], [274, 1420],
            [2574, 946], [178, 24], [2678, 1825], [1795, 962], [3384, 1498], [3520, 1079], [1256, 61], [1424, 1728],
            [3913, 192], [3085, 1528], [2573, 1969], [463, 1670], [3875, 598], [298, 1513], [3479, 821], [2542, 236],
            [3955, 1743], [1323, 280], [3447, 1830], [2936, 337], [1621, 1830], [3373, 1646], [1393, 1368],
            [3874, 1318], [938, 955], [3022, 474], [2482, 1183], [3854, 923], [376, 825], [2519, 135], [2945, 1622],
            [953, 268], [2628, 1479], [2097, 981], [890, 1846], [2139, 1806], [2421, 1007], [2290, 1810], [1115, 1052],
            [2588, 302], [327, 265], [241, 341], [1917, 687], [2991, 792], [2573, 599], [19, 674], [3911, 1673],
            [872, 1559], [2863, 558], [929, 1766], [839, 620], [3893, 102], [2178, 1619], [3822, 899], [378, 1048],
            [1178, 100], [2599, 901], [3416, 143], [2961, 1605], [611, 1384], [3113, 885], [2597, 1830], [2586, 1286],
            [161, 906], [1429, 134], [742, 1025], [1625, 1651], [1187, 706], [1787, 1009], [22, 987], [3640, 43],
            [3756, 882], [776, 392], [1724, 1642], [198, 1810], [3950, 1558]]

g2 = [100, [1380, 939], [2848, 96], [3510, 1671], [457, 334], [3888, 666], [984, 965], [2721, 1482], [1286, 525],
            [2716, 1432], [738, 1325], [1251, 1832], [2728, 1698], [3815, 169], [3683, 1533], [1247, 1945], [123, 862],
            [1234, 1946], [252, 1240], [611, 673], [2576, 1676], [928, 1700], [53, 857], [1807, 1711], [274, 1420],
            [2574, 946], [178, 24], [2678, 1825], [1795, 962], [3384, 1498], [3520, 1079], [1256, 61], [1424, 1728],
            [3913, 192], [3085, 1528], [2573, 1969], [463, 1670], [3875, 598], [298, 1513], [3479, 821], [2542, 236],
            [3955, 1743], [1323, 280], [3447, 1830], [2936, 337], [1621, 1830], [3373, 1646], [1393, 1368],
            [3874, 1318], [938, 955], [3022, 474], [2482, 1183], [3854, 923], [376, 825], [2519, 135], [2945, 1622],
            [953, 268], [2628, 1479], [2097, 981], [890, 1846], [2139, 1806], [2421, 1007], [2290, 1810], [1115, 1052],
            [2588, 302], [327, 265], [241, 341], [1917, 687], [2991, 792], [2573, 599], [19, 674], [3911, 1673],
            [872, 1559], [2863, 558], [929, 1766], [839, 620], [3893, 102], [2178, 1619], [3822, 899], [378, 1048],
            [1178, 100], [2599, 901], [3416, 143], [2961, 1605], [611, 1384], [3113, 885], [2597, 1830], [2586, 1286],
            [161, 906], [1429, 134], [742, 1025], [1625, 1651], [1187, 706], [1787, 1009], [22, 987], [3640, 43],
            [3756, 882], [776, 392], [1724, 1642], [198, 1810], [3950, 1558]]



# p2 = algo2.tsp(g2)

# print(p2, len(p2))


# le1 = []
# le2 = []

# for i in range(10):
#     l1, _ = algo1.tsp(g1)
#     l2, _ = algo2.tsp(g2)

#     le1.append(l1)
#     le2.append(l2)

# m1 = sum(le1) / 10
# m2 = sum(le2) / 10

# print(m1, m2)

# import matplotlib.pyplot as ppl


def distance(p, q):
    """Return the Euclidean distance between points p = (a, b) and q = (c, d)."""
    return ((p[0]-q[0])**2 + (p[1]-q[1])**2) ** 0.5

def get_length(path, points):
    """Return the length of the path.
    
    Input:  path is a list of point indices;
            points is a list of the form [n, (x_1, y_1), ..., (x_n, y_n)],
            where n is the number of points on a plane and (x_i, y_i) are their coordinates. 
    Output: The length of the input path
            assuming the coordinates specified in the input
            and the Euclidean distance between the points.
    """
    return sum(distance(points[path[i]], points[path[i+1]]) for i in range(len(path) - 1))
        

def test(points, baseline_path, short_path):
    """Test the tsp function on points.
    
    baseline_path is the length of a simple solution.
    short_path is the length of a good solution.
    
    Your solution should run for at most 30 seconds
    and should return a path of length less than than baseline_path
    (the only exception is when baseline_path is almost equal to short_path;
    in this case, it is OK to return a path of similar length).
    The score you get depends on how short your path is. The score is the returned value of the function.
    
    """
    print("Baseline path: ", baseline_path)
    print("Short path: ", short_path)
    n = points[0]

    path = algo2.tsp(points)
    
    assert len(path) == n + 1, "The route must contain n + 1 points."
    assert path[0] == 1 == path[-1], "The route should start and end at point 1."
    assert set(path) == set(range(1, n + 1)), "The route must contain all n points."

    length = get_length(path, points)
    print("Your path: ", length)
    if length <= short_path + 0.00001: # If your path is just slightly longer than short_path or shorter, you get 10. 
        return 10.0    
    if length >= baseline_path: # If it is the same as the baseline or longer, you get 1.
        return 1
    # Otherwise, the number of points you get depends on how close your path is to short_path.
    return math.ceil((baseline_path-length) / (baseline_path-short_path) * 10)


if __name__ == "__main__":

    # Square 1 x 1. Your algorithm is expected to find a shortest tour, e.g., [1, 3, 2, 4, 1].
    points = [4, (0, 0), (1, 1), (0, 1), (1, 0)]
    length = get_length([1, 3, 2, 4, 1], points)
    assert test(points, length, length) == 10


    # Line y = x + 1. Your algorithm is expected to find a shortest tour, e.g., [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1].
    points = [10, (1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20)]
    length = get_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1], points)
    assert test(points, length, length) == 10

    # x = [point[0] for point in points[1:]]
    # y = [point[1] for point in points[1:]]

    # ppl.scatter(x,y)

    # short = [1, 39, 25, 3, 24, 12, 33, 41, 31, 26, 6, 15, 7, 11, 13,
    #     19, 16, 36, 2, 5, 8, 22, 10, 38, 37, 20, 23, 29, 9, 4, 17,
    #     44, 32, 35, 42, 18, 14, 30, 21, 43, 27, 28, 45, 40, 34, 1]

    # for i in range(len(short)-1) :
    #     a = points[short[i]]
    #     b = points[short[i+1]]
    #     ppl.plot([a[0], b[0]], [a[1], b[1]],'black')

    points = [25,
            (6139, -9327),
            (7524, 9018),
            (-8201, -4582),
            (5277, -13042),
            (2541, 156),
            (-6748, 14001),
            (12371, 6187),
            (-3191, 3754),
            (-14173, 11185),
            (1725, 14670),
            (-14467, 12589),
            (-703, -13791),
            (6151, -7013),
            (1367, 14568),
            (-13867, 14509),
            (405, -6256),
            (6185, -13240),
            (7325, 5230),
            (845, 339),
            (7181, -2898),
            (-2921, -4544),
            (10395, 808),
            (11313, 2696),
            (-5320, 11409),
            (3790, 10442)
            ]

    baseline = get_length(
        [1, 13, 20, 22, 23, 7, 18, 2, 25, 10, 14, 24, 6, 15, 11, 9, 8, 19, 5, 16, 21, 3, 12, 4, 17, 1],
        points)
    short = get_length(
        [1, 17, 4, 12, 3, 21, 16, 5, 19, 8, 9, 11, 15, 6, 24, 14, 10, 25, 2, 18, 7, 23, 22, 20, 13, 1],
        points)

    test(points, baseline, short)

    points = [45,
            (175, 17),
            (134, 299),
            (244, 76),
            (17, 61),
            (111, 273),
            (195, 170),
            (155, 209),
            (57, 251),
            (57, 47),
            (100, 176),
            (182, 251),
            (272, 126),
            (213, 232),
            (131, 52),
            (174, 201),
            (239, 281),
            (8, 40),
            (142, 14),
            (298, 244),
            (28, 121),
            (151, 101),
            (40, 203),
            (70, 105),
            (290, 99),
            (294, 27),
            (221, 153),
            (182, 78),
            (186, 60),
            (70, 52),
            (151, 70),
            (218, 122),
            (58, 8),
            (240, 134),
            (178, 40),
            (71, 20),
            (153, 299),
            (25, 125),
            (6, 148),
            (245, 14),
            (177, 41),
            (237, 116),
            (94, 16),
            (158, 107),
            (3, 21),
            (194, 47)
            ]

    baseline = get_length(
        [1, 34, 40, 45, 28, 27, 30, 14, 18, 42, 35, 32, 9, 29, 23,
        20, 37, 38, 22, 8, 5, 2, 36, 11, 13, 15, 7, 6, 26, 33, 41,
        31, 3, 24, 12, 25, 39, 43, 21, 10, 4, 17, 44, 16, 19, 1],
        points)
    short = get_length(
        [1, 39, 25, 3, 24, 12, 33, 41, 31, 26, 6, 15, 7, 11, 13,
        19, 16, 36, 2, 5, 8, 22, 10, 38, 37, 20, 23, 29, 9, 4, 17,
        44, 32, 35, 42, 18, 14, 30, 21, 43, 27, 28, 45, 40, 34, 1],
        points)

    test(points, baseline, short)