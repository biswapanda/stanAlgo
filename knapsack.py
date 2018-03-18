import os
import sys

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

def optimal_value():
  V, W, n = load_data()
  A = {}
  for i in range(W +1):
    A[0, i] = 0
  for i in range(1, n + 1):
    for x in range(W + 1):
      vi, wi = V[i - 1]
      candidates = [A[i-1, x]]
      if x >= wi:
        candidates.append(A[i-1, x - wi] + vi)
      A[i, x] = max(candidates)
  return A[n, W]

def main():
  ret = optimal_value()
  p = input_data_path()
  if "input" in p:
    expected = int(open(p.replace("input", "output")).read())
    if expected != ret:
      print "expected=%s ret=%d" % (expected, ret)
    else:
      print "yay!"
  else:
    print "ret=", ret


if __name__ == "__main__":
  main()