import os
import sys

sys.setrecursionlimit(2000000)

def input_data_path():
  d = "/Users/bis/dev/stanford-algs/testCases/" \
      "course3/assignment4Knapsack"
  return os.path.join(d, sys.argv[1])

def load_data():
  k, n = None, None
  V = []
  with open(input_data_path()) as f:
    for line in f:
      line = line.strip()
      if not line:
        continue
      if n is None:
        k, n = [int(x) for x in line.strip().split(" ")]
        continue
      v, w = [int(x) for x in line.strip().split(" ")]
      V.append((v, w))
  assert len(V) == n
  return V, k, n

A = {}

def optimal_value(V, i, w):
  if i == 0 or i == 1:
    return 0
  global A
  if (i, w) in A:
    return A[i, w]
  vi, wi = V[i - 1]
  candidates = [optimal_value(V, i-1, w)]
  if w >= wi:
    candidates.append(optimal_value(V, i-1, w - wi) + vi)
  ret = max(candidates)
  A[i, w] = ret
  return ret

def main():
  V, W, n = load_data()
  ret = optimal_value(V, n, W)
  p = input_data_path()
  if "input" not in p:
    print "ret=", ret
    return
  expected = int(open(p.replace("input", "output")).read())
  if expected != ret:
    print A
    print "expected=%s ret=%d" % (expected, ret)

if __name__ == "__main__":
  main()