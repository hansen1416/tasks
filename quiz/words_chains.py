from typing import List
from heapq import heappop, heappush


def words_diff(word1, word2):
    """
    all words are of the same length
    """
    diff = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff += 1

    return diff


def solve(
    all_words: List[str],
    begin_word: str,
    end_word: str,
) -> int:

    if begin_word not in all_words:
        all_words.append(begin_word)

    if end_word not in all_words:
        all_words.append(end_word)

    n = len(all_words)
    adj_matrix = [[float('inf')] * n for _ in range(n)]

    for i, w1 in enumerate(all_words):
        if w1 == begin_word:
            src_node = i

        if w1 == end_word:
            dst_node = i

        for j, w2 in enumerate(all_words):
            adj_matrix[i][j] = words_diff(w1, w2)

    # graph, n = adj_matrix, len(adj_matrix)
    # HINT: use a parent array to store a parent for each vertice
    heap, path = [], []
    used = [False for i in range(n)]

    # YOUR CODE GOES HERE
    distance = [float("inf") for i in range(n)]
    parent = [-1] * n

    heappush(heap, (0, src_node))
    distance[src_node] = 0
    parent[src_node] = src_node

    while len(heap) > 0:
        d, v = heappop(heap)
        used[v] = True

        if distance[v] < d:
            continue

        for u in range(n):
            if not used[u] and adj_matrix[v][u] != float('inf') and distance[u] > (d + adj_matrix[v][u]):
                distance[u] = d + adj_matrix[v][u]
                heappush(heap, (distance[u], u))
                parent[u] = v

    if distance[dst_node] == float('inf'):
        return -1

    path.append(dst_node)

    while dst_node != src_node:
        path.append(parent[dst_node])
        dst_node = parent[dst_node]

    score = 0
    prev_word = None

    for p in path[::-1]:
        if prev_word is not None:
            score += words_diff(prev_word, all_words[p]) ** 2

        prev_word = all_words[p]

    return score #, path[::-1]

