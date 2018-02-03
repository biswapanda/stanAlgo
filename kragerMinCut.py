import copy
import random
import pprint
import time
import sys

ID = 1000
TEST_DIR = "/Users/bis/dev/stanford-algs/testCases/course1/assignment4MinCut"
RES = None


def get_next_id():
   global ID
   ID += 1
   return ID


def load_graph():
   G = {}
   global RES
   # with open(TEST_DIR + "/" + sys.argv[1].replace("input", "output")) as f:
   #   RES = int(f.read().strip())
   # with open(TEST_DIR + "/" + sys.argv[1]) as f:
   with open("/Users/bis/Desktop/krager.txt") as f:
      for line in f:
         if not line.strip():
            continue
         vertices = [int(x) for x in line.strip().split()]
         G[vertices[0]] = vertices[1:]
   return G


def get_edges(G):
   edges = []
   for u, v_list in G.items():
      for v in v_list:
         edges.append((u, v))
   return edges


def min_cut(G):
   random.seed(time.time())
   edges = get_edges(G)
   while len(set(edges)) > 2:
      edge = random.choice(edges)
      u, v = edge
      s = get_next_id()
      edges2 = []
      for e in edges:
         if e in [(u, v), (v, u)]:
            continue
         u1, v1 = e
         if u1 in {u, v}:
            edges2.append((s, v1))
            continue
         if v1 in {u, v}:
            edges2.append((u1, s))
            continue
         edges2.append(e)
      edges = edges2
   return len(edges) / 2


def main():
   G = load_graph()
   for k, v in G.items():
      assert len(set(v)) == len(v), "%s %s" % (k, sorted(v))
      assert k not in v
   min_cuts = []
   for _ in range(100):
      min_cuts.append(min_cut(G))
      print min(min_cuts), RES
      if min(min_cuts) == RES:
         break


if __name__ == "__main__":
   print sys.argv
   main()
