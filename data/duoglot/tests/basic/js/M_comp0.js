let y = [1, [21, 22], 3, 4, 5];
let str_list = [];
for (let x of y) {
  str_list.push(x.toString());
}
console.log(str_list);