def test():
  "--- test function ---"
  param =[(19, 14, 34,),(23, 51, 5,),(92, 10, 24,),(9, 50, 34,),(20, 67, 20,),(68, 25, 40,),(66, 30, 24,),(77, 22, 32,),(90, 1, 71,),(26, 34, 54,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n, m, k):
  if(m <= n - k + 1): return m + k - 1
  m = m -(n - k + 1)
  if(m % n == 0): return n
  else: return m % n
"-----------------"
test()
