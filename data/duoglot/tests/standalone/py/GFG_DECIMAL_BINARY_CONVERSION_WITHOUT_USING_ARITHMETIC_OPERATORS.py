def test():
  "--- test function ---"
  param =[(35,),(17,),(8,),(99,),(57,),(39,),(99,),(14,),(22,),(7,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  if(n == 0): return "0" ;
  bin = "" ;
  while(n > 0):
    if(n & 1 == 0): bin = '0' + bin ;
    else: bin = '1' + bin ;
    n = n >> 1 ;
  return bin ;
"-----------------"
test()
