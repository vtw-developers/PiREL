def test():
  "--- test function ---"
  param =[(17,),(72,),(43,),(55,),(62,),(22,),(17,),(68,),(20,),(29,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  k = n
  imin = 1
  ans = 0
  while(imin <= n):
    imax = n / k
    ans += k *(imax - imin + 1)
    imin = imax + 1
    k = n / imin
  return ans
"-----------------"
test()
