
let bar = null;
let a = 5;
let b = 0;
try {
  bar = b !== 0 ? a / b : (() => {throw Error("ZeroDivisionError")})()
  console.log("bar:", bar);
} catch (e) {
  if (e.message === "ZeroDivisionError") console.log("division by zero!");
  else throw e;
}
console.log("bar=", bar);
