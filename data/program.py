def fun(nums1, i, k, m):
  midVal1 = nums1[i + k // 2 - 1] if i + k // 2 - 1 < m else float('inf')
  return midVal1