def test():
  "--- test function ---"
  param =[([2, 2, 4, 4, 9, 10, 14, 16, 16, 19, 20, 21, 25, 26, 29, 36, 36, 37, 38, 44, 44, 49, 53, 54, 56, 61, 62, 64, 72, 72, 73, 77, 80, 84, 84, 87, 93, 94],[6, 8, 10, 10, 12, 14, 24, 31, 33, 33, 35, 35, 35, 41, 46, 47, 49, 51, 52, 56, 57, 59, 62, 65, 72, 72, 73, 73, 79, 80, 82, 83, 83, 84, 87, 87, 93, 99], 27, 21, 23,),([2, 4, - 90, 62, 22, - 94, - 74, - 22, 44, - 94, 20, - 40, 20, 0, 32, 24, 78, 8, 4, 98, - 74, - 60],[58, 74, - 46, 38, - 58, - 78, - 32, - 84, 84, - 54, 84, - 34, - 26, 88, 74, 48, 26, - 92, 68, - 86, 74, 88], 18, 11, 12,),([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 30, 31, 42,),([85, 44, 62, 2, 71, 88, 60, 78, 32, 46, 17, 47, 65, 78, 65, 94],[18, 3, 15, 9, 61, 73, 3, 62, 87, 1, 54, 97, 61, 37, 23, 65], 11, 11, 13,),([- 94, - 84, - 82, - 70, - 70, - 60, - 54, - 54, - 52, - 52, - 46, - 40, - 40, - 36, - 34, - 32, - 30, - 22, - 18, - 16, - 10, - 4, 8, 12, 18, 22, 32, 38, 38, 44, 50, 56, 64, 82, 84, 86, 88],[- 92, - 68, - 64, - 62, - 54, - 52, - 52, - 34, - 24, - 22, - 20, - 12, - 12, - 10, 6, 10, 14, 22, 22, 24, 24, 30, 30, 36, 36, 48, 50, 56, 58, 64, 68, 80, 84, 88, 88, 92, 94], 19, 26, 28,),([0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],[1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0], 24, 17, 23,),([53, 96, 99],[30, 55, 56], 1, 1, 1,),([98, 86, 36, - 68, 86, 22, 52, - 20, - 2, 74, - 72, 86, 80, - 78, 14, 62, 10, 94, - 66, 78, 28, 92, - 8, 46, - 24, 66],[72, - 72, - 90, 24, - 22, 60, 78, - 68, 98, 26, - 30, - 20, 44, - 96, 8, 90, 0, 98, - 24, - 68, - 32, - 62, 0, - 60, 26, - 98], 22, 19, 24,),([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 42, 40, 42,),([6, 21, 86, 58, 48, 27, 18, 73, 16, 79, 51, 33, 63, 26, 37, 88, 48, 58, 44, 32, 58, 23, 31],[87, 77, 44, 15, 70, 89, 36, 79, 82, 3, 18, 76, 37, 79, 85, 97, 19, 53, 17, 74, 87, 58, 49], 14, 22, 19,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(arr1, arr2, m, n, k):
  sorted1 =[0] *(m + n)
  i = 0
  j = 0
  d = 0
  while(i < m and j < n):
    if(arr1[i] < arr2[j]):
      sorted1[d] = arr1[i]
      i += 1
    else:
      sorted1[d] = arr2[j]
      j += 1
    d += 1
  while(i < m):
    sorted1[d] = arr1[i]
    d += 1
    i += 1
  while(j < n):
    sorted1[d] = arr2[j]
    d += 1
    j += 1
  return sorted1[k - 1]
"-----------------"
test()
