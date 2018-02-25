import time
import os
import sys
import threading

L = []
h = {}


def input_data_path():
  return "/Users/bis/dev/dev/pyplayground/2sum.txt"
  # TEST_DIR = "/Users/bis/dev/stanford-algs/testCases/course2/assignment4TwoSum"
  # return os.path.join(TEST_DIR, sys.argv[1])


def load_data():
  L = []
  with open(input_data_path()) as f:
    for line in f:
      line = line.strip()
      if not line:
        continue
      L.append(int(line))
  return L


def find_2_sum_count():
  s = time.time()
  t_set = set()
  t_rng = set(range(-10000, 10001))
  for i, x in enumerate(L):
    if i % 10000 == 0:
      print i, int(time.time() - s)
    t_rem = set()
    for t in t_rng:
      if t - x in h:
        t_set.add(t)
        t_rem.add(t)
    for x in t_rem:
      t_rng.remove(x)
  return len(t_set)


def main():
  global L
  global h
  L = load_data()
  h = {}
  for x in L:
    h[x] = True
  c = find_2_sum_count()
  print "res = ", c
  # with open(input_data_path().replace("input", "output")) as f:
  #   res = int(f.readline().strip())
  # print "******", c == res


if __name__ == "__main__":
  main()