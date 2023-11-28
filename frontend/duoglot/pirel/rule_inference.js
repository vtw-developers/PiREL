// namespace for API
var ruleInfAPI_ns = {};

// namespace for internal functions used in inferTranslationRule()
var _ruleInfInternal_ns = {};

/**
 * Error that is thrown when there is some error during rule post-processing on backend
*/
ruleInfAPI_ns.RulePostProcessingError = class extends Error {
  constructor(message = "") {
    super(message);
    this.name = "RULE_POST_PROCESSING_ERROR";
    this.message = message;
  }
};

/**
 * Error that is thrown when
*/
ruleInfAPI_ns.ContextNotFoundError = class extends Error {
  constructor(message = "") {
    super(message);
    this.name = "CONTEXT_NOT_FOUND_ERROR";
    this.message = message;
  }
};

/*
Given a list of program segments,
return a list of begin/end marks for each segment.
Since we pass all blocks of code joined together with a `\n`,
the marks for blocks[1:] are calculated relative to blocks[0].
*/
_ruleInfInternal_ns.getSegmentsMarks = function (segments) {
  function _numLinesUpToNotIncluding(segmentIdx, segmentsAsLines) {
    let numLines = 0;
    for (let i = 0; i < segmentIdx; i++) {
      numLines += segmentsAsLines[i].length;
    }
    return numLines;
  }
  let segmentsAsLines = segments.map((segment) => segment.split(/\n/));
  let marks = [];
  for (let i = 0; i < segmentsAsLines.length; i++) {
    let beginCol = 0;
    let beginRow = 0 + _numLinesUpToNotIncluding(i, segmentsAsLines);
    let endCol = segmentsAsLines[i].slice(-1)[0].length; // length of last line of i-th segment
    let endRow = beginRow + segmentsAsLines[i].length - 1; // # of lines of i-th segment
    marks.push([beginRow, beginCol, endRow, endCol]);
  }
  return marks;
};

/*
DuoGlot-style AST grammar:
ast: ast_node
ast_node: non-terminal | terminal
non-terminal: List[node_type, node_id, children]
terminal: "str"
node_type: str
node_id: int
children: List[ast_node]

For all non-terminals, return a dict containing:
{node_id: node, ...}
*/
_ruleInfInternal_ns.getNodeIdsToNodeAstsDict = function (ast) {
  function _rec(astNode, mutableDict) {
    // skip terminals
    if (!Array.isArray(astNode)) return;
    // skip string anno
    if (astNode.length >= 1 && astNode[0] === "anno") return;

    console.assert(astNode.length > 2, "Non-terminal AST node should have at least one child: debug");

    let node_id = astNode[1];
    mutableDict[node_id] = astNode;
    // recurse children
    for (let i = 2; i < astNode.length; i++) {
      _rec(astNode[i], mutableDict);
    }
  }
  resultDict = {};
  _rec(ast, resultDict);
  return resultDict;
};

/*
For each mark (#marks == #source-programs == #pairs)
find nodes that contain that mark entirely (i.e. nodes that subsume the marked region)
The output follows this structure:
[
  [
    mark1,
    [
      [node_id, node, node_ann],
      [node_id, node, node_ann],
      ...
    ]
  ],
  [
    mark2,
    [
      [node_id, node, node_ann],
      [node_id, node, node_ann],
      ...
    ]
  ],
  ...
]

p** - parent
c** - child
*s* - start
*e* - end
**l - line
**c - character

TODO what if there are multiple nodes spanning a mark? (related to #5 in debug_rule_inf.js)
*/
_ruleInfInternal_ns.queryRange = function (
  ann,
  ast,
  marks
) {

  function _isIncluded(parentRange, childRange) {
    let [psl, psc, pel, pec] = parentRange;
    let [csl, csc, cel, cec] = childRange;

    if ((csl > psl || (csl == psl && csc >= psc)) && (cel < pel || (cel == pel && cec <= pec))) {
      return true;
    }
    return false;
  }

  // tighter version of _isIncluded
  function _isExact(parentRange, childRange) {
    let [psl, psc, pel, pec] = parentRange;
    let [csl, csc, cel, cec] = childRange;

    if (csl == psl && csc == psc && cel == pel && cec == pec) {
      return true;
    }
    return false;
  }

  let nodeIdsToNodeAstsDict = _ruleInfInternal_ns.getNodeIdsToNodeAstsDict(ast);
  let result = [];

  for (let mark of marks) {
    let includedRangeInfo = [];
    for (let nodeId in ann) {
      let nodeAnn = ann[nodeId];
      let nodeRange = [...nodeAnn[2], ...nodeAnn[3]];
      // `node` contains `mark` entirely
      if (_isExact(nodeRange, mark)) {
        includedRangeInfo.push([nodeId, nodeIdsToNodeAstsDict[nodeId], nodeAnn]);
      }
    }
    result.push([mark, includedRangeInfo]);
  }

  return result;
};

