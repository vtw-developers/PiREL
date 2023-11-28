// default values for program pair editors
let DEFAULT_PAIRS = [
  // 0. default
  {
    source1: "print()",
    target1: "console.log();",
    source2: "print(1, 'hi')",
    target2: "console.log(1, 'hi');"
  },
  // 1. default example with hole at return type annotation
  {
    source1: "def f_gold(s: str) -> int:\n    PIREL_PRUNE_THIS_AND_AFTER()\n    i = ans = 0\n    chars = set()\n    for j, c in enumerate(s):\n        while c in chars:\n            chars.remove(s[i])\n            i += 1\n        chars.add(c)\n        ans = max(ans, j - i + 1)\n    return ans",
    target1: "function f_gold(s) {\n    PIREL_PRUNE_THIS_AND_AFTER();\n    let i = 0;\n    let ans = 0;\n    let chars = new Set();\n    for (let j = 0; j < s.length; j++) {\n        let c = s[j];\n        while (chars.has(c)) {\n            chars.delete(s[i]);\n            i++;\n        }\n        chars.add(c);\n        ans = Math.max(ans, j - i + 1);\n    }\n    return ans;\n}",
    source2: "def f_gold(s: str) -> str:\n    PIREL_PRUNE_THIS_AND_AFTER()\n    i = ans = 0\n    chars = set()\n    for j, c in enumerate(s):\n        while c in chars:\n            chars.remove(s[i])\n            i += 1\n        chars.add(c)\n        ans = max(ans, j - i + 1)\n    return ans",
    target2: "function f_gold(s) {\n    PIREL_PRUNE_THIS_AND_AFTER();\n    let i = 0;\n    let ans = 0;\n    let chars = new Set();\n    for (let j = 0; j < s.length; j++) {\n        let c = s[j];\n        while (chars.has(c)) {\n            chars.delete(s[i]);\n            i++;\n        }\n        chars.add(c);\n        ans = Math.max(ans, j - i + 1);\n    }\n    return ans;\n}"
  },
  // 2. complex rule with phs: [`val`, `.`, `*`]
  {
    source1: "for i,v in enumerate(e):\n  a += 1",
    target1: "for (let i = 0; i < e.length; i++) {\n    let v = e[i];\n    a += 1;\n}",
    source2: "for k,(a,b) in enumerate(d):\n  pass",
    target2: "for (let k = 0; k < d.length; k++) {\n    let [a,b] = d[k];\n    ;\n}"
  },
  // 3. replace py.block with pass_statement
  {
    source1: "for i,v in enumerate(e):\n  pass",
    target1: "for (let i = 0; i < e.length; i++) {\n    let v = e[i];\n}",
    source2: "for k,(a,b) in enumerate(d):\n  pass",
    target2: "for (let k = 0; k < d.length; k++) {\n    let [a,b] = d[k];\n}"
  },
  // 4. replace py.block with secret function
  {
    source1: "def f_gold(s: str) -> int:\n    some_secret_fn_4071()",
    target1: "function f_gold(s) {\n    some_secret_fn_4071();\n}",
    source2: "def f_gold(s: str) -> str:\n    some_secret_fn_4071()",
    target2: "function f_gold(s) {\n    some_secret_fn_4071();\n}"
  },
  // 5. debug ValueError: There has to be a matching placeholder in S for every placeholder in T.
  {
    source1: "### lengthOfLongestSubstring \nfrom typing import *\ndef f_gold(s: str) -> int:\n    some_secret_fn_4071()\n",
    target1: "function lengthOfLongestSubstring(s) {\n    some_secret_fn_4071();\n}\n",
    source2: "### lengthOfLongestSubstring \nfrom typing import *\ndef f_gold(arg1: Any) -> int:\n    some_secret_fn_4071()\n",
    target2: "function lengthOfLongestSubstring(arg1) {\n    some_secret_fn_4071();\n}\n"
  },
  // 6. debug matching placeholders error
  {
    source1: "for ind, elem in enumerate(vals):\n    some_secret_fn_4071()",
    target1: "for (let ind = 0; ind < vals.length; ind++) {\n    const elem = vals[ind];\n    some_secret_fn_4071();\n}",
    source2: "for position, word in enumerate(items):\n    some_secret_fn_4071()",
    target2: "for (let position = 0; position < items.length; position++) {\n    let word = items[position];\n    some_secret_fn_4071();\n}"
  },
  // 7. one hole at a time (later merge rules)
  {
    source1: "strs = [chars[int(d) - 2] for d in digits]",
    target1: "const strs = digits.map(d => chars[d - 2]);",
    source2: "strs = [letters[int(d) - 2] for d in digits]",
    target2: "const strs = digits.map(d => letters[d - 2]);"
  },
  // 8. one hole at a time (later merge rules)
  {
    source1: "strs = [chars[int(d) - 2] for d in digits]",
    target1: "const strs = digits.map(d => chars[d - 2]);",
    source2: "strs = [chars[int(dgt) - 2] for dgt in digits]",
    target2: "const strs = digits.map(dgt => chars[dgt - 2]);"
  },
  // 9. debug L0017 list_comprehension sub-template
  {
    source1: "strs = [chars[int(d) - 2] for d in chars]",
    target1: "var strs = chars.map(function(d) {\n    return chars[parseInt(d) - 2];\n});",
    source2: "strs = [chars[int(d) - 2] for d in digit_list]",
    target2: "var strs = digit_list.map(function(d) {\n    return chars[parseInt(d) - 2];\n});"
  },
  // 10. interesting specimen (rule can actually be inferenced)
  {
    source1: "from datetime import *",
    target1: "// No equivalent in JavaScript",
    source2: "from typing import *",
    target2: "// No equivalent in JavaScript"
  },
  // 11.
  {
    source1: "n = len(nums)",
    target1: "var n = nums.length;",
    source2: "x = len(y)",
    target2: "var x = y.length;"
  },
  // 12.
  {
    source1: "not res",
    target1: "!res;",
    source2: "not flag",
    target2: "!flag;"
  },
  // 13. L0004 tough list comprehension
  {
    source1: "array[i + k // 2 - 1] if i + k // 2 - 1 < m else float('inf')",
    target1: "array[i + Math.floor(k / 2) - 1] < m ? array[i + Math.floor(k / 2) - 1] : Infinity;",
    source2: "lst[i + k // 2 - 1] if i + k // 2 - 1 < m else float('inf')",
    target2: "lst[i + Math.floor(k / 2) - 1] < m ? lst[i + Math.floor(k / 2) - 1] : Infinity;",
  },
  // 14. strings (anno)
  {
    source1: "print('hi')",
    target1: "console.log('hi');",
    source2: "print('hello')",
    target2: "console.log('hello');"
  },
  // 15. L0004 tough list comprehension
  {
    source1: "midVal1 = array[i + k // 2 - 1] if i + k // 2 - 1 < m else float('inf')",
    target1: "midVal1 = array[i + Math.floor(k / 2) - 1] < m ? array[i + Math.floor(k / 2) - 1] : Infinity;",
    source2: "midVal1 = lst[i + k // 2 - 1] if i + k // 2 - 1 < m else float('inf')",
    target2: "midVal1 = lst[i + Math.floor(k / 2) - 1] < m ? lst[i + Math.floor(k / 2) - 1] : Infinity;",
  },
  // 16. L0004 bug in rule inference
  {
    source1: "x, n = len(nums1), len(nums2)",
    target1: "var x = nums1.length;\nvar n = nums2.length;",
    source2: "size, n = len(nums1), len(nums2)",
    target2: "var size = nums1.length;\nvar n = nums2.length;"
  },
  // 17
  {
    source1: "a = 5",
    target1: "let a = 5;",
    source2: "b = 4",
    target2: "let b = 4;"
  },
  // 18
  {
    source1: "c = k * 2",
    target1: "let c = k * 2;",
    source2: "d = r % 3",
    target2: "let d = r % 3;"
  },
  // 19
  {
    source1: "midVal1 = a if k > 2 else b",
    target1: "let midVal1 = k > 2 ? a : b;",
    source2: "midVal1 = 1 if True else 2",
    target2: "let midVal1 = true ? 1 : 2;"
  },
  // 20
  {
    source1: "midVal1 = \"hot\" if temperature > 30 else \"cold\"",
    target1: "let midVal1 = temperature > 30 ? \"hot\" : \"cold\";",
    source2: "midVal1 = numbers[k // 2] if k // 2 > m else numbers[0]",
    target2: "let midVal1 = Math.floor(k / 2) > m ? numbers[Math.floor(k / 2)] : numbers[0];"
  },
  // 21
  {
    source1: "def f_gold(x: float, n: int) -> int:\n    return n",
    target1: "function f_gold(x, n) {\n    return n;\n}",
    source2: "def f_gold(arg1: int, n: int) -> int:\n    return n",
    target2: "function f_gold(arg1, n) {\n    return n;\n}"
  },
  // 22 return type annotation
  {
    source1: "def f_gold() -> list[int]:\n    return []",
    target1: "function f_gold() {\n    return [];\n}",
    source2: "def f_gold() -> List[Integer]:\n    return []",
    target2: "function f_gold() {\n    return [];\n}"
  },
  // 23 return type annotation
  {
    source1: "def f_gold(arg1: int, target: int) -> int:\n    return target",
    target1: "function f_gold(arg1, target) {\n    return target;\n}",
    source2: "def f_gold(input_data: 'input_type', target: int) -> int:\n    return target",
    target2: "function f_gold(input_data, target) {\n    return target;\n}",
    context: {
      "source_context": {
        "siblings": [],
        "parents": [
          "\"py.parameters\"",
          "\"py.function_definition\""
        ]
      },
      "target_context": {
        "siblings": [],
        "parents": [
          "\"js.formal_parameters\"",
          "\"js.function_declaration\""
        ]
      }
    }
  },
  // 24 return type annotation
  {
    source1: "for i, val in enumerate(my_list):\n    secret_fun_4071()",
    target1: "my_list.forEach((val, i) => {\n    secret_fun_4071();\n});",
    source2: "for _ , element in enumerate(data):\n    secret_fun_4071()",
    target2: "data.forEach((element, _) => {\n    secret_fun_4071();\n});",
    context: {
      "source_context": {
        "siblings": [],
        "parents": []
      },
      "target_context": {
        "siblings": [],
        "parents": []
      }
    },
    isInsertSecretFn: true,
  },
];
let DEFAULT_PAIR_IDX = 24;

