import os
import copy
import random
import pprint
import time
import sys
import resource
import heapq

TEST_DIR = "/Users/bis/dev/stanford-algs/testCases/course2/assignment2Dijkstra"
RES = None

P = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]


def load_graph():
   # u v1,w1 v2,w2
   global RES
   # with open(TEST_DIR + "/" + sys.argv[1].replace("input", "output")) as f:
   #   RES = f.read().strip()
   G = {}
   # with open(TEST_DIR + "/" + sys.argv[1]) as f:
   with open("/Users/bis/stanford_algo/week2_dijkstra/dijkstra_data.txt") as f:
      for idx, line in enumerate(f):
         if not line.strip():
            continue
         L = [x.strip() for x in line.strip().split("\t") if x.strip()]
         G[int(L[0])] = [map(int, x.split(",")) for x in L[1:]]
   assert G.keys() == range(1, 201), set(G.keys()) ^ set(range(1, 201))
   return G


def shortest_path(G, S):
   H = []
   heapq.heappush(H, (0, 1))
   while H:
      # print H
      # print set(G) - set(S)
      # print
      d, u = heapq.heappop(H)
      if u in S and d >= S[u]:
         continue
      S[u] = d
      for v, w in G[u]:
         if v not in S or S[v] > d + w:
            heapq.heappush(H, (d+w, v))


def main():
   G = load_graph()
   S = {}
   shortest_path(G, S)
   print ",".join(str(S[x]) for x in P), RES


if __name__ == "__main__":
   main()