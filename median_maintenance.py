import sys
import heapq

TEST_DIR = "/Users/bis/dev/stanford-algs/testCases/course2/assignment3Median"
RES = None
RL = []
H_LOW = []
H_HIGH = []


def load_data():
   global RES
   input_file_path = "/Users/bis/dev/dev/pyplayground/Median.txt"
   # input_file_path = TEST_DIR + "/" + sys.argv[1]
   # with open(input_file_path.replace("input", "output")) as f:
   #   RES = f.read().strip()
   L = []
   with open(input_file_path) as f:
      for line in f:
         line = line.strip()
         if not line:
            continue
         L.append(int(line))
   return L


def get_median(e):
   global H_HIGH
   global H_LOW
   h_high_min, h_low_max = None, None
   if H_HIGH:
      h_high_min = H_HIGH[0][1]
   if H_LOW:
      h_low_max = H_LOW[0][1]
   if not H_LOW:
      heap_to_insert = H_LOW
   elif not H_HIGH:
      heap_to_insert = H_HIGH
   else:
      if h_low_max < e < h_high_min:
         heap_to_insert = H_LOW
      elif e < h_low_max:
         heap_to_insert = H_LOW
      else:
         heap_to_insert = H_HIGH
   heap_key = e * (-1 if heap_to_insert == H_LOW else 1)
   heapq.heappush(heap_to_insert, (heap_key, e))
   # balance heaps
   _maybe_balance_heaps(H_LOW, H_HIGH)
   count = len(H_HIGH) + len(H_LOW)
   if count % 2 == 0:
      median_idx = count / 2
   else:
      median_idx = (count + 1) / 2

   if median_idx == len(H_LOW):
      median = H_LOW[0][1]
   else:
      median = H_HIGH[0][1]
   # print e, H_LOW, H_HIGH, median
   return median


def _maybe_balance_heaps(h_low, h_high):
   if -1 < len(h_low) - len(h_high) < 1:
      return
   if len(h_low) < len(h_high):
      _, e = heapq.heappop(h_high)
      heapq.heappush(h_low, (-1 * e, e))
   else:
      _, e = heapq.heappop(h_low)
      heapq.heappush(h_high, (e, e))


def main():
   L = load_data()
   print L
   s = 0
   for x in L:
     s += get_median(x)
   print s%10000, RES


if __name__ == "__main__":
   main()