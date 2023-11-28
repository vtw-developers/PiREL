def test():
  "--- test function ---"
  param =[(6, 30,),(23, 87,),(89, 31,),(63, 36,),(23, 68,),(44, 66,),(81, 18,),(43, 73,),(9, 42,),(41, 98,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n, k):
  total = k
  mod = 1000000007
  same, diff = 0, k
  for i in range(2, n + 1):
    same = diff
    diff = total *(k - 1)
    diff = diff % mod
    total =(same + diff)% mod
  return total
"-----------------"
test()
