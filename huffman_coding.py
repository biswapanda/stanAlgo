import time
import os
import sys


def input_data_path():
   # return "/Users/bis/Desktop/mwis.txt"
   TEST_DIR = "/Users/bis/dev/stanford-algs/" \
              "testCases/course3/assignment3HuffmanAndMWIS/question1And2/"
   return os.path.join(TEST_DIR, sys.argv[1])


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


def huffman_coding(V):
  pass


def rec_sum(L):
   if isinstance(L, int):
      return L
   elif isinstance(L, list):
      return sum(rec_sum(x) for x in L)
   else:
      raise "L=%s, type(L)=%s" % (L, type(L))


def main():
   V = load_data()
   encoding = huffman_coding(V)
   # actual = ''.join(str(int(x in S)) for x in [1, 2, 3, 4, 17, 117, 517, 997])
   # print actual
   # return
   # expected = open(input_data_path().replace("in", "out")).read().strip()
   # if actual == expected:
   #    return
   # print "-" * 100
   # print A
   # print S
   # print "actual =", actual
   # print "expected =", expected
   # print "-" * 100


if __name__ == "__main__":
   main()
