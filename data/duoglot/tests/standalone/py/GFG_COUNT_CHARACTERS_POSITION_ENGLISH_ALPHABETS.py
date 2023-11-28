def test():
  "--- test function ---"
  param =[('lLkhFeZGcb',),('ABcED',),('geeksforgeeks',),('Alphabetical',),('abababab',),('bcdefgxyz',),('cBzaqx L',),(' bcd',),('11',),('MqqKY',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str):
  result = 0
  for i in range(len(str)):
    if((i == ord(str[i])- ord('a'))or(i == ord(str[i])- ord('A'))): result += 1
  return result
"-----------------"
test()
