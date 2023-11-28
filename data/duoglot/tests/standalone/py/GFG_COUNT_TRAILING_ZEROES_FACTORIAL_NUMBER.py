def test():
  "--- test function ---"
  param =[(9,),(43,),(50,),(32,),(37,),(51,),(33,),(49,),(1,),(75,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  count = 0
  i = 5
  while(n / i >= 1):
    count += int(n / i)
    i *= 5
  return int(count)
"-----------------"
test()
