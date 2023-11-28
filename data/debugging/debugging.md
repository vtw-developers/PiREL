# Watch expressions when debugging DuoGlot translation

## Inside `TransSession._get_expansion_for_slot()`

```python
# number of rules matched
len(expan_list)

# current source AST being matched (NOTE need to find which sibling exactly is matched)
slot.range_cursor[0]

# id of the matched rules
[x.notes['rule_id'] for x in expan_list]

# matched rules
[self.expansion_programs[x.notes['rule_id']]['match'] for x in expan_list]
[self.expansion_programs[x.notes['rule_id']]['expand'] for x in expan_list]
```

## Inside `TransSession._get_or_create_alt_node()`
For finding the context nodes of problematic node in both source and target.

```python
self.expansion_programs[expansion.notes['rule_id']]['match']
self.expansion_programs[expansion.notes['rule_id']]['expand']
```
