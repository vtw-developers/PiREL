def test():
  "--- test function ---"
  param =[(62,),(44,),(37,),(81,),(14,),(20,),(76,),(72,),(96,),(52,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  result = 0
  for i in range(n + 1):
    for j in range(n + 1):
      for k in range(n + 1):
        if i + j + k == n: result += 1
  return result
"-----------------"
test()
