var n, total, i;

// Find sum of integers from 0 to N
function sum_n(n) {
  total = 0;
  i = 1;
  while (i <= n) {
    total = total + i;
  }
  return total;
}