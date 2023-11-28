def test():
  "--- test function ---"
  param =[(67,),(48,),(59,),(22,),(14,),(66,),(1,),(75,),(58,),(78,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  maxvalue = 0
  i = 1
  for i in range(s - 1):
    j = 1
    for j in range(s):
      k = s - i - j
      maxvalue = max(maxvalue, i * j * k)
  return maxvalue
"-----------------"
test()
