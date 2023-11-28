def test():
  "--- test function ---"
  param =[(46, 89,),(26, 82,),(40, 12,),(58, 4,),(25, 44,),(2, 87,),(8, 65,),(21, 87,),(82, 10,),(17, 61,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(a, b):
  if a == 0: return b
  return f_gold(b % a, a)
"-----------------"
test()
