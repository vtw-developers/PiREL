# About
- Contains a simple program for testing a feature that allows learning base rules from scratch.
- Linked to `data/duoglot/tests/trans_programs/py_js/base_upd_minimal.snart`

# Example
Testing the idea by hand

```py
# original code
midVal1 = nums1[i + k // 2 - 1] if i + k // 2 - 1 < m else float('inf')

# template 1
__ = __

a = 5
b = 4
c = k * 2
d = r % 3

# template 2
midVal1 = __ if __ else __

midVal1 = a if k > 2 else b
midVal1 = 1 if True else 2
midVal1 = "hot" if temperature > 30 else "cold"
midVal1 = numbers[k // 2] if k // 2 > m else numbers[0]
```

```js
// translated code
midVal1 = ((i + Math.floor(k / 2)) - 1) < m ? nums1[((i + Math.floor(k / 2)) - 1)] : Infinity;

// template 1
let a = 5;
let b = 4;
let c = k * 2;
let d = r % 3;

// template 2
let midVal1 = k > 2 ? a : b;
let midVal1 = true ? 1 : 2;
let midVal1 = temperature > 30 ? "hot" : "cold";
let midVal1 = Math.floor(k / 2) > m ? numbers[Math.floor(k / 2)] : numbers[0];
```