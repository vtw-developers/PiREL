def test():
  "--- test function ---"
  param =[(52,),(47,),(75,),(36,),(68,),(16,),(99,),(38,),(84,),(45,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  count = 0
  for i in range(0, n + 1):
    for j in range(0, n + 1):
      for k in range(0, n + 1):
        if(i + j + k == n): count = count + 1
  return count
"-----------------"
test()
