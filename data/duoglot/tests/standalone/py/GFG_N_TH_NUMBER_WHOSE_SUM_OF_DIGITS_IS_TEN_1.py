def test():
  "--- test function ---"
  param =[(93,),(10,),(55,),(94,),(2,),(5,),(37,),(4,),(11,),(46,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  count = 0 ;
  curr = 19 ;
  while(True):
    sum = 0 ;
    x = curr ;
    while(x > 0): sum = sum + x % 10 ; x = int(x / 10);
    if(sum == 10): count += 1 ;
    if(count == n): return curr ;
    curr += 9 ;
  return - 1 ;
"-----------------"
test()
