def test():
  "--- test function ---"
  param =[(60,),(74,),(8,),(74,),(34,),(66,),(96,),(11,),(45,),(72,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(N):
  ans = 0
  for i in range(1, N + 1):
    for j in range(1, N + 1): ans += i // j
  return ans
"-----------------"
test()
