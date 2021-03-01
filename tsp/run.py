import matplotlib.pyplot as ppl
import math

from tsp import tsp

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

    path = tsp(points)
    
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

    x = [point[0] for point in points[1:]]
    y = [point[1] for point in points[1:]]

    ppl.scatter(x,y)

    short = [1, 39, 25, 3, 24, 12, 33, 41, 31, 26, 6, 15, 7, 11, 13,
        19, 16, 36, 2, 5, 8, 22, 10, 38, 37, 20, 23, 29, 9, 4, 17,
        44, 32, 35, 42, 18, 14, 30, 21, 43, 27, 28, 45, 40, 34, 1]

    for i in range(len(short)-1) :
        a = points[short[i]]
        b = points[short[i+1]]
        ppl.plot([a[0], b[0]], [a[1], b[1]],'black')