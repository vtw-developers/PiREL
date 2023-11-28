# Terms

## Program Pair
It is a pair of generated program and its translation.

```
{
  source: source_prog,
  target: target_prog
}
```

## Translation Pair
It is a pair of program pairs.
It is used as an input to rule inferencer.

```
[
  {
    source: source_prog,
    target: target_prog
  },
  {
    source: source_prog,
    target: target_prog
  }
]
```

