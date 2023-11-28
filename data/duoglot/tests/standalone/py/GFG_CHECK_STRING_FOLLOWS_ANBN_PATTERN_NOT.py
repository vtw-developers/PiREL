def test():
  "--- test function ---"
  param =[('ba',),('aabb',),('abab',),('aaabb',),('aabbb',),('abaabbaa',),('abaababb',),('bbaa',),('11001000',),('ZWXv te',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str):
  n = len(str)
  for i in range(n):
    if(str[i] != 'a'): break
  if(i * 2 != n): return False
  for j in range(i, n):
    if(str[j] != 'b'): return False
  return True
"-----------------"
test()
