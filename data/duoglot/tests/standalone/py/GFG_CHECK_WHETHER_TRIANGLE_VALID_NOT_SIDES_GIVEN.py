def test():
  "--- test function ---"
  param =[(29, 19, 52,),(83, 34, 49,),(48, 14, 65,),(59, 12, 94,),(56, 39, 22,),(68, 85, 9,),(63, 36, 41,),(95, 34, 37,),(2, 90, 27,),(11, 16, 1,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(a, b, c):
  if(a + b <= c)or(a + c <= b)or(b + c <= a): return False
  else: return True
"-----------------"
test()
