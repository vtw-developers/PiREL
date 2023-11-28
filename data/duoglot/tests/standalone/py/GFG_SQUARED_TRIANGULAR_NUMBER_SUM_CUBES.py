def test():
  "--- test function ---"
  param =[(15,),(36,),(39,),(43,),(75,),(49,),(56,),(14,),(62,),(97,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  _sum = 0
  n = 1
  while(_sum < s):
    _sum += n * n * n
    n += 1
  n -= 1
  if _sum == s: return n
  return - 1
"-----------------"
test()