/*
hacky function used in `_ruleInfInternal_ns.astToSExpr`
previous function name: IS_PARNAME_VALCHILD
TODO generalize?
*/
_ruleInfInternal_ns.hackyFunc = function (nodeType) {
  if (nodeType.indexOf("py.comment") >= 0) {
    return true;
  }
  if (nodeType.indexOf("py.string_content") >= 0) {
    return true;
  }
  if (nodeType.indexOf("identifier") > 0) {
    return true;
  }
  if (nodeType.indexOf("string_fragment") > 0) {
    return true;
  }
  if (nodeType.indexOf("number") > 0 || nodeType.indexOf("integer") > 0) {
    return true;
  }
  if (nodeType.indexOf("regex_pattern") > 0) {
    return true;
  }
  if (nodeType.indexOf("regex_flags") > 0) {
    return true;
  }
  return false;
};

/*
hacky function for js used in `_ruleInfInternal_ns.astToSExpr`
previous function name: SHOULD_INSERT_NOSTR_AFTER_STRS
TODO generalize?
*/
_ruleInfInternal_ns._jsHack1 = function (nodeType) {
  if (nodeType === "js.arrow_function") {
    return true;
  }
  if (nodeType === "js.method_definition") {
    if (typeof elem2nd !== "string") {
      return true;
    } else {
      return false;
    }
  }
  return false;
};

/**
 *
 * @param {ast} node DuoGlot-style AST node
 * @param {number} depthVal ?
 * @param {boolean} isIgnoreStr ?
 * @returns [s-expression of `node`, logs]
 */
_ruleInfInternal_ns.astToSExpr = function (node, depthVal, isIgnoreStr) {
  if (node === null) {
    return ["null", ["input is null."]];
  }

  // set up logging
  let _logs = [];
  function _log() {
    _logs.push(Array.from(arguments).join(" "));
  }
  _log("depth_val:", depthVal, " is_ignore_str:", isIgnoreStr);

  // recursive inner function
  function _sExprRec(_node, _parentName, _depth) {
    if (_depth >= depthVal) {
      _log("ignoring node at", _depth);
      return "...";
    }
    // `_node` is non-terminal
    if (Array.isArray(_node)) {
      let _nodeType = _node[0];
      // fragment node (top-most node)
      if (_nodeType === "fragment") {
        let retArr = ["fragment"];
        // there is only one child actually
        for (let i = 1; i < _node.length; i++) {
          retArr.push(_sExprRec(_node[i], _nodeType, _depth + 1));
        }
        return retArr;
      }
      // string annotation node
      else if (_nodeType === "anno") {
        let retArr = ["anno "];
        // children
        for (let i = 1; i < _node.length; i++) {
          let _childType = _node[i][0];
          let _childValue = _node[i][1];
          retArr.push([_childType, _childValue]);
        }
        return retArr;
      }
      // all remaining node types (NT & T)
      else {
        let retArr = ['"' + _nodeType + '"'];
        let nostrTbd = _ruleInfInternal_ns._jsHack1(_nodeType);
        // iterate children, skip node_id
        for (let i = 2; i < _node.length; i++) {
          // special treatment for js: nostr
          if (nostrTbd && typeof _node[i] !== "string") {
            retArr.push(["nostr"]);
            nostrTbd = false;
          }
          retArr.push(_sExprRec(_node[i], _nodeType, _depth + 1));
        }
        if (nostrTbd) {
          alert("What the hell? inserting nostr");
        }
        return retArr;
      }
    }
    // should not happen in proper AST's
    else if (typeof _node == "number") {
      _log("WARN Unexpected ast_node:", _node);
    }
    // `_node` is terminal
    else {
      if (_ruleInfInternal_ns.hackyFunc(_parentName)) {
        return ["val", _node];
      } else {
        if (isIgnoreStr) {
          _log("str node (ignored):", _node);
          return "";
        }
        return ["str", _node];
      }
    }
  }

  let result = _sExprRec(node, node[0], 0);
  return [result, _logs];
};

