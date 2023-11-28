midVal1 = nums1[i + k // 2 - 1] if i < k else float('inf')

```js
let midVal1;
if (i < k) {
    midVal1 = nums1[i + Math.floor(k / 2) - 1];
} else {
    midVal1 = Number.POSITIVE_INFINITY;
}
```

```js
let midVal1 = i < k ? nums1[i + Math.floor(k / 2) - 1] : Number.POSITIVE_INFINITY;
```



midVal1 = nums1[i + k // 2 - 1] if len(nums1) < len(nums2) else float('inf')

```js
let midVal1;
if (nums1.length < nums2.length) {
    midVal1 = nums1[i + Math.floor(k / 2) - 1];
} else {
    midVal1 = Infinity;
}
```

```js
let midVal1 = nums1.length < nums2.length ? nums1[i + Math.floor(k / 2) - 1] : Infinity;
```