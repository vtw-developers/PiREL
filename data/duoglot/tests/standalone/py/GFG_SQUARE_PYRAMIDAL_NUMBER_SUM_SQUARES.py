def test():
  "--- test function ---"
  param =[(1,),(5,),(14,),(140,),(204,),(3,),(506,),(42,),(4,),(87,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  _sum = 0
  n = 1
  while(_sum < s):
    _sum += n * n
    n += 1
  n -= 1
  if _sum == s: return n
  return - 1
"-----------------"
test()
