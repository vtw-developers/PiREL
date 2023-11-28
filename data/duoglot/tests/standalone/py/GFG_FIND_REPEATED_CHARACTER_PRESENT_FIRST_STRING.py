def test():
  "--- test function ---"
  param =[('ORXMflacQFBv',),('39977638567848',),('011110011011',),('fYjfNy',),('222280492',),('11',),('UjntBg',),('6866190138212',),('0000',),('FWz PWEQgVlRZ',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s):
  p = - 1
  for i in range(len(s)):
    for j in range(i + 1, len(s)):
      if(s[i] == s[j]):
        p = i
        break
    if(p != - 1): break
  return p
"-----------------"
test()
