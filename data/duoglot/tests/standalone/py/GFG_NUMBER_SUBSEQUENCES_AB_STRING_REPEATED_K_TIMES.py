def test():
  "--- test function ---"
  param =[('abbc', 96,),('abahk', 7,),('hugbabab', 5,),('abadbc', 60,),('nkg9', 8,),('jh7dab', 41,),('abd', 87,),('aabb8yk', 4,),('1111', 18,),('PFXAhr', 8,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s, K):
  n = len(s)
  c1 = 0
  c2 = 0
  C = 0
  for i in range(n):
    if s[i] == 'a': c1 += 1
    if s[i] == 'b':
      c2 += 1
      C += c1
  return C * K +(K *(K - 1)/ 2)* c1 * c2
"-----------------"
test()
