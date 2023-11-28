def test():
  "--- test function ---"
  param =[('ZCoQhuM', 2,),('7437725', 53,),('11', 30,),('buGlvR', 1,),('9', 92,),('101101010110', 3,),('YguiM', 18,),('8198', 90,),('11101', 71,),('hUInqJXNdbfP', 4,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str, n):
  l = len(str)
  if(l >= n): return True
  return False
"-----------------"
test()
