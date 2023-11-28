def test():
  "--- test function ---"
  param =[('HCoAefoaan',),('80336005',),('01111111110',),('qIH',),('4210598472796',),('10101',),('imqmKdatcgXjs',),('950509666021',),('10111101101',),('wasqgYFvz',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str):
  mx = ""
  for i in range(len(str)): mx = max(mx, str[i:])
  return mx
"-----------------"
test()
