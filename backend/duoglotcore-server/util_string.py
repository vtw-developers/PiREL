# from difflib import SequenceMatcher
import json


ALLOW_REMOVING_CHARS = set([" ", "\n", "\t"])
ALLOW_ADDING_CHARS = set([" ", "\n", ";"])


def get_string_mapping_a(s1, s2):
  i1 = 0
  i2 = 0
  mapping = []
  while True:
    if i1 >= len(s1): break
    if i2 >= len(s2):
      if s1[i1] in ALLOW_REMOVING_CHARS:
        i1 += 1
        mapping.append(None)
      else:
        around = s1[max(i1-20,0):min(i1+20,len(s1)-1)]
        print(f"ERROR! code_beautifier find unexpected char removal (s2 already ends) [{i1}]:", json.dumps(s1[i1]), json.dumps(around))
        assert "code_beautifier find unexpected char removal in s1 while s2 finished" == 0
    else:
      if s1[i1] == s2[i2]:
        mapping.append(i2)
        i1 += 1
        i2 += 1
      elif s1[i1] != s2[i2]:
        if s1[i1] in ALLOW_REMOVING_CHARS:
          i1 += 1
          mapping.append(None)
        elif s2[i2] in ALLOW_ADDING_CHARS:
          i2 += 1
        else:
            around = s1[max(i1-20,0):min(i1+20,len(s1)-1)]
            targetaround = s2[max(i2-30,0):min(i2+30,len(s2)-1)]
            print(f"ERROR! code_beautifier find unexpected char removal [{i1}]:", json.dumps(s1[i1]), json.dumps(around), json.dumps(targetaround))
            assert "code_beautifier find unexpected char removal" == 0

  assert len(mapping) == len(s1)
  return mapping


# def get_string_mapping_b(str1, str2):
#   s = SequenceMatcher(lambda x:False, str1, str2)
#   idx1to2 = []
#   matching_blocks = []
#   for m in s.get_matching_blocks():
#     matching_blocks.append((m.a, m.b, m.size))
#   current_mb_idx = 0
#   for i in range(len(str1)):
#     current_mb = matching_blocks[current_mb_idx]
#     if i >= current_mb[0] + current_mb[2]:
#       assert i == current_mb[0] + current_mb[2]
#       current_mb_idx += 1
#     current_mb = matching_blocks[current_mb_idx]
#     mapping = None
#     if i < current_mb[0]:
#       if str1[i] not in ALLOW_REMOVING_CHARS:
#         around = str1[max(i-20,0):min(i+20,len(str1)-1)]
#         j = current_mb[0]
#         targetaround = str2[max(j-30,0):min(j+30,len(str2)-1)]
#         print(f"ERROR! code_beautifier find unexpected char removal [{i}]:", json.dumps(str1[i]), json.dumps(around), json.dumps(targetaround))
#         assert "code_beautifier find unexpected char removal" == 0
#     else:
#       assert i >= current_mb[0] and i < current_mb[0] + current_mb[2]
#       mapping = current_mb[1] + (i - current_mb[0])
#     idx1to2.append(mapping)
#   return idx1to2
