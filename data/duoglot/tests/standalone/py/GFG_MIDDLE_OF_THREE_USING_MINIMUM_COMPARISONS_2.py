def test():
  "--- test function ---"
  param =[(48, 46, 38,),(21, 7, 16,),(71, 4, 31,),(93, 34, 11,),(3, 61, 32,),(58, 78, 6,),(88, 41, 66,),(8, 84, 38,),(17, 66, 27,),(13, 3, 23,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(a, b, c):
  x = a - b
  y = b - c
  z = a - c
  if x * y > 0: return b
  elif(x * z > 0): return
  else: return a
"-----------------"
test()
