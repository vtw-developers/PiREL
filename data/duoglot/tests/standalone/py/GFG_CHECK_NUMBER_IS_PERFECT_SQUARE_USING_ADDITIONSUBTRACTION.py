def test():
  "--- test function ---"
  param =[(1,),(4,),(9,),(25,),(36,),(3,),(121,),(14,),(17,),(80,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  i = 1
  the_sum = 0
  while the_sum < n:
    the_sum += i
    if the_sum == n: return True
    i += 2
  return False
"-----------------"
test()
