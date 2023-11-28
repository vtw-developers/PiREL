def test():
  "--- test function ---"
  param =[(79, 84,),(61, 29,),(39, 77,),(39, 65,),(61, 78,),(86, 73,),(7, 92,),(86, 50,),(86, 63,),(11, 2,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(A, B):
  variable = 1
  if(A == B): return 1
  elif((B - A)>= 5): return 0
  else:
    for i in range(A + 1, B + 1): variable =(variable *(i % 10))% 10
    return variable % 10
"-----------------"
test()