/*
`asts`: AST's that are to be unified

`fragment`:
["fragment" ast]

`sExpr`:
AST-like structure (refer to logs)
*/
_ruleInfInternal_ns.unifyAstFragments = async function (
  asts,
  mutablePhs,
  mutableTuplePhs,
  wildcardPhFunc,
  areSourceSegments
) {
  let fragments = asts.map((ast) => ["fragment", ast]);
  let sExprLogResults = fragments.map((fragment) => _ruleInfInternal_ns.astToSExpr(fragment, 100, false));
  let sExprs = sExprLogResults.map((x) => x[0]);

  // log
  for (let i = 0; i < sExprLogResults.length; i++) {
    let segmentText = areSourceSegments ? "source" : "target";
    await saveAnyTextfileAsync(
      consts_ns.DEBUG_OUTPUT_RULE_INFERENCE_DIR + `/${segmentText}-ast-to-s-expr-logs-seg${i}.json`,
      JSON.stringify(sExprLogResults[i][1])
    );
    await saveAnyTextfileAsync(
      consts_ns.DEBUG_OUTPUT_RULE_INFERENCE_DIR + `/${segmentText}-ast-to-unify-seg${i}.json`,
      JSON.stringify(fragments[i])
    );
    await saveAnyTextfileAsync(
      consts_ns.DEBUG_OUTPUT_RULE_INFERENCE_DIR + `/${segmentText}-s-expression-seg${i}.json`,
      JSON.stringify(sExprs[i])
    );
  }

  // the main unifying recursive function
  function _commonRootTree(sExprs) {
    let _nodeTypes = sExprs.map((x) => x[0]);
    // node types for all `sExprs` have to be identical
    for (let name of _nodeTypes) {
      if (name !== _nodeTypes[0]) {
        return ["ERROR_DIFF_NAME"];
      }
    }
    // at this point, node types are identical
    let _commonNodeType = _nodeTypes[0];
    // common node type is `str`
    if (_commonNodeType === "str") {
      let commonVal = sExprs[0][1];
      for (let sExpr of sExprs) {
        if (sExpr.length !== 2) {
          return ["ERROR_STR_NODE_LENGTH"];
        }
        if (sExpr[1] !== commonVal) {
          return wildcardPhFunc("_str_", sExprs, mutablePhs, mutableTuplePhs);
        }
      }
      return ["str", commonVal];
    }
    // common node type is `val`
    else if (_commonNodeType === "val") {
      let commonVal = sExprs[0][1];
      for (let sExpr of sExprs) {
        if (sExpr.length !== 2) {
          return ["ERROR_VAL_NODE_LENGTH"];
        }
        if (String(sExpr[1]) !== String(commonVal)) {
          return wildcardPhFunc("_val_", sExprs, mutablePhs, mutableTuplePhs);
        }
      }
      return ["val", commonVal];
    }
    // common node type is neither `str` nor `val`
    else {
      let _isNonTerminal = (nodeType) => nodeType.startsWith('"') && nodeType.indexOf(".") > 0;
      let isNt = _isNonTerminal(_commonNodeType);
      let isFragment = _commonNodeType === "fragment";
      let isNostr = _commonNodeType === "nostr";

      // @satbek: unify string `anno`s
      // NOTE potentially buggy: unifies different types of strings (i.e. r'' with b'', etc.)
      // NOTE experimental: might be problematic with programs with complex strings
      let isAnno = _commonNodeType.trim() === "anno";
      if (isAnno) {
        return null;
      }

      if (!isNt && !isFragment && !isNostr) {
        return ["ERROR_NT_OR_FRAGMENT_EXPECTED"];
      }

      let commonRoot = [_commonNodeType];
      for (let i = 1; true; i++) {
        let ithChildren = sExprs.map((x) => x[i]);
        // the types of i-th children may differ
        // fix on the i-th child of the first segment
        let sExprIthChildSegment1 = ithChildren[0];
        if (sExprIthChildSegment1 === undefined) {
          if (ithChildren.some((x) => x !== undefined)) {
            commonRoot.push(wildcardPhFunc("*", sExprs, mutablePhs, mutableTuplePhs));
          }
          break;
        }
        // i-th child has to be an array
        if (["string", "number"].includes(typeof sExprIthChildSegment1)) {
          commonRoot.push("ERROR_UNEXPECTED_STRING_OR_NUMBER");
          return commonRoot;
        }
        if (!Array.isArray(sExprIthChildSegment1)) {
          commonRoot.push("ERROR_UNEXPECTED_NON_ARRAY_CHILD");
          return commonRoot;
        }
        // compare i-th child of the first segment
        // to the i-th children of the remaining segments
        let toBeCommonIsNt = _isNonTerminal(sExprIthChildSegment1[0]);
        let toBeCommonNodeType = sExprIthChildSegment1[0];
        let nameDiffFound = false;
        let allNt = toBeCommonIsNt;
        // iterate over i-th children of the remaining segments (j -> 1 .. )
        for (let j = 1; j < ithChildren.length; j++) {
          let sExprIthChildSegmentJ = ithChildren[j];
          // i-th child has to be an array
          if (!Array.isArray(sExprIthChildSegmentJ)) {
            commonRoot.push("ERROR_UNEXPECTED_NON_ARRAY_CHILD");
            return commonRoot;
          }
          // types of i-th children are different (thus need to be made into holes)
          if (toBeCommonNodeType !== sExprIthChildSegmentJ[0]) {
            nameDiffFound = true;
          }
          // all of the i-th children are non-terminals (need for distinguishing b/w `.` and `*`)
          if (toBeCommonIsNt && !_isNonTerminal(sExprIthChildSegmentJ[0])) {
            allNt = false;
          }
        }
        // i-th children are non-terminals (recurse down)
        if (allNt) {
          if (nameDiffFound) {
            commonRoot.push(wildcardPhFunc(".", ithChildren, mutablePhs, mutableTuplePhs));
          } else {
            let commonRootTreeVar = _commonRootTree(ithChildren);

            // @satbek: null check due to `anno` check above
            // should not result in regression errors
            if (commonRootTreeVar !== null) {
              commonRoot.push(commonRootTreeVar);
            }

          }
        }
        // i-th children are a mix of non-terminals and terminals (recurse right)
        else {
          if (nameDiffFound) {
            commonRoot.push(wildcardPhFunc("*", sExprs, mutablePhs, mutableTuplePhs));
            break;
          } else {
            let commonRootTreeVar = _commonRootTree(ithChildren);

            // @satbek: null check due to `anno` check above
            // should not result in regression errors
            if (commonRootTreeVar !== null) {
              commonRoot.push(commonRootTreeVar);
            }

          }
        }
      }
      return commonRoot;
    }
  }
  let unified = _commonRootTree(sExprs);
  unified.push(wildcardPhFunc("*", "TAIL", mutablePhs, mutableTuplePhs));
  return unified;
};

