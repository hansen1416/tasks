def solve(
    lamps: 'List[float]',
    cells: 'List[float]',
    cord_len: float,
) -> bool:
    
    the_max = max(
        abs(lamp - cell) for lamp, cell in
        zip(sorted(lamps), sorted(cells))
    )
        
    return the_max <= cord_len

if __name__ == "__main__":

    lamps = [1, 3.5, 8]
    cells = [2, 10, 4]
    cord_len = 2

    # lamps = [1, 3.5, 8]
    # cells = [2, 10, 4]
    # cord_len = 1

    res = solve(lamps, cells, cord_len)

    print(res)