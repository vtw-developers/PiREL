// level 1: add two numbers
var a, b, total;

function add(a, b) {
  total = a + b;
  return total;
}


// level 2: sum [1, N]
var n, total, i;

function sum_n(n) {
  total = 0;
  i = 1;
  while (i <= n) {
    total = total + i;
  }
  return total;
}


// level 3: sum [1, N]
var n, total, i;

function sum_n(n) {
  total = 0;
  i = 1;
  while (1 > 0) {
    total = total + i;
    if (i == n) {
      break;
    }
  }
  return total;
}