if __name__ == "__main__":
    # all_words = ['vice', 'noon', 'mick', 'hear']
    # begin_word = 'kick'
    # end_word = 'nice'

    # res = solve(all_words, begin_word, end_word)

    # print(res)

    all_words = ['wk', 'lj', 'dw', 'ax', 'wr', 'bj', 'fg', 'hn', 'eo', 'er', 
    'fr', 'ie', 'pj', 'gr', 'wp', 'kt', 'is', 'zq', 'qt', 'qv', 'si', 'ry', 'do', 
    'pj', 'dd', 'sy', 'yk', 'xg', 'sw', 'eb', 'my', 'kv', 'ea', 'oz', 'hg', 'mw', 
    've', 'nj', 'tu', 'ci', 'lr', 'vw', 'vk', 'oy', 'fm', 'wa', 'be', 'ws', 'pe', 
    'kg', 'lh', 'la', 'eo', 'mw', 'ys', 'gj', 'gp', 'wc', 'ex', 'vn', 'jy', 'gc', 
    'kc', 'wh', 'pt', 'sv', 'ef', 'zk', 'og', 'tt', 'kb', 'hu', 'kv', 'bw', 'jp', 
    'pp', 'tm', 'bb', 'qy', 'es', 'mp', 'nv', 'rt', 'qh', 'qf', 'wu', 'vz', 'fe', 
    'sm', 'kr', 'xc', 'gn', 'rw', 'ch', 'sd', 'sl', 'rl', 'ag', 'cd', 'kj', 'dd', 
    'vx', 'ft', 'il', 'po', 'mk', 'ct', 'vu', 'cl', 'vq', 'xu', 'fz', 'er', 'jw', 
    'ha', 'ub', 'ra', 'bu', 'qi', 'wx', 'yp', 'zp', 'pt', 'gb', 'fk', 'rk', 'le', 
    'fv', 'ft', 'rg', 'id', 'px', 'ts', 'bw', 'zb', 'mz', 'pp', 'yw', 'dc', 'pu', 
    'yy', 'zc', 'vl', 'zh', 'bn', 'mv', 'ly', 'hn', 'bm', 'mt', 'dw', 'cg', 'ss', 
    'ol', 'oi', 'ry', 'ou', 'vr', 'qi', 'au', 'if', 'yu', 'cu', 'aa', 'xo', 'oo', 
    'pf', 'uk', 'ql', 'ts', 'ko', 'pb', 'cm', 'vf', 'nn', 'vi', 'vn', 'if', 'jx', 
    'uy', 'tr', 'kz', 'gx', 'hj', 'zz', 'in', 'vb', 'bc', 'cx', 'ui', 'lq', 'zb', 
    'ah', 'uq', 'cp', 'qf', 'sz', 'wu', 'ts', 'yo', 'ai', 'dd', 'lb', 'kg', 'ry', 
    'bc', 'xm', 'ds', 'ah', 'vi', 'lk', 'xc', 'pb', 'xw', 'ac', 'tl', 'gf', 'fj', 
    'wb', 'jz', 'md', 'km', 'yc', 'su', 'ls', 'cr', 'fg', 'rr', 'ph', 'il', 'pa', 
    'hh', 'lj', 'ud', 'nn', 'bj', 'ku', 'zr', 'ef', 'iv', 'lr', 'id', 'ud', 'pz', 
    'cg', 'mi', 'kj', 'jy', 'xh', 'lv', 'do', 'yh', 'vq', 'ca', 'ik', 'rf', 'px', 
    'fo', 'ek', 'wn', 'gy', 'nz', 'in', 'ko', 'jj', 'lc', 'jj', 'tk', 'vk', 'ok', 
    'cj', 'ri', 'wh', 'nw', 'xd', 'dw', 'is', 'uk', 'op', 'la', 'hn', 'cf', 'ap', 
    'us', 'wl', 'gb', 'sw', 'qp', 'yx', 'tx', 'yj', 'wk', 'xm', 'nj', 'sa', 'ei', 
    'on', 'sy', 'hx', 'wc', 'co', 'nf']
    begin_word = 'co'
    end_word = 'nf'

    res = solve(all_words, begin_word, end_word)

    print(res)

    all_words = ['gpi', 'gib', 'lwc', 'vop', 'gav', 'hdx', 'boz', 'xyc', 'djy', 
    'est', 'hdd', 'nir', 'imp', 'ezl', 'qsm', 'mwi', 'goc', 'zrf', 'zfy', 'cbi', 
    'mrl', 'boy', 'kul', 'rtn', 'tdo', 'pdr', 'mcp', 'ejn', 'bwc', 'xlh', 'xln', 
    'njp', 'tep', 'hhu', 'dqm', 'zha', 'nkm', 'ycc', 'ddd', 'hlq', 'ryd', 'iim', 
    'kmt', 'mjo', 'uzk', 'cwe', 'wqj', 'cyr', 'vuq', 'vgg', 'ybl', 'xia', 'bqi', 
    'num', 'pyh', 'job', 'mje', 'slk', 'uyt', 'mig', 'trj', 'ipq', 'hqq', 'kvm', 
    'vez', 'khi', 'gvi', 'wux', 'fvk', 'lvx', 'own', 'goo', 'agy', 'gtk', 'ofv', 
    'zwo', 'fws', 'rbf', 'knz', 'unl', 'hgp', 'vpl', 'yak', 'ztv', 'puj', 'ikh', 
    'xnt', 'fsy', 'qwm', 'yea', 'wmh', 'spf', 'urn', 'yvk', 'aoa', 'gjo', 'kce', 
    'hcg', 'mhv', 'dog', 'zii', 'xjo', 'xqa', 'mop', 'kgo', 'xdq', 'iyw', 'dww', 
    'khy', 'qum', 'gwf', 'bjj', 'qdm', 'hwq', 'koz', 'uxk', 'ozr', 'axq', 'wzh', 
    'ljn', 'cos', 'tca', 'tyb', 'wkn', 'bev', 'uup', 'yab', 'ist', 'bhj', 'qoi', 
    'ztr', 'joi', 'god', 'mjv', 'cxc', 'qxb', 'rqb', 'pph', 'wtw', 'dxa', 'lwd', 
    'qbb', 'xel', 'xyb', 'ixp', 'zlq', 'gil', 'cnm', 'qub', 'wsj', 'nvb', 'wnb', 
    'htj', 'tgx', 'xcw', 'pih', 'gfw', 'qjb', 'jsp', 'vfe', 'qdy', 'ene', 'rry', 
    'mjj', 'smv', 'wts', 'czg', 'wqw', 'for', 'kok', 'vpv', 'kpt', 'ium', 'udo', 
    'eet', 'usy', 'vni', 'hkl', 'nhs', 'qsd', 'ldi', 'gww', 'dwd', 'jfd', 'ssl', 
    'pui', 'qfp', 'det', 'vtf', 'vze', 'khw', 'onq', 'pdn', 'goy', 'sno', 'xsw', 
    'hts', 'ykh', 'mso', 'xec', 'jbh', 'pju', 'cxj', 'hpr', 'epi', 'wfy', 'iul', 
    'vtc', 'iqr', 'iky', 'ywt', 'nth', 'czr', 'rfz', 'jgt', 'oas', 'dvm', 'nmb', 
    'ulo', 'vaf', 'txq', 'tvl', 'dju', 'beb', 'mvm', 'iqy', 'hoj', 'xyr', 'mww', 
    'ywt', 'raz', 'iay', 'pms', 'kfy', 'rjf', 'gtm', 'wxg', 'imd', 'lgh', 'mro', 
    'mrl', 'nqr', 'ssu', 'pup', 'bdp', 'prl', 'wjr', 'esu', 'yvb', 'wub', 'hcs', 
    'uoh', 'tfk', 'ebx', 'ysg', 'pso', 'ozm', 'rga', 'yhd', 'yrp', 'rjf', 'ukj', 
    'gdy', 'fvk', 'dhy', 'hra', 'qtq', 'cmk', 'hvo', 'ico', 'wnj', 'jsu', 'dnk', 
    'ogi', 'chs', 'nik', 'zah', 'jpk', 'cyx', 'ghn', 'iwo', 'kzp', 'yru', 'nto', 
    'cen', 'zzr', 'aqp', 'piz', 'zqs', 'ngx', 'zhf', 'sgg', 'slx', 'yjj', 'kjo', 
    'edw', 'crn', 'msy', 'syh', 'aly', 'did', 'sxb']

    begin_word = 'did'
    end_word = 'sxb'

    res = solve(all_words, begin_word, end_word)

    print(res)