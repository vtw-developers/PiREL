def test():
  "--- test function ---"
  param =[(37, 93,),(58, 13,),(89, 27,),(75, 14,),(59, 47,),(84, 39,),(47, 76,),(37, 75,),(83, 62,),(28, 58,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(a, b):
  if(a == 0): return b
  if(b == 0): return a
  k = 0
  while(((a | b)& 1)== 0):
    a = a >> 1
    b = b >> 1
    k = k + 1
  while((a & 1)== 0): a = a >> 1
  while(b != 0):
    while((b & 1)== 0): b = b >> 1
    if(a > b):
      temp = a
      a = b
      b = temp
    b =(b - a)
  return(a << k)
"-----------------"
test()
