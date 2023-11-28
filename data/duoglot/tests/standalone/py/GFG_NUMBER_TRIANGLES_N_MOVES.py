def test():
  "--- test function ---"
  param =[(33,),(72,),(81,),(93,),(8,),(76,),(97,),(91,),(61,),(6,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  answer =[None] *(n + 1);
  answer[0] = 1 ;
  i = 1
  while i <= n: answer[i] = answer[i - 1] * 3 + 2 ; i = i + 1
  return answer[n] ;
"-----------------"
test()
