def test():
  "--- test function ---"
  param =[(37, 80,),(10000000000, - 10000000000,),(10000000000, 10000000000,),(999999999, 999999999,),(39, 36,),(92, 56,),(14, 21,),(19, 38,),(14, 82,),(88, 41,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(a, b):
  if(a == 0 or b == 0): return False
  result = a * b
  if(result >= 9223372036854775807 or result <= - 9223372036854775808): result = 0
  if(a ==(result // b)):
    print(result // b)
    return False
  else: return True
"-----------------"
test()
