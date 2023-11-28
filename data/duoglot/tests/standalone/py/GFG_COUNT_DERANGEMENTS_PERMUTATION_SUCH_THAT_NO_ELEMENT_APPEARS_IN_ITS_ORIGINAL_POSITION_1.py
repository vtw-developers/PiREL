def test():
  "--- test function ---"
  param =[(22,),(91,),(33,),(93,),(90,),(59,),(88,),(41,),(70,),(63,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  der =[0 for i in range(n + 1)]
  der[0] = 1
  der[1] = 0
  der[2] = 1
  for i in range(3, n + 1): der[i] =(i - 1)*(der[i - 1] + der[i - 2])
  return der[n]
"-----------------"
test()
