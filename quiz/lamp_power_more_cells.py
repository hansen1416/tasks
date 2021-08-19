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

    # print(lamps, cells)

    lamp_p = 0
    cell_p = 0
    # pre_diff = cord_len + 1

    while lamp_p < len(lamps):

        if cell_p >= len(cells):
            return False

        diff = abs(lamps[lamp_p] - cells[cell_p])
        # print(diff)
        if diff <= cord_len:
            lamp_p += 1
            cell_p += 1
            # pre_diff = cord_len + 1
        else:
            # pre_diff = diff
            cell_p += 1
            # if pre_diff < diff:
            #     return False
            # else:
            #     pre_diff = diff
            #     cell_p += 1
        
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

    lamps = [10, -10]
    cells = [8, -2, -1, -12]
    cord_len = 10

    res = solve(lamps, cells, cord_len)

    print(res)




    # Some tests failed. Per-test feedbacks:
    #  ["wrong answeron test {'lamps': [10, -10], 'cells': [8, -2, -1, -12], 'cord_len': 10}", 
    # "wrong answeron test {'lamps': [6, 5, -29, 25, -23], 'cells': [-36, 11, -44, 35, 7, 2, -31, 22, 50, -23], 'cord_len': 10}", 
    # "wrong answeron test {'lamps': [-56, 24, 94, -59, 43, -65, -54, 32, 31, 91], 'cells': [-27, 32, -86, -74, -33, -30, -93, 30, 70, 54, 37, 93, 10, 67, -57, 56, 64, -35, 86, -96], 'cord_len': 100}", 'Ok',
    # "wrong answeron test {'lamps': [43, 170, 103, -85, -149, -67, -97, 90, -194, 63, 64, -32, 121, 60, -79, -22, -186, -163, -191, 121], 'cells': [-169, 46, -11, -91, -156, -59, 86, 58, -124, -124, 10, 134, -40, -157, -54, -22, 49, -9, 105, -148, -166, -173, -32, 73, -46, -48, 98, -106, -190, 98, -156, -51, 170, 195, -106, 110, -141, -75, 98, 65], 'cord_len': 100}",
    # 
    # "wrong answeron test {'lamps': [-159, -274, -463, 312, 376, 262, -177, 
    # 478, -164, -26, -213, 396, -144, 264, -262, 306, -407, 467, -213, 125, 
    # -357, -376, -270, -294, 30, -149, 338, -180, -412, 239, 221, -104, -284,
    #  -246, 410, -277, -328, -99, 17, -113, 25, 495, 37, -346, 407, 122, 319,
    #  162, -184, 48], 'cells': [-441, 427, -325, 356, -428, 214, 494, 75, 340, 
    # 373, -127, -384, 180, -53, -305, -387, -71, 154, 4, 1, 127, 183, -489, -52, 
    # 248, 298, -423, -164, 153, 317, 54, 337, 203, 171, -116, 19, 286, -252, -48, 
    # 346, -35, -290, 41, -207, -430, -176, 193, -24, -131, -465, -259, -339, 337, 
    # 308, -26, 237, -190, -224, 397, -368, -446, 237, 10, -399, 397, -254, 451, 
    # 212, -386, -197, -440, -40, -496, 13, -30, -30, -359, 233, -301, -208, 203, 
    # 387, 232, -81, 246, -119, 440, -71, 359, 48, -227, 349, -318, -20, 248, 
    # 136, 488, -485, 353, -351], 'cord_len': 100}", 

