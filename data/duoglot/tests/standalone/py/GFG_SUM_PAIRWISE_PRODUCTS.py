def test():
  "--- test function ---"
  param =[(21,),(32,),(16,),(38,),(9,),(3,),(5,),(46,),(45,),(87,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  sm = 0
  for i in range(1, n + 1):
    for j in range(i, n + 1): sm = sm + i * j
  return sm
"-----------------"
test()
