def test():
  "--- test function ---"
  param =[(76,),(91,),(62,),(65,),(83,),(57,),(76,),(6,),(2,),(86,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  prevPrev = 1
  prev = 2
  curr = 3
  while n > 0:
    prevPrev = prev
    prev = curr
    curr = prevPrev + prev
    n = n -(curr - prev - 1)
  n = n +(curr - prev - 1)
  return prev + n
"-----------------"
test()
