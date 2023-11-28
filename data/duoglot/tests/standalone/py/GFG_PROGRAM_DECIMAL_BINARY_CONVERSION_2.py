def test():
  "--- test function ---"
  param =[(18,),(92,),(87,),(50,),(56,),(88,),(3,),(16,),(45,),(58,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(N):
  B_Number = 0
  cnt = 0
  while(N != 0):
    rem = N % 2
    c = pow(10, cnt)
    B_Number += rem * c
    N //= 2
    cnt += 1
  return B_Number
"-----------------"
test()