/*
POST1: `srcPhs` is mutated
POST2: `srcTuplePhs` is mutated
*/
_ruleInfInternal_ns.srcWildcardPhFunc = function (
  x,
  diffingSExprs,
  mutableSrcPhs,
  mutableSrcTuplePhs
) {
  if (x === "." || x === "*") {
    mutableSrcPhs.push([x, diffingSExprs]);
  } else if (x in mutableSrcTuplePhs) {
    mutableSrcTuplePhs[x].push([x, diffingSExprs]);
  } else {
    console.warn("# ruleInferenceHandler src_wildcard_ph_func Unknown ph:", x);
  }
  // unreachable return? TODO debug
  return '"' + x + '"';
};

/*
POST1: `tarPhs` is mutated
POST2: `tarTuplePhs` is mutated
*/
_ruleInfInternal_ns.tarWildcardPhFunc = function (
  x,
  diffingSExprs,
  mutableTarPhs,
  mutableTarTuplePhs
) {
  if (x === "." || x === "*") {
    mutableTarPhs.push([x, diffingSExprs]);
    return '"' + x + `PH${mutableTarPhs.length}"`;
  } else if (x in mutableTarTuplePhs) {
    mutableTarTuplePhs[x].push([x, diffingSExprs]);
    return x === "_str_" ? `"_strPH${mutableTarTuplePhs[x].length}_"` : `"_valPH${mutableTarTuplePhs[x].length}_"`;
  } else {
    console.warn("# ruleInferenceHandler tar_wildcard_ph_func Unknown ph:", x);
    return '"' + x + '"';
  }
};

