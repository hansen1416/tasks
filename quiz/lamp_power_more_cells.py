def solve(
    lamps: 'List[float]',
    cells: 'List[float]',
    cord_len: float,
) -> bool:

    """
    use two pinters on lamps and cells

    if diff between current lamp and current cell is less or equal to cord_len, 
    we can plug lamp, we move on to next lamp and cell, both pointers + 1

    if diff between current lamp and current cell is larger than cord_len,
    we first check 
    if current diff is larger than previous diff, 
    if yes, it means previous cell is too far away from lamp, 
    and it is not getting better, since the array is sorted, so we return False
    if current diff is less or equal than previous diff,
    there is still hope, we try next cell, cell pointer += 1 
    """

    lamps = sorted(lamps)
    cells = sorted(cells)

    lamp_p = 0
    cell_p = 0
    pre_diff = cord_len + 1

    while lamp_p < len(lamps):

        if cell_p >= len(cells):
            return False

        diff = abs(lamps[lamp_p] - cells[cell_p])

        if diff <= cord_len:
            lamp_p += 1
            cell_p += 1
            pre_diff = cord_len + 1
        else:
            if pre_diff < diff:
                return False
            else:
                pre_diff = diff
                cell_p += 1
        
    return True

if __name__ == "__main__":

    lamps = [1, 3.5, 8]
    cells = [2, 10, 4, 1, 7]
    cord_len = 1

    res = solve(lamps, cells, cord_len)

    print(res)

    lamps = [1, 3.5, 8]
    cells = [2, 10, 4, 1, 7]
    cord_len = 0.1

    res = solve(lamps, cells, cord_len)

    print(res)