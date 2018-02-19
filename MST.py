import sys

TEST_DIR = "/home/bis/dev/stanford-algs/testCases/" \
           "course3/assignment1SchedulingAndMST/question3"
RES = None



def load_graph():
   G = {}
   global RES
   # filepath = TEST_DIR + "/" + sys.argv[1]
   filepath = "/home/bis/Desktop/edges.txt"
   # with open(filepath.replace("input", "output")) as f:
   #   RES = int(f.read().strip())
   V, E = None, None
   with open(filepath) as f:
      for line in f:
         if not line.strip():
            continue
         if V is None:
            V, E = [int(x) for x in line.strip().split()]
            continue
         u, v, w = [int(x) for x in line.strip().split()]
         G.setdefault(u, []).append((v, w))
         G.setdefault(v, []).append((u, w))
   return V, E, G


def find_mst(V, E, G):
   X = {1}
   cost = 0
   while X != set(range(1, 1 + V)):
      L = []
      for u in X:
         for v, w in G[u]:
            if v in X:
               continue
            L.append((w, v))
      w_min, v_min = sorted(L, key=lambda x:x[0])[0]
      cost += w_min
      X.add(v_min)
   return cost


def main():
   V,E,G = load_graph()
   cost = find_mst(V, E, G)
   print cost
   # print RES, cost, RES == cost


if __name__ == "__main__":
   main()