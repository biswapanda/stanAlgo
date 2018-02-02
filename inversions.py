import copy

def get_array():
   filepath = "/Users/bis/Desktop/inversion.txt"
   with open(filepath) as f:
      return [int(x) for x in f if x.strip()]


def print_function_name(f):
   def foo(*a, **kw):
      b = copy.deepcopy(a)
      ret = f(*a, **kw)
      # print f.func_name, b, "ret=", ret
      return ret
   return foo


@print_function_name
def count_cross_inversion(A, B):
   if not A:
      return 0
   if not B:
      return 0
   inv = 0
   for _ in range(len(A) + len(B)):
      if not B or not A:
         break
      if A[0] < B[0]:
         A.remove(A[0])
      else:
         inv += len(A)
         B.remove(B[0])
   return inv


@print_function_name
def count_inversion(arr):
   if len(arr) in [0, 1]:
      return 0
   m = len(arr) / 2
   L = count_inversion(copy.deepcopy(arr[:m]))
   R = count_inversion(copy.deepcopy(arr[m:]))
   C = count_cross_inversion(sorted(arr[:m]), sorted(arr[m:]))
   return L + R + C


@print_function_name
def main():
   # print count_inversion([2, 1, 3, 4])
   # print count_inversion([4, 3, 2, 1])
   # print count_inversion([])
   # print count_inversion([4])
   # print count_inversion([1, 6, 2, 3, 5, 4])
   print count_inversion(get_array())

   print count_inversion([3, 6, 1, 5, 4, 2])
   # print count_cross_inversion([6], [])
   # print count_cross_inversion ([1, 3, 6], [2, 4, 5])

if __name__ == "__main__":
   main()