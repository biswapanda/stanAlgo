import time
import os
import sys
import threading

L = []
h = {}

def input_data_path():
  # return "2sum.txt"
  TEST_DIR = "/Users/bis/dev/stanford-algs/testCases/course2/assignment4TwoSum"
  return os.path.join(TEST_DIR, sys.argv[1])


def load_data():
  L = []
  with open(input_data_path()) as f:
    for line in f:
      line = line.strip()
      if not line:
        continue
      L.append(int(line))
  return L


def find_2_sum_count(i, t_set):
  # print "starting", threading.current_thread().getName()
  # for _ in range(i * 1):
  #   print "%s - %s" % (threading.current_thread().getName(), i)
  #   time.sleep(1)
  # print "done", threading.current_thread().getName()
  ll = len(L)/8
  for idx in range(i*ll, (i + 1)*ll):
    for t in range(-10000, 10001):
      x = L[idx]
      if t - x in h:
        t_set.add(t)
  # print "done", threading.current_thread().getName()


def main():
  global L
  global h
  L = load_data()
  h = {}
  for x in L:
    h[x] = True
  threads = []
  t_sets = []
  for i in range(8):
    t_sets.append(set())
    threads.append(threading.Thread(target=find_2_sum_count,
                                    args=(i, t_sets[i])))
                                    # args=(, h, t_sets[i])))
  [x.start() for x in threads]
  time.sleep(1)
  while [x.isAlive() for x in threads]:
    time.sleep(1)
    # print "len(threads) = ", len(threads)
    for x in threads:
      x.join()
      if not x.is_alive():
        threads.remove(x)
  # print "---- all threads have been killed"

  s = set()
  for t in t_sets:
    # print len(t)
    s.update(t)
  # print "ans=", len(s)
  with open(input_data_path().replace("input", "output")) as f:
    res = int(f.readline().strip())
  print "******", len(s) == res


if __name__ == "__main__":
  main()