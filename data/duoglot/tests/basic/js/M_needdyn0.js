a = [1, 2, 3];
b = 1;
if (a.indexOf(b) >= 0) {
    console.log("b in a!");
}
"omitted docs";
c = new Set();
c.add(2);
d = 2;
if (c.indexOf(d) >= 0) {
    console.log("d in c!");
}
f = {}
f["c"] = 1;
k = "c";
if (f.indexOf(k) >= 0) {
    console.log("k in f!");
}
for (let i of a) {
    console.log("a", i);
}
for (let i of c) {
    console.log("c", i);
}
for (let i of f) {
    console.log("f", i, f[i]);
}