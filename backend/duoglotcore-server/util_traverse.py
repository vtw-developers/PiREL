import cython
import sys
# if cython.compiled: print("[util_traverse] Compiled.", file=sys.stderr)
# else: print("[util_traverse] Interpreted.", file=sys.stderr)
####################################


# traversing json tree in js:
#  https://github.com/HALOCORE/semantic-pretty/blob/main/src/lib/tree-transformer.js


def traverse_nested_list_replace(
  nested_list,
  node_replacer_func
):
  """
  node_replacer_func: node -> should_skip, should_replace, is_subarray, replace_node
  """
  if isinstance(nested_list, list):
    replace_count = 0
    i = 0
    maxlen = len(nested_list)
    while i < maxlen:
      should_skip, should_replace, is_subarray, replace_node = node_replacer_func(nested_list[i])
      if should_skip:
        i += 1
        continue
      if should_replace:
        if not is_subarray:
          nested_list[i] = replace_node
          replace_count += 1
          i += 1
        else:
          replace_count += 1
          nested_list.pop(i)
          maxlen -= 1
          for rep_elem in replace_node:
            nested_list.insert(i, rep_elem)
            i += 1
            maxlen += 1
      else:
        replace_count += traverse_nested_list_replace(nested_list[i], node_replacer_func)
        i += 1
    assert i == len(nested_list)

  else:
    return 0

  return replace_count


def traverse_nested_list_and_dict(list_or_dict, node_reader_func) -> bool:
  """
  node_replacer_func: node -> should_skip, should_stop

  Return True if stop was called
  Return False if stop was never called

  Visit elements in nested list/dict structures in pre-order traversal
  """

  def _traverse_rec(list_or_dict_or_else):

    # is list
    if isinstance(list_or_dict_or_else, list):
      for i in range(len(list_or_dict_or_else)):

        should_skip, should_stop = node_reader_func(i, list_or_dict_or_else[i])
        if should_skip:
          continue
        if should_stop:
          return True

        rec_shold_stop = _traverse_rec(list_or_dict_or_else[i])
        if rec_shold_stop:
          return True

      return False

    # is dict
    elif isinstance(list_or_dict_or_else, dict):
      for key in list_or_dict_or_else:

        should_skip, should_stop = node_reader_func(key, list_or_dict_or_else[key])
        if should_skip:
          continue
        if should_stop:
          return True

        rec_shold_stop = _traverse_rec(list_or_dict_or_else[key])
        if rec_shold_stop:
          return True

      return False

    # not list nor dict
    if not isinstance(list_or_dict_or_else, (int, str)):
      print("TRAVERSE TYPE ERROR:", type(list_or_dict_or_else), list_or_dict_or_else)
      assert 0 == "list_or_dict_or_else_NOT_int_OR_str"

  return _traverse_rec(list_or_dict)
