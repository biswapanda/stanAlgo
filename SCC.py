import copy
import random
import pprint
import time
import sys

sys.setrecursionlimit(150000)

V_COUNT = 875714
DEBUG = False # True

TEST_DIR = "/Users/bis/dev/stanford-algs/testCases/course2/assignment1SCC"
RES = None
first_pass = set()
second_pass = set()
current_node = None
t = 0
f = {}
scc = {}
v_set = set()


def load_graph():
   # global RES
   # with open(TEST_DIR + "/" + sys.argv[1].replace("input", "output")) as f:
   #   RES = f.read().strip()
   G = {}
   global v_set
   # with open(TEST_DIR + "/" + sys.argv[1]) as f:
   with open("/Users/bis/Desktop/scc.txt") as f:
      for idx, line in enumerate(f):
         if not line.strip():
            continue
         u, v = [int(x) for x in line.strip().split(" ")]
         G.setdefault(u, []).append(v)
         v_set.add(v)
         v_set.add(u)
   print "loaded graph"
   return G


def dfs_loop(G, vertices, explored_set, pass_count):
   global current_node
   for v in sorted(vertices, reverse=True):
     if v not in explored_set:
        current_node = v
        dfs(G, v, explored_set, pass_count)


def dfs(G, v, explored_set, pass_count):
   if v in explored_set:
      return
   explored_set.add(v)
   for u in G.get(v, []):
      dfs(G, u, explored_set, pass_count)
   if pass_count == 1:
      global t
      global f
      t += 1
      f[v] = t
      if DEBUG:
         print "f ->", v, t, explored_set
   if pass_count == 2:
      global scc
      scc.setdefault(current_node, []).append(v)


def invert_graph(G):
   G_inverse = {}
   for u in range(1, V_COUNT + 1):
      for v in G.get(u, []):
         G_inverse.setdefault(f[v], []).append(f[u])
   return G_inverse


def main():
   G = load_graph()
   if DEBUG:
      print "G ="
      pprint.pprint(G)
   dfs_loop(G, vertices=v_set,
            explored_set=first_pass,
            pass_count=1)
   if DEBUG:
      print f
   # assert set(f.items()) == set(range(1, 1 + V_COUNT))
   G_inverse = invert_graph(G)
   if DEBUG:
      print "G_inverse ="
      pprint.pprint(G_inverse)

   dfs_loop(G_inverse, vertices=range(1, 1 + t),
            explored_set=second_pass, pass_count=2)
   if DEBUG:
      print "scc="
   z = sorted([len(x) for x in scc.values()],
              reverse=True)[:5]
   if DEBUG:
      print z
   if len(z) < 5:
      z.extend([0] * (5 - len(z)))
   print ",".join([str(x) for x in z])
   # print RES


if __name__ == "__main__":
   main()
