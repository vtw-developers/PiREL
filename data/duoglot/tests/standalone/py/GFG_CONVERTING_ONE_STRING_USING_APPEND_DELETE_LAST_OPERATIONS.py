def test():
  "--- test function ---"
  param =[('ZNHGro', 'jAdbtDUYQu', 3,),('382880806774', '65565', 10,),('0', '00100010100', 2,),('lxHTRFCTSQ', 'sViXYE', 89,),('6399914758', '780990121', 9,),('01100011100000', '0100', 0,),('WkGqlob', 'NpQVdXzEtUZy', 6,),('46974006151', '74438', 11,),('1001001', '1000010', 15,),('IJQ', 'nFOHAeYEAp', 42,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str1, str2, k):
  if((len(str1)+ len(str2))< k): return True
  commonLength = 0
  for i in range(0, min(len(str1), len(str2)), 1):
    if(str1[i] == str2[i]): commonLength += 1
    else: break
  if((k - len(str1)- len(str2)+ 2 * commonLength)% 2 == 0): return True
  return False
"-----------------"
test()
