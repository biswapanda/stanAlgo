import time
import os
import sys

TEST_DIR = "/home/bis/dev/stanford-algs/testCases/course3/assignment2Clustering/question2"


def input_filename():
    # return "/home/bis/Desktop/clustering1.txt"
    return os.path.join(TEST_DIR, sys.argv[1])


def load_data():
    N = None
    B = None
    V = []
    with open(input_filename()) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if N is None:
                N, B = [int(x) for x in line.strip().split()]
                continue
            V.append("".join(line.split()))
    return N, B, V


def max_spacing(E, clusters):
   import itertools
   s_set = set()
   for c1, c2 in itertools.combinations(clusters.keys(), 2):
       for x1 in clusters[c1]:
           for x2 in clusters[c2]:
               s = E[tuple(sorted([x1, x2]))]
               s_set.add(s)
   return min(s_set)


def get_masks(B):
    s = []
    for i in range(B):
        s.append((2**i, 1))
        for j in range(B):
            if i < j:
                s.append((2**i + 2**j, 2))
    return s


def main():
    st = time.time()
    N, B, V = load_data()
    V_int = [int(x, 2) for x in V]
    M = get_masks(B)
    edges = []
    V_int = list(set(V_int))
    s = set()
    for i, x in enumerate(V_int):
        if i % 10000 == 0:
            print i, "%.3f" % (time.time() - st)
        for m, w in M:
            e = sorted([x, x ^ m])
            e.append(w)
            e = tuple(e)
            if e in s:
                edges.append(e)
            else:
                s.add(e)
    edges = list(set(edges))
    E_sorted = sorted(edges, key=lambda x: x[2])
    e_len = len(edges)
    L = {x: x for x in V_int}
    for idx, (u, v, w) in enumerate(E_sorted):
        if L[u] == L[v]:
            continue
        if idx % 1000 == 0:
            print "E", idx, "%.3f seconds, %d %%" % \
                ((time.time() - st), 100.0 * idx / e_len)
        # add edge to MST
        uu, vv = [], []
        for key, val in L.iteritems():
            if val == L[u]:
                uu.append(key)
            if val == L[v]:
                vv.append(key)
        if len(uu) > len(vv):
            new_leader = L[u]
            change_leader = vv
        else:
            new_leader = L[v]
            change_leader = uu
        for x in change_leader:
           L[x] = new_leader
    result = len(set(L.values()))
    if "input_random_1000.txt" in input_filename():
        print "result =", result
        sys.exit(0)
    with open(input_filename().replace("input", "output")) as f:
        expected = int(f.readline().strip())
    if result != expected:
        print "result=%s expected=%s: %s" % (result, expected, input_filename())


if __name__ == "__main__":
    main()
