```python
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")


for letter in 'PythonProgramming':
    if letter == 'o':
        continue
```




```js
for (const key in my_dict) {
    const value = my_dict[key];
    console.log(`Key: ${key}, Value: ${value}`);
}

Object.entries(my_dict).forEach(([key, value]) => {
    console.log(`Key: ${key}, Value: ${value}`);
});





for (let letter of 'PythonProgramming') {
    if (letter === 'o') {
        continue;
    }
}

'PythonProgramming'.split('').forEach(letter => {
    if (letter === 'o') {
        return;
    }
});
```