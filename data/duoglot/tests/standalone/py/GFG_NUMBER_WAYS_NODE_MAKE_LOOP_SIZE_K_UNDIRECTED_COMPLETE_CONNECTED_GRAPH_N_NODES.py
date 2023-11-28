def test():
  "--- test function ---"
  param =[(27, 59,),(70, 87,),(77, 40,),(83, 26,),(16, 2,),(90, 66,),(39, 72,),(48, 26,),(56, 77,),(10, 47,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n, k):
  p = 1
  if(k % 2): p = - 1
  return(pow(n - 1, k)+ p *(n - 1))/ n
"-----------------"
test()
