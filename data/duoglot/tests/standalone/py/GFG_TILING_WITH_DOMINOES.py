def test():
  "--- test function ---"
  param =[(29,),(13,),(25,),(65,),(27,),(42,),(19,),(50,),(59,),(13,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  A =[0] *(n + 1)
  B =[0] *(n + 1)
  A[0] = 1
  A[1] = 0
  B[0] = 0
  B[1] = 1
  for i in range(2, n + 1):
    A[i] = A[i - 2] + 2 * B[i - 1]
    B[i] = A[i - 1] + B[i - 2]
  return A[n]
"-----------------"
test()
