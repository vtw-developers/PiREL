def test():
  "--- test function ---"
  param =[(32,),(52,),(52,),(32,),(73,),(31,),(29,),(75,),(39,),(49,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(A):
  n = 2 * A
  dpArray =[0] *(n + 1)
  dpArray[0] = 1
  dpArray[2] = 1
  for i in range(4, n + 1, 2):
    for j in range(0, i - 1, 2): dpArray[i] +=(dpArray[j] * dpArray[i - 2 - j])
  return int(dpArray[n])
"-----------------"
test()
