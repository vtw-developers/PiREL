def test():
  "--- test function ---"
  param =[('',),('abbc',),('abcabc',),('agsdbkfdc ',),('ababab',),('aaaaaaa',),('aabaaabcc',),('19',),('1001100',),('DtAnuQbU',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  aCount = 0
  bCount = 0
  cCount = 0
  for i in range(len(s)):
    if(s[i] == 'a'): aCount =(1 + 2 * aCount)
    elif(s[i] == 'b'): bCount =(aCount + 2 * bCount)
    elif(s[i] == 'c'): cCount =(bCount + 2 * cCount)
  return cCount
"-----------------"
test()
