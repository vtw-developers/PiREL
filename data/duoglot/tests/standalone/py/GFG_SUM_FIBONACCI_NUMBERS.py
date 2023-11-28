def test():
  "--- test function ---"
  param =[(9,),(50,),(7,),(21,),(21,),(91,),(11,),(25,),(62,),(4,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  if(n <= 0): return 0
  fibo =[0] *(n + 1)
  fibo[1] = 1
  sm = fibo[0] + fibo[1]
  for i in range(2, n + 1):
    fibo[i] = fibo[i - 1] + fibo[i - 2]
    sm = sm + fibo[i]
  return sm
"-----------------"
test()
