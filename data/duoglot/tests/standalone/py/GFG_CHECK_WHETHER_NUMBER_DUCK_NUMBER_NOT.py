def test():
  "--- test function ---"
  param =[('HLlQWSphZcIC',),('080287724',),('0000100000',),(' Q',),('4247040983',),('00001011101',),('LbNsnYTHmLbCf',),('24',),('110',),('ie',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(num):
  l = len(num)
  count_zero = 0
  i = 1
  while i < l:
    ch = num[i]
    if(ch == "0"): count_zero = count_zero + 1
    i = i + 1
  return count_zero
"-----------------"
test()
