def test():
  "--- test function ---"
  param =[(52, 29,),(36, 94,),(12, 6,),(69, 7,),(45, 11,),(7, 51,),(45, 55,),(62, 86,),(96, 63,),(89, 12,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(a, b):
  if(a == b): return a
  if(a == 0): return b
  if(b == 0): return a
  if((~ a & 1)== 1):
    if((b & 1)== 1): return f_gold(a >> 1, b)
    else: return(f_gold(a >> 1, b >> 1)<< 1)
  if((~ b & 1)== 1): return f_gold(a, b >> 1)
  if(a > b): return f_gold((a - b)>> 1, b)
  return f_gold((b - a)>> 1, a)
"-----------------"
test()
