def solve(
    bricks: 'List[Tuple[float, float, float]]',
    values: 'List[float]',
    weight_limit: float,
    density: float,
) -> float:
    brick_vols = [size[0] * size[1] * size[2] for size in bricks]

    val_por = sorted(
        range(len(values)),
        key = lambda i_ : brick_vols[i_] / values[i_],
    )
    
    indx = 0
    ps = []
    sum_val = 0.0

    while weight_limit > 0:

        pointer = val_por[indx]

        if brick_vols[pointer] * density <= weight_limit:
            vol = brick_vols[pointer]
            weight_limit -= brick_vols[pointer] * density
        else:
            vol = weight_limit / density
            weight_limit = 0

        ps.append((bricks[pointer], values[pointer], vol))

        sum_val += vol / brick_vols[pointer] * values[pointer]

        indx += 1

    return sum_val, ps


if __name__ == "__main__":
    bricks = [(1, 2, 3), (2, 3, 2)]
    values = [10, 15]
    weight_limit = 7.5 
    density = 2.5

    res = solve(bricks, values, weight_limit, density)

    print(res)