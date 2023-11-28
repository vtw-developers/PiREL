def test():
  "--- test function ---"
  param =[(67,),(89,),(12,),(94,),(96,),(25,),(49,),(8,),(33,),(59,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(limit):
  if(limit < 2): return 0
  ef1 = 0
  ef2 = 2
  sm = ef1 + ef2
  while(ef2 <= limit):
    ef3 = 4 * ef2 + ef1
    if(ef3 > limit): break
    ef1 = ef2
    ef2 = ef3
    sm = sm + ef2
  return sm
"-----------------"
test()
