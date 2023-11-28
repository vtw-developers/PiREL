def test():
  "--- test function ---"
  param =[(4922.762671782271, 18,),(- 838.1149138859112, 7,),(8829.981827152698, 18,),(- 7084.090587314416, 11,),(9213.145968063258, 42,),(- 4743.690018081376, 63,),(3281.586891359318, 30,),(- 4006.1025383282854, 63,),(7806.145296436601, 52,),(- 7219.421835366018, 31,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(x, y):
  if(y == 0): return 1
  temp = f_gold(x, int(y / 2))
  if(y % 2 == 0): return temp * temp
  else:
    if(y > 0): return x * temp * temp
    else: return(temp * temp)/ x
"-----------------"
test()
