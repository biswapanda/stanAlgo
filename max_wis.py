import time
import os
import sys


def input_data_path():
  return "/Users/bis/Desktop/mwis.txt"
  # TEST_DIR = "/Users/bis/dev/stanford-algs/" \
  #            "testCases/course3/assignment3HuffmanAndMWIS/question3"
  # return os.path.join(TEST_DIR, sys.argv[1])


def load_data():
  n, V = None, []
  with open(input_data_path()) as f:
    for line in f:
      line = line.strip()
      if not line:
        continue
      if n is None:
        n = int(line)
        continue
      V.append(int(line))
  assert n == len(V)
  return V


def max_wis(V):
  A = {-2: 0, -1: 0, 0: 0}
  S = set()
  for i, w in enumerate(V):
    v = max(A[i-1], w + A[i-2])
    A[i] = v
  i = len(V) - 1
  while i >= 0:
    if A[i - 1] >= A[i-2] + V[i]:
      i = i - 1
    else:
      S.add(1 + i)
      i = i - 2
  return A, S


def main():
  V = load_data()
  A, S = max_wis(V)
  actual = ''.join(str(int(x in S)) for x in [1, 2, 3, 4, 17, 117, 517, 997])
  print actual
  return
  expected = open(input_data_path().replace("in", "out")).read().strip()
  if actual == expected:
    return
  print "-" * 100
  print A
  print S
  print "actual =", actual
  print "expected =", expected
  print "-" * 100


if __name__ == "__main__":
  main()