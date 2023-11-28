def test():
  "--- test function ---"
  param =[(86,),(75,),(14,),(5,),(41,),(35,),(30,),(89,),(84,),(53,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  a =[0 for i in range(n)]
  b =[0 for i in range(n)]
  a[0] = b[0] = 1
  for i in range(1, n):
    a[i] = a[i - 1] + b[i - 1]
    b[i] = a[i - 1]
  return a[n - 1] + b[n - 1]
"-----------------"
test()
