def test():
  "--- test function ---"
  param =[('onWEchl',),('2',),('100',),('GHbCZA',),('50568798206105',),('001011110001',),('lljpYhznnyu',),('54499921759984',),('11101',),('qvypgCYEjsyjwZ',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str_):
  n = len(str_)
  arr =[0] * n
  concat = str_ + str_
  for i in range(n): arr[i] = concat[i: n + i]
  arr.sort()
  return arr[0]
"-----------------"
test()
