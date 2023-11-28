def test():
  "--- test function ---"
  param =[(60, 71,),(56, 17,),(16, 16,),(42, 60,),(55, 56,),(64, 59,),(68, 24,),(88, 2,),(64, 94,),(42, 79,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n, k):
  res = ""
  for i in range(k): res = res + chr(ord('a')+ i)
  count = 0
  for i in range(n - k):
    res = res + chr(ord('a')+ count)
    count += 1
    if(count == k): count = 0 ;
  return res
"-----------------"
test()
