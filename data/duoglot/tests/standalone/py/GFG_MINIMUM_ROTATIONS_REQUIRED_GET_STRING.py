def test():
  "--- test function ---"
  param =[('vdevdNdQSopPtj',),('5',),('100010101011',),('tlDOvJHAyMllu',),('06',),('101',),('DYgtU',),('4',),('00',),('Dt',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str):
  tmp = str + str
  n = len(str)
  for i in range(1, n + 1):
    substring = tmp[i: n]
    if(str == substring): return i
  return n
"-----------------"
test()
