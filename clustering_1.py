import os
import sys


TEST_DIR = "/home/bis/dev/stanford-algs/testCases/course3/assignment2Clustering/question1"


def input_filename():
    return "/home/bis/Desktop/clustering1.txt"
    return os.path.join(TEST_DIR, sys.argv[1])


def load_data():
    N = None
    C = {}
    with open(input_filename()) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if N is None:
                N = int(line)
                continue
            x = [int(y) for y in line.split()]
            C[tuple(sorted([x[0], x[1]]))] = x[2]
    assert len(C) == N * (N - 1) / 2
    return N, C


def max_spacing(E, clusters):
   import itertools
   s_set = set()
   for c1, c2 in itertools.combinations(clusters.keys(), 2):
       for x1 in clusters[c1]:
           for x2 in clusters[c2]:
               s = E[tuple(sorted([x1, x2]))]
               s_set.add(s)
   return min(s_set)


def main():
    N, E = load_data()
    E_sorted = sorted(E.items(), key=lambda x: x[1])
    L = {x: x for x in range(1, 1 + N)}
    T = set()
    for (u, v), w in E_sorted:
        # print u, v, w
        if L[u] == L[v]:
            continue
        # add edge to MST
        T.add((u, v))
        u_c = [x for x in L.itervalues() if x == u]
        v_c = [x for x in L.itervalues() if x == v]
        if len(u_c) > len(v_c):
            old_leader, new_leader = L[v], L[u]
        else:
            old_leader, new_leader = L[u], L[v]
        for key, val in L.items():
            if val == old_leader:
                L[key] = new_leader
        if len(set(L.values())) == 4:
            break
    clusters = {}
    for u, l in L.iteritems():
        clusters.setdefault(l, []).append(u)
    max_s = max_spacing(E, clusters)
    print max_s
    return
    with open(input_filename().replace("input", "output")) as f:
        res = int(f.readline().strip())
    print res == max_s
    if res!= max_s:
        print "max_s=%s expected=%s" % (max_s, res)


if __name__ == "__main__":
    main()
    # ANSWER = 106