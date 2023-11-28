def test():
  "--- test function ---"
  param =[(87,),(69,),(15,),(11,),(11,),(15,),(47,),(65,),(50,),(58,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  BT =[0] *(n + 1)
  BT[0] = BT[1] = 1
  for i in range(2, n + 1):
    for j in range(i): BT[i] += BT[j] * BT[i - j - 1]
  return BT[n]
"-----------------"
test()
