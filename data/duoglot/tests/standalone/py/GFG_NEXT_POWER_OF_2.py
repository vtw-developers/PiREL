def test():
  "--- test function ---"
  param =[(74,),(70,),(85,),(78,),(71,),(32,),(97,),(90,),(64,),(48,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  count = 0 ;
  if(n and not(n &(n - 1))): return n
  while(n != 0):
    n >>= 1
    count += 1
  return 1 << count ;
"-----------------"
test()
