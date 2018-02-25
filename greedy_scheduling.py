import sys

TEST_DIR = "/Users/bis/dev/stanford-algs/testCases/course3/assignment1SchedulingAndMST/questions1And2"
RES = None


def load_data():
   global RES
   input_file_path = TEST_DIR + "/" + sys.argv[1]
   with open(input_file_path.replace("input", "output")) as f:
     RES = f.read()
   L = []
   count = None
   with open(input_file_path) as f:
      for line in f:
         line = line.strip()
         if not line:
            continue
         if count is None:
            count = int(line)
            continue
         L.append([int(x) for x in line.split(" ")])
   return L


def main():
   L = load_data()
   print L


if __name__ == '__main__':
   main()