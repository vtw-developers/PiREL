def test():
  "--- test function ---"
  param =[('IZTSMw j', 'W', 'k',),('7288334', '6', '9',),('010110000', '1', '1',),('b gJX', 't', 'P',),('734', '4', '4',),('1', '1', '1',),('xCaUKdhA', 'X', 'S',),('4370992644981', '5', '6',),('01010', '0', '1',),('ZNIFGshaWA', 'Q', 'x',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s, c1, c2):
  l = len(s)
  for i in range(l):
    if(s[i] == c1): s = s[0: i] + c2 + s[i + 1:]
    elif(s[i] == c2): s = s[0: i] + c1 + s[i + 1:]
  return s
"-----------------"
test()
