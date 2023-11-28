let bar = true;
let y = [1, [21, 22], 3, 4, 5];
let str_list = [];
for (let x of y) {
  str_list.push(x.toString());
}
let c = " good nice";
console.log("hi" + bar.toString());

let a = 0;
for (let i = 0; i < 10; i++) {
  for (let j = 10; j > i; j -= 1) {
    a += Math.abs(i * j);
  }
}

function baz(x, y, z) {}

function foo(x, y) {
  a = x;
  let z = x + y;
  if (bar) {
    baz("hello", x, y);
    return z;
  }
  return x - y;
}

try {
  throw Error("CustomError");
} catch (e) {
  console.log("Exception!");
  console.log(e);
} 
