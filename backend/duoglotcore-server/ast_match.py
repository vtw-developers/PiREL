import ast_match_util_apted

"""
Match of concrete nodesand type match.
"""

def match_combo_with_AST(ast1, combo1, ast2, combo2, algo_name):
  sourceComboDict = {}
  targetComboDict = {}

  def _comboTreeToAptedStrAndDictRec(comboTree, comboDict):
    str_list = ['{']
    str_list.append(comboTree["comboId"])
    comboDict[comboTree["comboId"]] = comboTree
    for child in comboTree["children"]:
      str_list.append(_comboTreeToAptedStrAndDictRec(child, comboDict))
    str_list.append("}")
    return "".join(str_list)

  sourceAPTEDStr = _comboTreeToAptedStrAndDictRec(combo1, sourceComboDict)
  targetAPTEDStr = _comboTreeToAptedStrAndDictRec(combo2, targetComboDict)
  print("sourceComboTree_APTED", sourceAPTEDStr)
  print("targetComboTree_APTED", targetAPTEDStr)

  sourceAstDict = {}
  targetAstDict = {}

  def _astToDictRec(ast, id_prefix, astdict):
    if isinstance(ast, list):
      astdict[id_prefix + str(ast[1])] = ast
      if len(ast) > 2:
        for i in range(2, len(ast)):
          _astToDictRec(ast[i], id_prefix, astdict)

  _astToDictRec(ast1, "source", sourceAstDict)
  _astToDictRec(ast2, "target", targetAstDict)

  if algo_name == "structure_only":
    result = ast_match_util_apted.editdis_mapping_naive1(sourceAPTEDStr, targetAPTEDStr, verbose=False)
  elif algo_name == "structure_ComboNT_sim":

    def _sourceGetCmpStrFunc(combo):
      mainId = combo["mainId"]
      assert mainId is not None
      return sourceAstDict[mainId][0]

    def _targetGetCmpStrFunc(combo):
      mainId = combo["mainId"]
      assert mainId is not None
      return targetAstDict[mainId][0]

    sourceCmpStrDict = {x:_sourceGetCmpStrFunc(sourceComboDict[x]) for x in sourceComboDict}
    targetCmpStrDict = {x:_targetGetCmpStrFunc(targetComboDict[x]) for x in targetComboDict}

    result = ast_match_util_apted.editdis_mapping_naive2(
      sourceAPTEDStr, targetAPTEDStr,
      lambda comboId : sourceCmpStrDict[comboId],
      lambda comboId : targetCmpStrDict[comboId],
      verbose=False)

  def _matchResultToTMList(result):
    tmList = []
    listId = 1
    for [sourceComboId, targetComboId] in result:
      assert sourceComboId is not None or targetComboId is not None
      sourceComboNT = None
      targetComboNT = None
      if sourceComboId is not None:
        sourceCombo = sourceComboDict[sourceComboId]
        assert "mainId" in sourceCombo
        sourceComboNT = sourceAstDict[sourceCombo["mainId"]][0]
      if targetComboId is not None:
        targetCombo = targetComboDict[targetComboId]
        assert "mainId" in targetCombo
        targetComboNT = targetAstDict[targetCombo["mainId"]][0]

      source_conflict_ugItems = []
      target_conflict_ugItems = []
      expected_Item = None
      for tmItem in tmList:
        if tmItem["sourceComboNT"] == sourceComboNT and sourceComboNT is not None:
          # TODO: consider other comboNT cases
          if tmItem["targetComboNT"] == targetComboNT and targetComboNT is not None:
            tmItem["count"] += 1
            tmItem["observedComboIdPairs"].append([sourceComboId, targetComboId])
            expected_Item = tmItem
          else:
            # source equal, target not equal
            source_conflict_ugItems.append(tmItem)
        else:
          # source not equal
          if tmItem["targetComboNT"] == targetComboNT and targetComboNT is not None:
            target_conflict_ugItems.append(tmItem)
          else: pass
      if expected_Item is None:
        expected_Item = {
          "id": listId,
          "sourceComboNT": sourceComboNT,
          "targetComboNT": targetComboNT,
          "count": 1,
          "conflicts": [],
          "observedComboIdPairs": [[sourceComboId, targetComboId]]
        }
        listId += 1
        tmList.append(expected_Item)
        # notice: length of conflict is #rules, not #times
        for tmItem in source_conflict_ugItems:
          tmItem["conflicts"].append(expected_Item['id'])
          expected_Item["conflicts"].append(tmItem['id'])
        for tmItem in target_conflict_ugItems:
          tmItem["conflicts"].append(expected_Item['id'])
          expected_Item["conflicts"].append(tmItem['id'])
    return tmList

  typematch = _matchResultToTMList(result)
  print("match_combo " + algo_name + " result:", result)
  return result, typematch


def distance_of_AST_frags(frag1, frag2, algo_name):
  if algo_name == "EXACT":
    if frag1 == frag2: return 0
    else: return 1
  id_str_dict = {"": ""}
  str_idx = 0

  def frag_to_str(frag):
    childs = []
    nonlocal str_idx
    if isinstance(frag, str) or isinstance(frag, int):
      id_str_dict[str(str_idx)] = str(frag)
      childs.append("{" + str(str_idx) + "}")
      str_idx += 1
    elif isinstance(frag, list) or isinstance(frag, tuple):
      for elem in frag:
        childs.append(frag_to_str(elem))
    else:
      assert "Unsupported_frag_for_comparison" == 0
    return "{" + "".join(childs) + "}"

  aptedStr1 = frag_to_str(frag1)
  aptedStr2 = frag_to_str(frag2)

  distval = ast_match_util_apted.editdis_naive2(
    aptedStr1, aptedStr2,
    lambda idx : id_str_dict[idx],
    lambda idx : id_str_dict[idx],
    verbose=False)

  print("algo_name:", algo_name, " distance:", distval, "\n  aptedStr1:", aptedStr1, "\n  aptedStr2:", aptedStr2)
  return distval
