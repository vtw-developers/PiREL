def test():
  "--- test function ---"
  param =[(49, 15,),(59, 69,),(76, 20,),(27, 76,),(61, 60,),(67, 27,),(63, 71,),(85, 25,),(90, 64,),(24, 55,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n, k):
  if(k <= 0): return n
  return(n & ~(1 <<(k - 1)))
"-----------------"
test()
