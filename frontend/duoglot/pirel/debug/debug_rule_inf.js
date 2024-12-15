// default values for program pair editors
let DEFAULT_PAIRS = [
  // 0. default
  {
    source1: "print()",
    target1: "console.log();",
    source2: "print(1, 'hi')",
    target2: "console.log(1, 'hi');"
  },
  // 1 return type annotation
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
  // 2
  {
    source1: "for i, num in enumerate(nums):\n    secret_fun_4071()",
    target1: "for (let i = 0; i < nums.length; i++) {\n    secret_fun_4071();\n}",
    source2: "for _ in enumerate(_):\n    secret_fun_4071()",
    target2: "for (let _ = 0; _ < nums.length; _++) {\n    secret_fun_4071();\n}",
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
  // 3
  {
    source1: "def f_gold(nums: List[int], x) -> List[int]:\n    return nums",
    target1: "function f_gold(nums, pirel_dummy_var, ) {\n    pirel_dummy_var;\n    pirel_dummy_var;\n}",
    source2: "def f_gold(array: float, x) -> List[int]:\n    return nums",
    target2: "function f_gold(array, pirel_dummy_var, ) {\n    pirel_dummy_var;\n    pirel_dummy_var;\n}",
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
    },
    isInsertSecretFn: false,
  },
];
let DEFAULT_PAIR_IDX = 3;

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

  let data = {
    source1: sourceProgram1,
    source2: sourceProgram2,
    target1: targetProgram1,
    target2: targetProgram2,
    context: context,
    isInsertSecretFn: DEFAULT_PAIRS[DEFAULT_PAIR_IDX].isInsertSecretFn,
    pretty_print_rule: prettyPrintRule
  };

  let kwargs = {
    subject_name: DEFAULT_PAIR_IDX.toString()
  };

  let rule = await ruleInfAPI_ns.ruleInferenceDebug(data, kwargs);
  generatedRuleEditorObj.setValue(rule);
}
