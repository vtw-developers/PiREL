def test():
  "--- test function ---"
  param =[(91,),(52,),(78,),(51,),(65,),(39,),(42,),(12,),(56,),(98,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(k):
  cur = int((k *(k - 1))+ 1)
  sum = 0
  while k:
    sum += cur
    cur += 2
    k = k - 1
  return sum
"-----------------"
test()
