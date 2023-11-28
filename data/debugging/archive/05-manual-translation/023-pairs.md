midVal1 = nums1[i + k // 2 - 1] if i + k - 1 < m else float('inf')

```js
var midVal1 = (i + k - 1 < m) ? nums1[Math.floor(i + k / 2) - 1] : Infinity;
```
```js
let midVal1;
if (i + k - 1 < m) {
    midVal1 = nums1[Math.floor(i + k / 2) - 1];
} else {
    midVal1 = Infinity;
}
```




midVal1 = nums1[i + k // 2 - 1] if x + y - 1 < m else float('inf')

```js
let midVal1 = (i + Math.floor(k / 2) - 1 < m) ? nums1[i + Math.floor(k / 2) - 1] : Number.POSITIVE_INFINITY;
```

In JavaScript, the `Number.POSITIVE_INFINITY` property represents the positive Infinity value. This is equivalent to Python's `float('inf')`.

JavaScript doesn't directly support Python's conditional assignment syntax or the `float('inf')` representation. However, we can achieve the same effect with an `if` statement and by using `Infinity` for infinite values.

Translation 1:
```js
let midVal1;
if (i + k / 2 - 1 < m) {
    midVal1 = nums1[i + Math.floor(k / 2) - 1];
} else {
    midVal1 = Infinity;
}
```

Translation 2 (Alternative using ternary operator):
```js
let midVal1 = i + Math.floor(k / 2) - 1 < m ? 
            nums1[i + Math.floor(k / 2) - 1] : 
            Infinity;
```

