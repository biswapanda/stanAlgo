import time
import heapq
import os
import sys


def input_data_path():
   return "/home/bis/Desktop/huffman.txt"
   # TEST_DIR = "/home/bis/dev/stanford-algs/" \
   #            "testCases/course3/assignment3HuffmanAndMWIS/question1And2/"
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


class TreeNode(object):

  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val

  def __repr__(self):
    return "<V=%s L:%s R:%s>" % (self.val, self.left, self.right)


def depth(T, op):
  if T is None:
    return 0
  return 1 + op(depth(T.left, op),
                depth(T.right, op))


def huffman_coding(V, debug=False):
  L = [(x, TreeNode(x)) for x in V]
  heapq.heapify(L)
  while len(L) != 1:
    _, u = heapq.heappop(L)
    _, v = heapq.heappop(L)
    n = TreeNode(u.val + v.val)
    n.left = u
    n.right = v
    heapq.heappush(L, (n.val, n))
  if debug:
    print L
  max_code_len = depth(L[0][1], op=max) - 1
  min_code_len = depth(L[0][1], op=min) - 1
  return min_code_len, max_code_len


def rec_sum(L):
   if isinstance(L, int):
      return L
   elif isinstance(L, list):
      return sum(rec_sum(x) for x in L)
   else:
      raise "L=%s, type(L)=%s" % (L, type(L))


def main():
   V = load_data()
   min_code_len, max_code_len = huffman_coding(V)
   actual = [max_code_len, min_code_len]
   print actual
   # expected = open(input_data_path().replace("in", "out")).read().strip().split()
   # expected = [int(x) for x in expected]
   # if  actual == expected:
   #    return
   # print "-" * 100
   # print "actual =", actual
   # print "expected =", expected
   # huffman_coding(V, debug=True)
   # print "-" * 100


if __name__ == "__main__":
   main()
