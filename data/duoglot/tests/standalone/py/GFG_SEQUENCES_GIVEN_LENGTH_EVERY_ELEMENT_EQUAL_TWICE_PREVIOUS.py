def test():
  "--- test function ---"
  param =[(38, 34,),(39, 29,),(24, 99,),(90, 23,),(44, 2,),(49, 70,),(58, 84,),(97, 34,),(99, 72,),(19, 67,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(m, n):
  if m < n: return 0
  if n == 0: return 1
  res =(f_gold(m - 1, n)+ f_gold(m // 2, n - 1))
  return res
"-----------------"
test()
