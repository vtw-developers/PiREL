def test():
  "--- test function ---"
  param =[(['v'],['Z'], 0,),(['6', '8', '3', '3', '5', '2', '5', '6', '9', '9', '2', '6', '2', '1', '9', '3', '7'],['8', '6', '0', '2', '8', '0', '8', '7', '0', '5', '4', '5', '9', '4', '5', '4', '4'], 11,),(['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], 34,),(['e', 'G', 'a', 'r', 'F', 'U', 'W', 'k', 'u', 'z', 'y', 'v', 'A', 'W', 'm', 'G', 'H', 'O', 'I', 'a', 'u', 'V', 'f', 'B', 'q', 'e', 'E', 'e', 'L', 'c', ' ', 'w', 'K', ' ', 'K', 'j', 'j', 's', 'q', 'u', 'n', 'i', 'T', 'a', 'Y'],['S', 'm', 'd', 'a', 'W', 'N', 'F', 'H', 'B', 'E', 'h', 'M', 'z', 'H', 'c', 'X', 'l', 'a', 'R', 'e', 'D', 'D', 'q', 'V', 'U', 'w', 'o', 'K', 'u', 'n', 'b', 'k', 'Y', 'M', 'L', 'H', 'L', 'X', 'H', 'r', 'D', 'o', 'A', 'Y', 'H'], 41,),(['0', '0', '0', '0', '1', '1', '1', '2', '2', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '6', '6', '6', '7', '7', '7', '7', '7', '7', '8', '8', '9', '9', '9', '9'],['0', '0', '0', '0', '0', '1', '1', '1', '2', '2', '2', '3', '3', '4', '4', '4', '5', '5', '5', '5', '6', '6', '7', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '9', '9', '9'], 33,),(['1', '0', '0', '1', '0', '1', '1', '1', '0', '0', '0', '1', '0', '0', '0', '1', '1', '0', '0', '0', '0', '1', '1'],['1', '1', '0', '0', '0', '1', '0', '1', '1', '0', '0', '0', '1', '0', '1', '0', '1', '1', '0', '1', '1', '0', '1'], 13,),([' ', 'B', 'D', 'D', 'D', 'E', 'E', 'E', 'G', 'H', 'J', 'K', 'K', 'K', 'L', 'N', 'O', 'S', 'V', 'W', 'Y', 'Z', 'b', 'c', 'd', 'd', 'f', 'f', 'f', 'f', 'f', 'f', 'i', 'k', 'k', 'o', 't', 'u', 'v', 'x', 'x', 'z'],['G', 'G', 'J', 'K', 'L', 'N', 'Q', 'R', 'R', 'S', 'U', 'W', 'X', 'Y', 'Y', 'a', 'b', 'b', 'b', 'c', 'd', 'e', 'e', 'f', 'f', 'h', 'j', 'j', 'k', 'k', 'l', 'm', 'm', 'n', 'o', 's', 't', 't', 'w', 'z', 'z', 'z'], 40,),(['4'],['8'], 0,),(['0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1'],['0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'], 12,),(['D', 'I', 'u', 'K', 'e', 's', 'n', 'z', 'd', 'y', 'S', 'P', 'y', 'r'],['N', 'h', 'M', 'N', 'n', 'F', 'Y', 'L', 'G', 'w', 'o', 'G', 'y', 'q'], 7,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(s1, s2, index):
  s2[index] = s1[index] ;
  if(index == len(s1)- 1): return ;
  f_gold(s1, s2, index + 1);
"-----------------"
test()