_ruleInfInternal_ns.getMinIdxes = function (distMatrix) {
  let result = [];
  for (let i = 0; i < distMatrix.length; i++) {
    let row = distMatrix[i];
    let minVal = Infinity;
    let minIdx = -1;
    for (let j = 0; j < row.length; j++) {
      if (row[j] < minVal) {
        minVal = row[j];
        minIdx = j;
      }
    }
    result.push(minIdx);
  }
  return result;
};

_ruleInfInternal_ns.setPh = function (pattern, searchPh, replacePh) {
  if (Array.isArray(pattern)) {
    return pattern.map((x) => _ruleInfInternal_ns.setPh(x, searchPh, replacePh));
  }
  if (typeof pattern !== "string") {
    throw Error("set_ph expect nested string or array.");
  }
  if (pattern === searchPh) {
    return replacePh;
  }
  return pattern;
};

/*
`sExpr` has a very similar structure to DuoGlot style AST's.
This function returns a string version of it which is THE version
that is parsed by the DuoGlot transpiler.
*/
_ruleInfInternal_ns.prettySExpr = function (sExpr) {
  if (Array.isArray(sExpr)) {
    let result = ["("];
    for (let i = 0; i < sExpr.length; i++) {
      result.push(_ruleInfInternal_ns.prettySExpr(sExpr[i]));
      if (i < sExpr.length - 1) {
        result.push(" ");
      }
    }
    result.push(")");
    return result.join("");
  } else {
    return String(sExpr);
  }
};

/*
This function is a supplementary to `_ruleInfInternal_ns.prettySExpr`
Allows printing translation rules as tree-like that might be used for debugging.
This function has no functional importance for Pirel.
The default `_ruleInfInternal_ns.prettySExpr` is enough.

`globalIndent`: custom prefix for all lines of the output
*/
_ruleInfInternal_ns.prettySExprTreelike = function (sExpr, indentSize = 2, globalIndent = "  ") {
  function _rec(sExpr, indentLevel, indentSize, globalIndent) {
    // base cases
    if (typeof sExpr === "string") {
      return globalIndent + " ".repeat(indentSize).repeat(indentLevel) + sExpr;
    }
    if (Array.isArray(sExpr) && sExpr.length === 2 && typeof sExpr[0] === "string" && typeof sExpr[1] === "string") {
      return globalIndent + " ".repeat(indentSize).repeat(indentLevel) + sExpr[0] + " " + sExpr[1];
    }

    let result = globalIndent + " ".repeat(indentSize).repeat(indentLevel) + "(";
    result += sExpr[0];
    for (let i = 1; i < sExpr.length; i++) {
      result += "\n" + _rec(sExpr[i], indentLevel + 1, indentSize, globalIndent);
    }
    result += "\n" + globalIndent + " ".repeat(indentSize).repeat(indentLevel) + ")";
    return result;
  }
  let result = _rec(sExpr, 0, indentSize, globalIndent);
  return result;
};

