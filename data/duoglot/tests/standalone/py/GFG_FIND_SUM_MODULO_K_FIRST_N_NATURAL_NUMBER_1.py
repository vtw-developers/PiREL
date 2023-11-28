def test():
  "--- test function ---"
  param =[(40, 90,),(46, 64,),(97, 20,),(63, 1,),(92, 52,),(60, 35,),(67, 40,),(61, 62,),(74, 61,),(67, 41,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(N, K): ans = 0 ; y = N / K ; x = N % K ; ans =((K *(K - 1)/ 2)* y +(x *(x + 1))/ 2); return int(ans);
"-----------------"
test()
