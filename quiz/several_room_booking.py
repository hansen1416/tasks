from typing import List, Tuple, Optional

def get_max_num_ok_slots(
    slot_begin_end_pairs: 'List[Tuple[str, str]]'
) -> int:
    num_ok_slots: int = 0
    last_end: 'Optional[str]' = None

    for begin, end in sorted(
        slot_begin_end_pairs,
        key=lambda pair: pair[1],
    ):
        if last_end is None or begin >= last_end:
            last_end = end
            num_ok_slots += 1

    return num_ok_slots


def solve(
    begin_end_pairs: 'List[Tuple[int, int]]',
    num_rooms: int,
) -> int:
    num_ok_slots: int = 0

    begin_end_pairs = sorted(
        begin_end_pairs,
        key=lambda pair: pair[1],
    )

    room_taken = set()

    for _ in range(num_rooms):
        last_end: 'Optional[str]' = None

        for i, (begin, end) in enumerate(begin_end_pairs):

            if i in room_taken:
                continue

            if last_end is None or begin >= last_end:
                last_end = end
                num_ok_slots += 1
                room_taken.add(i)

    print(room_taken)
    return num_ok_slots


if __name__ == "__main__":
    # begin_end_pairs = [(0, 10), (15, 25), (10, 25), (5, 30)]
    # num_rooms = 2

    # res = solve(begin_end_pairs, num_rooms)

    # print(res)

    begin_end_pairs = [[67, 73], [8, 10], [22, 24], [5, 15], [1, 2], [30, 44], 
    [59, 67], [16, 23], [88, 102], [45, 51], [32, 40], [100, 108], [57, 68], 
    [33, 35], [63, 76], [45, 46], [5, 11], [63, 73], [78, 80], [49, 51], 
    [6, 11], [44, 49], [64, 76], [1, 3], [62, 65], [10, 13], [39, 42], 
    [78, 88], [70, 79], [84, 88], [12, 23], [84, 95], [58, 59], [19, 30], 
    [51, 56], [45, 54], [6, 20], [91, 96], [49, 54], [36, 37], [65, 68], 
    [6, 20], [1, 10], [19, 33], [36, 49], [53, 60], [92, 106], [47, 56], 
    [47, 48], [33, 40]]
    num_rooms = 2

    res = solve(begin_end_pairs, num_rooms)

    print(res)

    #  "wrong answeron test {'begin_end_pairs': [[22, 31], [87, 100], [39, 47], [100, 106], [76, 79], [32, 37], [14, 16], [60, 67], [42, 52], [21, 26], [62, 76], [10, 21], [83, 96], [41, 43], [69, 73], [23, 37], [19, 28], [42, 56], [67, 74], [5, 8], [22, 35], [88, 97], [44, 55], [5, 19], [42, 49], [18, 30], [97, 111], [91, 92], [52, 64], [70, 78], [13, 20], [21, 31], [35, 44], [28, 34], [44, 53], [51, 58], [79, 83], [38, 40], [92, 105], [59, 69], [21, 23], [67, 77], [11, 25], [21, 31], [20, 26], [19, 30], [38, 41], [59, 71], [77, 79], [98, 104]], 'num_rooms': 4}", "wrong answeron test {'begin_end_pairs': [[22, 32], [31, 43], [66, 72], [28, 34], [36, 44], [79, 81], [36, 37], [70, 82], [100, 104], [25, 35], [8, 13], [60, 73], [57, 69], [11, 22], [96, 100], [34, 37], [56, 62], [23, 31], [18, 24], [65, 66], [23, 26], [25, 28], [97, 98], [47, 54], [45, 58], [94, 98], [74, 80], [91, 96], [71, 81], [83, 97], [100, 109], [71, 85], [39, 40], [17, 27], [16, 28], [57, 68], [19, 20], [3, 16], [14, 25], [28, 42], [65, 78], [88, 102], [62, 72], [66, 71], [28, 39], [16, 17], [77, 81], [58, 65], [54, 63], [44, 50]], 'num_rooms': 2}", "wrong answeron test {'begin_end_pairs': [[45, 58], [49, 51], [89, 95], [16, 28], [75, 87], [40, 41], [7, 21], [59, 66], [2, 5], [76, 89], [13, 26], [9, 15], [59, 63], [24, 29], [3, 5], [35, 47], [68, 80], [47, 51], [40, 46], [25, 30], [25, 29], [63, 68], [74, 83], [44, 45], [32, 46], [79, 81], [14, 19], [71, 74], [81, 90], [53, 63], [39, 50], [6, 20], [35, 38], [34, 47], [100, 112], [88, 96], [58, 65], [63, 65], [87, 99], [13, 22], [41, 45], [99, 107], [81, 89], [0, 10], [59, 71], [75, 89], [30, 35], [30, 36], [45, 56], [62, 70]], 'num_rooms': 3}", "wrong answeron test {'begin_end_pairs': [[100, 103], [69, 80], [31, 32], [98, 110], [67, 74], [77, 87], [57, 67], [47, 51], [44, 55], [1, 13], [37, 43], [89, 90], [82, 87], [0, 9], [73, 79], [34, 43], [76, 84], [59, 68], [73, 82], [72, 81], [12, 26], [82, 89], [85, 92], [3, 15], [15, 17], [71, 84], [57, 59], [7, 19], [88, 99], [2, 4], [38, 41], [100, 114], [24, 26], [71, 83], [69, 74], [80, 93], [10, 13], [39, 52], [33, 40], [59, 60], [13, 22], [22, 32], [37, 48], [62, 74], [74, 82], [81, 84], [73, 76], [30, 39], [86, 91], [86, 97]], 'num_rooms': 6}", "wrong answeron test {'begin_end_pairs': [[111, 114], [131, 138], [105, 111], [164, 168], [127, 136], [139, 141], [33, 48], [172, 189], [200, 211], [80, 86], [65, 76], [177, 187], [23, 37], [197, 215], [76, 83], [105, 107], [159, 179], [94, 114], [187, 188], [5, 12], [44, 53], [129, 140], [190, 201], [7, 9], [144, 162], [70, 71], [27, 34], [46, 47], [65, 68], [52, 58], [182, 188], [159, 178], [92, 101], [68, 74], [72, 84], [62, 74], [16, 32], [182, 200], [25, 36], [165, 170], [95, 107], [76, 96], [147, 151], [10, 14], [120, 130], [141, 143], [140, 148], [168, 187], [192, 205], [138, 152], [151, 165], [30, 46], [40, 44], [29, 45], [14, 28], [25, 34], [15, 18], [162, 176], [162, 177], [147, 159], [24, 36], [38, 49], [50, 55], [153, 160], [164, 172], [106, 110], [144, 161], [84, 85], [28, 46], [162, 176], [153, 170], [35, 42], [116, 129], [73, 90], [78, 92], [85, 99], [200, 218], [122, 126], [76, 95], [24, 27], [156, 163], [23, 39], [55, 69], [26, 35], [69, 81], [136, 155], [23, 24], [128, 144], [126, 131], [18, 36], [18, 36], [97, 103], 
    # [102, 109], [14, 23], [166, 183], [83, 94], [3, 11], [105, 106], [33, 43], [95, 100]], 'num_rooms': 9}", "wrong answeron test {'begin_end_pairs': [[53, 54], [86, 95], [141, 143], [190, 205], [10, 11], [185, 194], [67, 80], [9, 23], [87, 92], [175, 190], [41, 43], [12, 28], [103, 111], [19, 38], [84, 92], [21, 30], [96, 111], [183, 195], [69, 79], [136, 146], [25, 28], [183, 189], [105, 113], [197, 199], [163, 166], [165, 168], [188, 204], [166, 168], [168, 182], [16, 26], [126, 140], [91, 96], [154, 168], [145, 151], [99, 104], [70, 82], [112, 124], [141, 156], [77, 89], [95, 104], [58, 62], [23, 41], [119, 125], [3, 9], [49, 69], [60, 61], [158, 166], [11, 17], [15, 24], [92, 112], [59, 71], [65, 85], [42, 50], [137, 142], [128, 136], [26, 32], [116, 134], [156, 164], [189, 198], [62, 69], [28, 48], [7, 13], [86, 89], [1, 14], [25, 39], [57, 68], [77, 93], [192, 204], [99, 100], [187, 198], [83, 91], [197, 205], [139, 155], [134, 152], [10, 12], [81, 88], [64, 77], [22, 39], [115, 128], [79, 80], [163, 164], [85, 104], [181, 195], [155, 159], [97, 109], [122, 140], [181, 196], [97, 105], [191, 196], [129, 141], [144, 149], [179, 192], [167, 182], [143, 163], [134, 151], [48, 65], [112, 132], [141, 151], [149, 169], [7, 9]], 'num_rooms': 2}", "wrong answeron test {'begin_end_pairs': [[107, 120], [69, 80], [176, 183], [62, 72], [140, 157], [192, 199], [168, 183], [36, 55], [53, 66], [61, 75], [151, 159], [123, 142], [153, 163], [180, 190], [156, 176], [170, 173], [65, 75], [103, 111], [122, 141], [84, 88], [88, 104], [70, 84], [13, 19], [90, 106], [61, 70], [127, 129], [160, 164], [29, 43], [128, 144], [148, 162], [55, 72], [116, 121], [171, 182], [164, 166], [80, 91], [33, 38], [28, 42], [83, 99], [21, 31], [22, 32], [149, 166], [84, 104], [153, 163], [32, 40], [75, 76], [36, 50], [156, 166], [188, 192], [140, 147], [170, 185], [197, 213], [104, 121], [95, 112], [24, 37], [31, 34], [136, 145], [45, 52], [192, 203], [75, 81], [112, 132], [190, 203], [38, 40], [152, 169], [28, 43], [75, 79], [168, 177], [189, 196], [87, 99], [47, 60], [183, 197], [191, 195], [185, 195], [69, 80], [114, 115], [31, 36], [18, 38], [52, 71], [160, 178], [195, 209], [6, 15], [176, 186], [8, 28], [163, 167], [87, 104], [65, 81], [40, 55], [126, 133], [167, 185], [172, 183], [159, 175], [133, 134], [198, 200], [147, 153], [78, 79], [117, 134], [200, 215], [169, 176], [98, 100], [121, 122], [22, 34]], 'num_rooms': 4}", "wrong answeron test {'begin_end_pairs': [[103, 109], [4, 23], [63, 83], [121, 132], [27, 34], [148, 160], [67, 76], [115, 125], [47, 57], [92, 97], [162, 180], [176, 187], [158, 166], [125, 130], [109, 119], [144, 154], [5, 6], [126, 143], [114, 118], [100, 105], [140, 148], [0, 5], [154, 170], [196, 202], [178, 186], [8, 28], [28, 34], [67, 78], [128, 146], [22, 28], [83, 84], [48, 63], [72, 86], [191, 207], [51, 71], [85, 103], [108, 117], [198, 209], [190, 207], [197, 199], [59, 62], [27, 33], [70, 78], [165, 177], [41, 49], [66, 81], [181, 193], [55, 72], [107, 120], [22, 37], [71, 77], [91, 108], [98, 110], [28, 46], [174, 176], [176, 181], [185, 197], [113, 133], [82, 95], [43, 48], [159, 168], [36, 43], [190, 198], [148, 157], [154, 166], [0, 10], [140, 150], [194, 195], [182, 184], [16, 23], [117, 127], [81, 99], [81, 97], [85, 97], [58, 63], [110, 121], [146, 158], [93, 105], [78, 83], [127, 137], [5, 14], [151, 154], [7, 20], [197, 217], [35, 38], [102, 111], [136, 150], [55, 59], [132, 146], [141, 145], [57, 75], [145, 151], [71, 74], [155, 158], [1, 14], [132, 143], [58, 73], [90, 99], [55, 58], [168, 178]], 'num_rooms': 6}", "wrong answeron test {'begin_end_pairs': [[53, 65], [109, 112], [157, 172], [180, 191], [80, 95], [101, 103], [33, 49], [13, 30], [166, 181], [56, 63], [125, 127], [104, 108], [110, 114], [168, 183], [150, 156], [118, 126], [50, 57], [151, 168], [87, 97], [139, 147], [16, 29], [126, 131], [182, 186], [92, 105], [194, 211], [81, 97], [190, 205], [96, 111], [52, 67], [199, 216], [106, 114], [11, 31], [104, 115], [194, 204], [8, 20], [39, 47], [136, 151], [13, 28], [152, 171], [40, 48], [59, 74], [111, 120], [164, 175], [169, 172], [187, 205], [46, 52], [55, 66], [87, 107], [184, 187], [109, 111], [189, 205], [187, 189], [9, 19], [175, 179], [0, 3], [132, 151], [34, 41], [51, 70], [28, 32], [57, 75], [151, 166], [132, 152], [153, 155], [148, 155], [68, 84], [89, 106], [141, 147], [127, 140], [27, 42], [164, 173], [184, 195], [68, 81], [132, 143], [98, 111], [189, 192], [155, 162], [72, 86], [175, 189], [193, 202], [151, 154], [136, 149], [138, 157], [183, 196], [73, 77], [89, 101], [43, 51], [84, 93], [30, 41], [35, 46], [28, 33], [9, 12], [27, 46], [73, 78], [33, 51], [178, 194], [74, 92], [60, 71], [41, 46], [144, 162], [48, 59]], 'num_rooms': 7}", "wrong answeron test {'begin_end_pairs': [[470, 497], [1229, 1276], [602, 662], [387, 403], [345, 385], [51, 108], [584, 587], [583, 612], [84, 104], [1009, 1058], [505, 562], [1870, 1873], [71, 107], [1785, 1805], [927, 978], [16, 72], [1127, 1140], [289, 340], [1807, 1865], [1561, 1564], [1073, 1094], [74, 117], [874, 904], [916, 937], [1141, 1196], [1557, 1618], [1185, 1232], [1180, 1200], [1782, 1810], [1154, 1159], [829, 858], [308, 322], [1010, 1052], [592, 627], [1812, 1845], [243, 301], [1552, 1605], [1410, 1448], [123, 181], [210, 247], [384, 390], [1860, 1884], [372, 375], [692, 695], [487, 504], [1871, 1911], [1128, 1180], [987, 1048], [1983, 2038], [456, 462], [316, 327], [71, 118], [1705, 1765], [1289, 1350], [977, 1008], [1459, 1515], [867, 868], [389, 418], [1630, 1661], [1, 6], [300, 308], [1448, 1458], [798, 833], [470, 483], [1469, 1489], [1485, 1492], [1063, 1076], [751, 798], [879, 923], [863, 907], [446, 447], [1665, 1666], [720, 729], [871, 888], [953, 993], [1768, 1797], [1817, 1871], [1379, 1398], [206, 252], [4, 55], [386, 439], [1151, 1187], [1004, 1013], [1258, 1302], [861, 897], [1597, 1622], [1215, 1232], [235, 236], [802, 816], [1169, 1229], [1019, 1072], [1621, 1655], [950, 981], [1022, 1063], [1973, 2004], [392, 398], [812, 840], [1961, 2001], [1048, 1079], [274, 298], [1920, 1961], [1529, 1553], [1789, 1846], [277, 329]]