/*
Pretty-prints a translation rule to the standard format.
*/
_ruleInfInternal_ns.prettyRule = function (
  match,
  expand,
  treeLike
) {
  let ruleType = "match_expand";
  if (treeLike) {
    return (
      `(${ruleType}\n\n` +
      `${_ruleInfInternal_ns.prettySExprTreelike(match)}\n\n` +
      `${_ruleInfInternal_ns.prettySExprTreelike(expand)}\n\n)`
    );
  }
  return (
    `(${ruleType}\n` +
    `  ${_ruleInfInternal_ns.prettySExpr(match)}\n` +
    `  ${_ruleInfInternal_ns.prettySExpr(expand)}\n)`
  );
};

/**
 * Given a list of source-target program pairs, infer a translation rule.
 *
 * PARAMS
 * programPairs
 * [{source: str, target: str}, {source: str, target: str}, ...]
 *
 * srcLang - 'py'
 * tarLang - 'js'
 *
 * pyBlockReplaced
 * whether or not the program pairs contain a secret
 * function call which replaces a block node (py.block, js.statement_block)
 *
 * TODO this parameter might be unnecessary after introduction of context info
 * isChooseLargestContainingNode
 * whether or not to choose a largest node that has
 * the same boundaries as srcMarks or tarMarks
 *
 * ppTreeLike
 * return rule pretty-printed as a tree (for visual)
*/
ruleInfAPI_ns.inferTranslationRule = async function (
  srcLang,
  tarLang,
  programPairs,
  context,
  templatizedNodeIds,
  templatizedNodesReplaceDWS,
  isInsertSecretFn,
  ppTreeLike = false
) {

  let _lastElem = (arr) => {
    return arr[arr.length - 1];
  };
  let _firstElem = (arr) => {
    return arr[0];
  };
  let _rStrip = (x, characters) => {
    // https://davidbieber.com/snippets/2020-12-26-pythons-strip-lstrip-and-rstrip-in-javascript/
    let end = x.length - 1;
    while (characters.indexOf(x[end]) >= 0) {
      end -= 1;
    }
    return x.substr(0, end + 1);
  };

  // 1. split `programPairs`
  let srcSegments = programPairs.map((pair) => pair["source"].trim());
  let tarSegments = programPairs.map((pair) => pair["target"].trim());

  // 2. get marks
  let srcMarks = _ruleInfInternal_ns.getSegmentsMarks(srcSegments);
  let tarMarks = _ruleInfInternal_ns.getSegmentsMarks(tarSegments);

  // 3. parse
  let [srcAst, srcAnn] = await parseAsync(srcSegments.join("\n"), srcLang);
  let [tarAst, tarAnn] = await parseAsync(tarSegments.join("\n"), tarLang);

  // 4 query range
  let srcQueryResults = _ruleInfInternal_ns.queryRange(srcAnn, srcAst, srcMarks);
  let tarQueryResults = _ruleInfInternal_ns.queryRange(tarAnn, tarAst, tarMarks);

  // 5
  let srcPhs = [];
  let srcTplPhs = { _str_: [], _val_: [] };
  let tarPhs = [];
  let tarTplPhs = { _str_: [], _val_: [] };

  // 6 unify AST fragments
  let srcSmallestContainingNodesPerSegment = srcQueryResults.map((x) => _lastElem(x[1])[1]);
  let srcLargestContainingNodesPerSegment = srcQueryResults.map((x) => _firstElem(x[1])[1]);
  let srcContainingNodesPerSegment = srcLargestContainingNodesPerSegment;
  let srcUnifiedPattern = await _ruleInfInternal_ns.unifyAstFragments(
    srcContainingNodesPerSegment,
    srcPhs,
    srcTplPhs,
    _ruleInfInternal_ns.srcWildcardPhFunc,
    (areSourceSegments = true)
  );

  let tarSmallestContainingNodesPerSegment = tarQueryResults.map((x) => _lastElem(x[1])[1]);
  let tarLargestContainingNodesPerSegment = tarQueryResults.map((x) => _firstElem(x[1])[1]);
  let tarContainingNodesPerSegment = tarLargestContainingNodesPerSegment;
  let tarUnifiedPattern = await _ruleInfInternal_ns.unifyAstFragments(
    tarContainingNodesPerSegment,
    tarPhs,
    tarTplPhs,
    _ruleInfInternal_ns.tarWildcardPhFunc,
    (areSourceSegments = false)
  );

  // 7
  let phsCompare = await computeTreeDistancesAsync(srcPhs, tarPhs, null);
  let strCompare = await computeTreeDistancesAsync(srcTplPhs["_str_"], tarTplPhs["_str_"], "EXACT");
  let valCompare = await computeTreeDistancesAsync(srcTplPhs["_val_"], tarTplPhs["_val_"], "EXACT");

  // 8
  let phsMatchIdxes = _ruleInfInternal_ns.getMinIdxes(phsCompare);
  let strMatchIdxes = _ruleInfInternal_ns.getMinIdxes(strCompare);
  let valMatchIdxes = _ruleInfInternal_ns.getMinIdxes(valCompare);

  // 9
  for (let i = 0; i < phsMatchIdxes.length; i++) {
    tarUnifiedPattern = _ruleInfInternal_ns.setPh(
      tarUnifiedPattern,
      '"*PH' + String(i + 1) + '"',
      '"*' + String(phsMatchIdxes[i] + 1) + '"'
    );
    tarUnifiedPattern = _ruleInfInternal_ns.setPh(
      tarUnifiedPattern,
      '".PH' + String(i + 1) + '"',
      '".' + String(phsMatchIdxes[i] + 1) + '"'
    );
  }

  for (let i = 0; i < strMatchIdxes.length; i++) {
    tarUnifiedPattern = _ruleInfInternal_ns.setPh(
      tarUnifiedPattern,
      '"_strPH' + String(i + 1) + '_"',
      '"_str' + String(strMatchIdxes[i] + 1) + '_"'
    );
  }

  for (let i = 0; i < valMatchIdxes.length; i++) {
    tarUnifiedPattern = _ruleInfInternal_ns.setPh(
      tarUnifiedPattern,
      '"_valPH' + String(i + 1) + '_"',
      '"_val' + String(valMatchIdxes[i] + 1) + '_"'
    );
  }

  // log
  await saveAnyTextfileAsync(
    consts_ns.DEBUG_OUTPUT_RULE_INFERENCE_DIR + `/source-unified-pattern.json`,
    JSON.stringify(srcUnifiedPattern)
  );
  await saveAnyTextfileAsync(
    consts_ns.DEBUG_OUTPUT_RULE_INFERENCE_DIR + `/target-unified-pattern.json`,
    JSON.stringify(tarUnifiedPattern)
  );

  // 10 post-process inferred rule
  let dataToPostProcess = {
    source_pattern: srcUnifiedPattern,
    target_pattern: tarUnifiedPattern,
    templatized_node_ids: templatizedNodeIds,
    context: context,
    templatized_nodes_replace_dws: templatizedNodesReplaceDWS,
    is_insert_secret_fn: isInsertSecretFn
  };
  let resultData = await postProcessTranslationRuleOnBackendAsync(dataToPostProcess);
  // exception on backend during post-processing
  if (!resultData["success"]) {
    if (resultData["error_message"] === "context not found") {
      throw new ruleInfAPI_ns.ContextNotFoundError();
    }
    let errorMessage = resultData["error_message"] + "\n" + resultData["traceback"];
    throw new ruleInfAPI_ns.RulePostProcessingError(errorMessage);
  }
  srcUnifiedPattern = resultData["source"];
  tarUnifiedPattern = resultData["target"];

  return _ruleInfInternal_ns.prettyRule(
    srcUnifiedPattern,
    tarUnifiedPattern,
    ppTreeLike
  );
};

// this function is an interface for debugging
// refer to debug/debug_rule_inf.js
ruleInfAPI_ns.ruleInferenceDebug = async function (data) {

  let programPairs = [
    {
      source: data.source1,
      target: data.target1,
    },
    {
      source: data.source2,
      target: data.target2,
    },
  ];

  console.log(data.context);
  let isInsertSecretFn = data.isInsertSecretFn;

  let rule = await ruleInfAPI_ns.inferTranslationRule(
    "py",  // srcLang
    "js",  // tarLang
    programPairs,  // programPairs
    data.context,
    {},  // templatizedNodeIds
    [],  // templatizedNodesReplaceDWS
    isInsertSecretFn,
    data.pretty_print_rule
  );

  return rule;
};
