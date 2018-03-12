import os, sys

TEST_DIR = "/home/bis/dev/stanford-algs/testCases/course4/assignment1AllPairsShortestPath"
TEST_DIR = "/home/bis/Desktop"


def input_filename():
    return os.path.join(TEST_DIR, sys.argv[1])


def load_data():
    V = None
    E = None
    edges = []
    with open(input_filename()) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if V is None:
                V, E = [int(x) for x in line.strip().split()]
                continue
            edges.append([int(x) for x in line.split()])
    return V, E, edges


def apap(V, edges):
    inf = sys.maxint
    E = {}
    for u, v, w in edges:
        vv = E.get((u, v), 0)
        vv += w
        E[u, v] = vv
    A = {}
    V = range(1, V + 1)
    N = len(V)
    for i in V:
        for j in V:
            if (i, j) in E:
                v = E[i, j]
            elif i == j:
                v = 0
            else:
                v = inf
            A[i, j, 0] = v
    for k in V:
        for i in V:
            for j in V:
                A[i, j, k] = min([A[i, j, k - 1],
                                  A[i, k, k - 1] + A[k, j, k - 1]])
        if k == N:
            if A[i, i, N] < 0:
                print "null"
                sys.exit(0)
    print "min=", min([A[i, j, N] for i in V for j in V])


def main():
    V, E, edges = load_data()
    apap(V, edges)


if __name__ == "__main__":
    main()