let a = 5;
if (a > 0) {
  a = a + 4;
}

for (let i = 0; i < 10; i++) {
  a += i;
}

while (true) {
  a -= 1;
  if (a === 0) continue;
  if (a < 0) break;
}