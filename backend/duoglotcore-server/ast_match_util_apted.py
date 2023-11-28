from apted import APTED, Config
from collections import deque
import Levenshtein


class Tree(object):
  """Represents a Tree Node"""
  def __init__(self, name, *children):
    self.name = name
    self.children = list(children)

  def bracket(self):
    """Show tree using brackets notation"""
    result = str(self.name)
    for child in self.children:
      result += child.bracket()
    return "{{{}}}".format(result)

  def __repr__(self):
    return self.bracket()

  @classmethod
  def from_text(cls, text):
    """Create tree from bracket notation
    Bracket notation encodes the trees with nested parentheses, for example,
    in tree {A{B{X}{Y}{F}}{C}} the root node has label A and two children
    with labels B and C. Node with label B has three children with labels
    X, Y, F.
    """
    tree_stack = []
    stack = []
    for letter in text:
      if letter == "{":
        stack.append("")
      elif letter == "}":
        text = stack.pop()
        children = deque()
        while tree_stack and tree_stack[-1][1] > len(stack):
          child, _ = tree_stack.pop()
          children.appendleft(child)

        tree_stack.append((cls(text, *children), len(stack)))
      else:
        stack[-1] += letter
    return tree_stack[0][0]


class _Naive1Config(Config):
  def rename(self, node1, node2):
    """Compares attribute .value of trees"""
    return 1 if node1.name != node2.name else 0


def editdis_mapping_naive1(t1str, t2str, verbose=True):
  def _getTree(s):
    t = Tree.from_text(s)
    return t
  t1 = _getTree(t1str)
  t2 = _getTree(t2str)
  apted = APTED(t1, t2, _Naive1Config())
  ted = apted.compute_edit_distance()
  print("edit_mapping_naive1 edit distance:", ted)
  mapping = apted.compute_edit_mapping()
  mappingIds = []
  for mp in mapping:
    if(verbose): print("  ", mp)
    comId1 = mp[0].name if mp[0] is not None else None
    comId2 = mp[1].name if mp[1] is not None else None
    mappingIds.append((comId1, comId2))
  return mappingIds


class _Naive2Config(Config):
  def __init__(self, name1ToCmpStrFunc, name2ToCmpStrFunc):
    super().__init__()
    self.name1ToStr = name1ToCmpStrFunc
    self.name2ToStr = name2ToCmpStrFunc
    self._costCache = {}

  # https://stackoverflow.com/questions/64113621/how-to-normalize-levenshtein-distance-between-0-to-1?rq=1
  def _distance_to_sim(self, distance, str1, str2):
    maxlen = max(len(str1), len(str2))
    if maxlen > 0: return distance / maxlen
    else: return 0

  def rename(self, node1, node2):
    """Compares attribute .value of trees"""
    str1 = self.name1ToStr(node1.name)
    str2 = self.name2ToStr(node2.name)
    # string distance
    if str1 not in self._costCache:
      self._costCache[str1] = {}
    if str2 in self._costCache[str1]:
      return self._costCache[str1][str2]
    else:
      dis = Levenshtein.distance(str1, str2)
      sim = self._distance_to_sim(dis, str1, str2)
      self._costCache[str1][str2] = sim
      assert sim >= 0 and sim <= 1
      return sim


def editdis_mapping_naive2(t1str, t2str, name1ToCmpStrFunc, name2ToCmpStrFunc, verbose=True):
  def _getTree(s):
    t = Tree.from_text(s)
    return t
  t1 = _getTree(t1str)
  t2 = _getTree(t2str)
  apted = APTED(t1, t2, _Naive2Config(name1ToCmpStrFunc, name2ToCmpStrFunc))
  ted = apted.compute_edit_distance()
  print("edit_mapping_naive1 edit distance:", ted)
  mapping = apted.compute_edit_mapping()
  mappingIds = []
  for mp in mapping:
    if(verbose): print("  ", mp)
    comId1 = mp[0].name if mp[0] is not None else None
    comId2 = mp[1].name if mp[1] is not None else None
    mappingIds.append((comId1, comId2))
  return mappingIds


def editdis_naive2(t1str, t2str, name1ToCmpStrFunc, name2ToCmpStrFunc, verbose=True):
  def _getTree(s):
    t = Tree.from_text(s)
    return t
  t1 = _getTree(t1str)
  t2 = _getTree(t2str)
  apted = APTED(t1, t2, _Naive2Config(name1ToCmpStrFunc, name2ToCmpStrFunc))
  ted = apted.compute_edit_distance()
  # print("edit_mapping_naive1 edit distance:", ted)
  return ted


# -------------------------------- test code
def naive1_test():
  t1Str = "{A{A2{X1}}{B{X2}{Y{Z}}{F}}{C}}"
  t2Str = "{A{B{X3}{D{Y}{F}}}{C2}}"
  editdis_mapping_naive1(t1Str, t2Str)


if __name__ == "__main__":
  naive1_test()