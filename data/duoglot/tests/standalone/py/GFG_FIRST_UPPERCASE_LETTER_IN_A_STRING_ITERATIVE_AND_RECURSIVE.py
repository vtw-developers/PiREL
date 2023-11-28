def test():
  "--- test function ---"
  param =[('pH',),('96544000',),('000010000',),('ujqpx',),('20684847994',),('111',),('rclkv',),('45173693434',),('11111011001101',),('f',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str):
  for i in range(0, len(str)):
    if(str[i].istitle()): return str[i]
  return 0
"-----------------"
test()
