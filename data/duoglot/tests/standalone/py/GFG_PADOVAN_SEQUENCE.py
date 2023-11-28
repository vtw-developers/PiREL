def test():
  "--- test function ---"
  param =[(1,),(92,),(29,),(52,),(55,),(13,),(83,),(83,),(10,),(67,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  pPrevPrev, pPrev, pCurr, pNext = 1, 1, 1, 1
  for i in range(3, n + 1):
    pNext = pPrevPrev + pPrev
    pPrevPrev = pPrev
    pPrev = pCurr
    pCurr = pNext
  return pNext ;
"-----------------"
test()
