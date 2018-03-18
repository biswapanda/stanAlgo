import os
import sys

p = [.2, .05, .17, .1, .2, .03, .25]
p2 = [.05, .4, .08, .04, .1, .1, .23]
# 2.18


def get_a(A, i, j):
  if i > j:
    return 0
  return A[i, j]


def main(pp):
  N = len(pp)
  A = {}
  for x in range(1, N + 1):
    A[x, x] = pp[x - 1]
  for s in range(N):
    for i in range(1, N + 1):
      if i + s > N:
        continue
      p_sum = sum([pp[i - 1 + x] for x in range(s + 1)])
      A[i, i + s] = (p_sum +
                     min([get_a(A, i, r-1) + get_a(A, r+1, i+s)
                          for r in range(i, i + s +1)]))
  print A
  print A[1, N]


if __name__ == "__main__":
  main(p)
  print "-" * 10
  main(p2)