require.config({ paths: { vs: '../../../_common/monaco/node_modules/monaco-editor/min/vs' } });

// DOM buttons
let debugRuleInferenceButton = document.getElementById("debug-rule-inf-btn");
debugRuleInferenceButton.addEventListener("click", debugRuleInferenceButtonHandler);

// DOM editors
let sourceEditor1Elem = document.getElementById("source-1-editor");
let sourceEditor2Elem = document.getElementById("source-2-editor");
let targetEditor1Elem = document.getElementById("target-1-editor");
let targetEditor2Elem = document.getElementById("target-2-editor");
let contextEditorElem = document.getElementById("context-editor");
let generatedRuleEditorElem = document.getElementById("generated-rule-editor");

// DOM controls
let prettyPrintRuleCheckbox = document.getElementById("pretty-print-rule");

// editor objects
let sourceEditorObj1 = null;
let sourceEditorObj2 = null;
let targetEditorObj1 = null;
let targetEditorObj2 = null;
let contextEditorObj = null;
let generatedRuleEditorObj = null;

// functions
(async function initEditors() {
  require(['vs/editor/editor.main'], function () {
    sourceEditorObj1 = monaco.editor.create(sourceEditor1Elem, {
      value: DEFAULT_PAIRS[DEFAULT_PAIR_IDX]['source1'],
      language: 'python',
      wordWrap: "on",
      automaticLayout: true
    });
    sourceEditorObj2 = monaco.editor.create(sourceEditor2Elem, {
      value: DEFAULT_PAIRS[DEFAULT_PAIR_IDX]['source2'],
      language: 'python',
      wordWrap: "on",
      automaticLayout: true
    });
    targetEditorObj1 = monaco.editor.create(targetEditor1Elem, {
      value: DEFAULT_PAIRS[DEFAULT_PAIR_IDX]['target1'],
      language: 'javascript',
      wordWrap: "on",
      automaticLayout: true
    });
    targetEditorObj2 = monaco.editor.create(targetEditor2Elem, {
      value: DEFAULT_PAIRS[DEFAULT_PAIR_IDX]['target2'],
      language: 'javascript',
      wordWrap: "on",
      automaticLayout: true
    });
    contextEditorObj = monaco.editor.create(contextEditorElem, {
      value: JSON.stringify(DEFAULT_PAIRS[DEFAULT_PAIR_IDX]['context']),
      language: 'json',
      wordWrap: "on",
      automaticLayout: true,
      tabSize: 2
    });
    generatedRuleEditorObj = monaco.editor.create(generatedRuleEditorElem, {
      // value: "",
      // language: 'javascript',
      wordWrap: "on",
      automaticLayout: true
    });
  });
})();

// entry point
async function debugRuleInferenceButtonHandler() {

  let sourceProgram1 = sourceEditorObj1.getValue();
  let sourceProgram2 = sourceEditorObj2.getValue();
  let targetProgram1 = targetEditorObj1.getValue();
  let targetProgram2 = targetEditorObj2.getValue();

  let contextStr = contextEditorObj.getValue();
  let emptyContext = {
    "source_context": {
      "siblings": [],
      "parents": []
    },
    "target_context": {
      "siblings": [],
      "parents": []
    }
  };

  let context = emptyContext;
  if (contextStr !== "") {
    context = JSON.parse(contextStr);
  }

  let prettyPrintRule = prettyPrintRuleCheckbox.checked;

  data = {
    source1: sourceProgram1,
    source2: sourceProgram2,
    target1: targetProgram1,
    target2: targetProgram2,
    context: context,
    isInsertSecretFn: DEFAULT_PAIRS[DEFAULT_PAIR_IDX].isInsertSecretFn,
    pretty_print_rule: prettyPrintRule
  }

  let rule = await ruleInfAPI_ns.ruleInferenceDebug(data);
  generatedRuleEditorObj.setValue(rule);
}
