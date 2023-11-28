def test():
  "--- test function ---"
  param =[('pR',),('9518',),('1',),('nNMCIXUCpRMmvO',),('3170487',),('0100101010',),('Z rONcUqWb',),('00419297',),('00',),('r',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str):
  res = ord(str[0])- 48
  for i in range(1, len(str)):
    if(str[i] == '0' or str[i] == '1' or res < 2): res += ord(str[i])- 48
    else: res *= ord(str[i])- 48
  return res
"-----------------"
test()
