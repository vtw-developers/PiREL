def test():
  "--- test function ---"
  param =[("00001",),("0000",),("11",),("111110",),("1",),("111010111010",),("hUInqJXNdbfP",),("5191",),("1110101101",),('NupSrU xz',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str):
  zeros = 0
  ones = 0
  for i in range(0, len(str)):
    ch = str[i] ;
    if(ch == '0'): zeros = zeros + 1
    else: ones = ones + 1
  return(zeros == 1 or ones == 1);
"-----------------"
test()
