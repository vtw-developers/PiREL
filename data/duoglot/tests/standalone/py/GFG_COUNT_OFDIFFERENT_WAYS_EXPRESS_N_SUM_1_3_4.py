def test():
  "--- test function ---"
  param =[(44,),(9,),(19,),(10,),(78,),(94,),(70,),(81,),(81,),(49,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  DP =[0 for i in range(0, n + 1)]
  DP[0] = DP[1] = DP[2] = 1
  DP[3] = 2
  for i in range(4, n + 1): DP[i] = DP[i - 1] + DP[i - 3] + DP[i - 4]
  return DP[n]
"-----------------"
test()
