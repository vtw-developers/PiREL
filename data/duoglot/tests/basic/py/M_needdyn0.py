a = [1,2,3]
b = 1
if b in a:
  print("b in a!")

"""hello"""

c = set()
c.add(2)
d = 2
if d in c:
  print("d in c!")

f = dict()
f["c"] = 1
k = "c"
if k in f:
  print("k in f!")

for i in a:
  print("a", i)

for i in c:
  print("c", i)

for i in f:
  print("f", i, f[i])
