import sys

RES = None
TEST_DIR = "/home/bis/dev/stanford-algs/testCases/" \
           "course3/assignment1SchedulingAndMST/questions1And2"


def load_data():
    global RES
    L = []
    # with open(TEST_DIR + "/" + sys.argv[1].replace("input", "output")) as f:
    #   RES = [int(x) for x in f.read().strip().split()]
    count = None
    with open("/home/bis/Desktop/jobs.txt") as f:
    # with open(TEST_DIR + "/" + sys.argv[1]) as f:
        for line in f:
            if not line.strip():
                continue
            if count is None:
                count = line
                continue
            p = [int(x) for x in line.split(" ")]
            L.append(dict(w=p[0], l=p[1]))
    return L


def sort_A(w, l):
    return ((w - l), w)


def sort_B(w, l):
    return float(w) / float(l)


def compute_weighted_completion_times(L, sort_func):
    sorted_L = sorted(L,
                      key=lambda x: sort_func(x["w"], x["l"]),
                      reverse=True)
    c = 0
    wc = 0
    for x in sorted_L:
        c += x["l"]
        wc += x["w"] * c
    return wc


def main():
   L = load_data()
   a = compute_weighted_completion_times(L, sort_func=sort_A)
   b = compute_weighted_completion_times(L, sort_func=sort_B)
   # print RES[0] == a
   # print RES[1] == b
   print a, b
   print "-" * 100


if __name__ == "__main__":
    main()