def test():
  "--- test function ---"
  param =[(43, 24, 7,),(76, 54, 66,),(57, 5, 40,),(10, 13, 4,),(59, 47, 56,),(92, 14, 50,),(49, 62, 65,),(16, 95, 12,),(33, 41, 90,),(66, 63, 46,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(a, b, c):
  if a > b:
    if(b > c): return b
    elif(a > c): return c
    else: return a
  else:
    if(a > c): return a
    elif(b > c): return c
    else: return b
"-----------------"
test()
