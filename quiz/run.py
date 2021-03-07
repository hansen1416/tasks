import numpy as np

def bound_prob_correct(p, n) :
    # modify the formula below
    return exp(-1* p / 8)

b = bound_prob_correct(1, 2)
assert 0.75 - 1e-10 < b and b < 1.383, b

b = bound_prob_correct(8, 2)
assert 0.564 < b and b < .868, b