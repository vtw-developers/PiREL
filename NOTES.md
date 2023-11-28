# Debugging DuoGlot
- https://stackoverflow.com/questions/58491870/unable-to-debug-or-use-pdb-in-django-bdb-bdbquit

## Python (through shell)
### Steps
1. Restart the services if necessary (main-host-start.sh)
2. Set a breakpoint using
   ```python
   __import__("remote_pdb").set_trace(host='0.0.0.0', port=4444)
   ```
3. Invoke a trigger in the frontend (e.g. click "Trans" button) for a function you are debugging
4. Log into the backend Docker container. NOTE: the container name might be different.
   ```bash
   docker exec -ti docker-backend-duoglotcore-1 bash
   ```
5. Run
   ```bash
   telnet 0.0.0.0 4444
   ```
   and start debugging.

### Some notes on debugging
1. In case the debugger does not work, try clearing browser cache.
2. Make sure that you run "cython-izable" Python modules in "interpreted" mode.  
   `INTERPRET_MODE = True` should be used for these purposes in `server_trans.py`.
3. Restart the services if server fails (check terminal).
4. Increase the nginx timeout from 3000 (current) to a higher number (seconds) in `docker/duoglot.nginx.conf`

## Python (VSCode GUI)
- https://github.com/microsoft/debugpy

### Prerequisites
1. Assuming that debugging through shell is working properly (with all necessary port forwarding, etc. set up)

### Steps
1. Import the module:
   ```python
   import debugpy
   ```
2. Put a breakpoint with the following:
   ```python
   debugpy.listen(('0.0.0.0', 4444))
   debugpy.wait_for_client()
   debugpy.breakpoint()
   ```
3. Provoke backend action (so that you hit the breakpoint)
4. Start a debugger in VSCode by hitting F5.
5. Enjoy.

### `launch.json` configuration
```json
{
    "name": "DuoGlot backend: Attach",
    "type": "python",
    "request": "attach",
    "connect": {
        "host": "0.0.0.0",
        "port": 4444
    },
    "pathMappings": [
        {
            "localRoot": "${workspaceFolder}/backend/duoglotcore-server",
            "remoteRoot": "/opt/duoglotcore-server"
        }
    ],
    "justMyCode": true
}
```

## JavaScript
### Steps
1. Open developer window in chrome
2. Go to 'Sources'
3. Refer to https://developer.chrome.com/docs/devtools/javascript/ for more info.

# Internals of Pirel
## Structure of `templatesDict` (example)
```json
{
    "problematic_node_type": "typed_parameter",
    "level-0": {
        "level": 0,
        "template": "__: __",
        "context_node_type": "typed_parameter"
    },
    "level-1": {
        "level": 1,
        "template": "(__: __)",
        "context_node_type": "parameters"
    },
    "level-2": {
        "level": 2,
        "template": "def f_gold(__: __) -> int:\n    i = ans = 0\n    chars = set()\n    for j, c in enumerate(s):\n        while c in chars:\n            chars.remove(s[i])\n            i += 1\n        chars.add(c)\n        ans = max(ans, j - i + 1)\n    return ans",
        "context_node_type": "function_definition"
    },
    "level-3": {
        "level": 3,
        "template": "### lengthOfLongestSubstring \nfrom typing import *\ndef f_gold(__: __) -> int:\n    i = ans = 0\n    chars = set()\n    for j, c in enumerate(s):\n        while c in chars:\n            chars.remove(s[i])\n            i += 1\n        chars.add(c)\n        ans = max(ans, j - i + 1)\n    return ans",
        "context_node_type": "module"
    },
    "levels": 4
}
```

# Internals of DuoGlot (backend)

## `src_ast` and `src_ann` in `server_trans.py`
Tree representation of:
```python
print('hi')
```

is this (in pure `list`, `int`, `str` types) `src_ast`:
```
['py.module',
 0,
 ['py.expression_statement',
  1,
  ['py.call',
   2,
   ['py.identifier', 3, '"print"'],
   ['py.argument_list',
    4,
    '"("',
    ['py.string',
     5,
     ['anno', ['"stype"', '""'], ['"quote"', '"\'"']],
     '"\\""',
     ['py.string_content', 6, '"hi"'],
     '"\\""'],
    '")"']]]]
```

and `src_ann`:
```
{0: [0, 11, (0, 0), (0, 11)],
 1: [0, 11, (0, 0), (0, 11)],
 2: [0, 11, (0, 0), (0, 11)],
 3: [0, 5, (0, 0), (0, 5)],
 4: [5, 11, (0, 5), (0, 11)],
 5: [6, 10, (0, 6), (0, 10)],
 6: [7, 9, (0, 7), (0, 9)]}
```

## `TransSession.expansion_programs` (a.k.a. translation rules)
all types are pure `dict`, `list`, `str`:  
```
[{'expand': ['fragment', ['"js.program"', '"*1"']],
  'match': ['fragment', ['"py.module"', '"*"']],
  'type': 'match_expand'},
 {'expand': ['fragment', ['"js.expression_statement"', '"*1"'], '"*2"'],
  'match': ['fragment', ['"py.expression_statement"', '"*"'], '"*"'],
  'type': 'match_expand'},
 {'expand': ['fragment',
             ['"js.call_expression"',
              ['"js.member_expression"',
               ['"js.identifier"', ['val', '"console"']],
               ['"js.property_identifier"', ['val', '"log"']]],
              '".1"'],
             '"*2"'],
  'match': ['fragment',
            ['"py.call"', ['"py.identifier"', ['val', '"print"']], '"."'],
            '"*"'],
  'type': 'match_expand'},
 {'expand': ['fragment', ['"js.arguments"', '"*1"'], '"*2"'],
  'match': ['fragment', ['"py.argument_list"', '"*"'], '"*"'],
  'type': 'match_expand'},
 {'expand': ['fragment', ['"js.string"', '"*1"'], '"*2"'],
  'match': ['fragment', ['"py.string"', '"*"'], '"*"'],
  'type': 'match_expand'},
 {'expand': ['fragment', ['"js.string_fragment"', '"_val1_"'], '"*1"'],
  'match': ['fragment', ['"py.string_content"', '"_val_"'], '"*"'],
  'type': 'match_expand'}]
```

## `grammar_dlmparser.Slot.range_cursor`
```
Tuple(src_ast,      int,              int)
      range_cursor  range_cursor_idx  ?
```

raw:
```
([['py.module',
   0,
   ['py.expression_statement',
    1,
    ['py.call',
     2,
     ['py.identifier', 3, '"print"'],
     ['py.argument_list',
      4,
      '"("',
      ['py.string',
       5,
       ['anno', ['"stype"', '""'], ['"quote"', '"\'"']],
       '"\\""',
       ['py.string_content', 6, '"hi"'],
       '"\\""'],
      '")"']]]]],
 0,
 1)
```

# Tree-sitter

## Methods of `Node`
```python
__class__
__delattr__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getstate__
__gt__
__hash__
__init__
__init_subclass__
__le__
__lt__
__module__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__setattr__
__sizeof__
__str__
__subclasshook__
child_by_field_id
child_by_field_name
child_count
children
children_by_field_id
children_by_field_name
end_byte
end_point
field_name_for_child
has_changes
has_error
id
is_missing
is_named
named_child_count
named_children
next_named_sibling
next_sibling
parent
prev_named_sibling
prev_sibling
sexp
start_byte
start_point
text
type
walk
```

# Random

## OpenAI API in vanilla JavaScript
```js
// https://community.openai.com/t/communicating-with-the-api-in-vanilla-js-no-server-side-stuff/4984/6
  function OpenaiFetchAPI() {
    console.log("Calling GPT3")
    var url = "https://api.openai.com/v1/chat/completions";
    var bearer = 'Bearer ' + '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'

    var messages = [
      {"role": "system", "content": "You are a software engineer."},
      {"role": "user", "content": "I assume that you are familiar with Tree-sitter and its grammars."},
      {"role": "user", "content": "Generate the smallest Python program, that includes `call_expression` in its abstract syntax tree. \nSurround blocks of code with ``` (triple backticks)."},
    ];

    fetch(url, {
      method: 'POST',
      headers: {
          'Authorization': bearer,
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
          "model": "gpt-3.5-turbo",
          "messages": messages,
          "temperature": 0.7
      })
    }).then(response => {
        return response.json()
    }).then(data=>{
        console.log(data)
        console.log(typeof data)
        console.log(Object.keys(data))
        console.log(data['choices'][0].text)
    }).catch(error => {
        console.log('Something bad happened ' + error)
    });
  }

  async function ruleInferenceHandler(e) {
    console.log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    console.log("starting rule inference");

    var resp = OpenaiFetchAPI();
    console.log(resp);

    // ...
  }
```

## Namespacing in JS
http://michaux.ca/articles/javascript-namespacing

# Prompts
## Skeleton + Holes with `<||>`
```
def <|identifier|>(<|typed_parameter|>):
    <|block|>
```
You are a world-class software engineer. You have a world-class experience with ANTLR grammars. 

You are given a skeleton of a program in Python programming language. The skeleton has missing parts or holes (in software engineering terminology). 

The holes are surrounded with `<|` and `|>` symbols. A hole specifies the name of a starting production rule that is used to generate the code that fills in the hole. 

For example, 
```
<|atom|> = 5
```
can be correctly filled as
```python
num = 5
```
because `num` can be correctly derived from `atom` production rule in ANTLR grammar for Python.

Another example,
```
def foo(a):
    <|if_stmt|>
```
can be correctly filled as
```python
def foo(a):
    if True:
        print('Hello, World')
```
because `if True:\n    print('Hello, World')` can be correctly derived from `if_stmt` production rule in ANTLR grammar for Python. In fact, any random if statement would work in this case. 

Your response should contain only AND only the program with its holes filled. Surround your response with triple backticks (```) as in Markdown. 


## Skeleton + Holes as underscores

### Configuration 1
- Example: `./duoglot/tests/staleetcode/pysep/L0003_LongestSubstringWithoutRepeatingCharacters.py`
- Base rule: `base`

#### `comment`
1. no rule for `comment`
2. manually enter examples
```

##### Translate this function from Python into JavaScript
### Python

# this is a comment
# another comment

### JavaScript

// this is a comment
// another comment


```
```
; examples: "\n##### Translate this function from Python into JavaScript\n### Python\n\n# this is a comment\n# another comment\n\n### JavaScript\n\n// this is a comment\n// another comment\n\n"
; mark: {"source":[[4,0,4,19],[5,0,5,17]],"target":[[9,0,9,20],[10,0,10,18]]}
(match_expand 
  (fragment ("py.comment" "_val_") "*")
  (fragment ("js.comment" "_str0_") "*1")
)
```
3. The above rule does not work, and produces an AssertionError in Expansion class. 
4. changing the rule to the following fixes the issue.
```
; examples: "\n##### Translate this function from Python into JavaScript\n### Python\n\n# this is a comment\n# another comment\n\n### JavaScript\n\n// this is a comment\n// another comment\n\n"
; mark: {"source":[[4,0,4,19],[5,0,5,17]],"target":[[9,0,9,20],[10,0,10,18]]}
(match_expand 
  (fragment ("py.comment" "_val_") "*")
  (fragment "*1")
)
```

#### `import_from_statement`
1. no rule for `import_from_statement`
2. manually enter examples
```

##### Translate this function from Python into JavaScript
### Python

from typing import *

### JavaScript

 

```
3. It looks like it is impossible to learn a rule that allows ignoring a node (try giving empty marks, and there is an error at index_editrule.js:1399:58). But this type of rule can be generated manually:
```
; examples: "\n##### Translate this function from Python into JavaScript\n### Python\n\nfrom typing import *\n\n### JavaScript\n\n;\n\n"
; mark: {"source":[[4,0,4,20]],"target":[[8,0,8,0]]}
(match_expand 
  (fragment ("py.import_from_statement" (str "from") ("py.dotted_name" ("py.identifier" (val "typing"))) (str "import") ("py.wildcard_import" (str "*"))) "*")
  (fragment "*1")
)
```


#### `typed_parameter`
1. no rule for `typed_parameter`
```
s: str
```
2. Here are the hand-crafted examples for rule inference:
```

##### Translate this function from Python into JavaScript
### Python

def f_gold(nums: list):
    pass

def other_fun(arg: int):
    pass

### JavaScript

function f_gold(nums) {
}

function other_fun(arg) {
}

```
3. Here is the rule learned:
```
; examples: "\n##### Translate this function from Python into JavaScript\n### Python\n\ndef f_gold(nums: list):\n    pass\n\ndef other_fun(arg: int):\n    pass\n\n### JavaScript\n\nfunction f_gold(nums) {\n}\n\nfunction other_fun(arg) {\n}\n"
; mark: {"source":[[4,0,5,8],[7,0,8,8]],"target":[[12,0,13,1],[15,0,16,1]]}
(match_expand 
  (fragment ("py.function_definition" (str "def") ("py.identifier" "_val_") ("py.parameters" (str "(") ("py.typed_parameter" ("py.identifier" "_val_") (str ":") ("py.type" ("py.identifier" "_val_"))) (str ")")) (str ":") ("py.block" ("py.pass_statement" (str "pass")))) "*")
  (fragment ("js.function_declaration" (str "function") ("js.identifier" "_val1_") ("js.formal_parameters" (str "(") ("js.identifier" "_val2_") (str ")")) ("js.statement_block" (str "{") (str "}"))) "*1")
)

; expanded as a tree
(fragment 
  ("py.function_definition" 
    (str "def")
    ("py.identifier"
      "_val1_"
    )
    ("py.parameters"
      (str "(")
      ("py.typed_parameter"
        ("py.identifier"
          "_val2_"
        )
        (str ":")
        ("py.type"
          ("py.identifier"
            "_val3_"
          )
        )
      )
      (str ")")
    )
    (str ":")
    ("py.block"
      ("py.pass_statement"
        (str "pass")
      )
    )
  )
  "*1"
)

(fragment
  ("js.function_declaration"
    (str "function")
    ("js.identifier"
      "_val1_"
    )
    ("js.formal_parameters"
      (str "(")
      ("js.identifier"
        "_val2_"
      )
      (str ")")
    )
    ("js.statement_block"
      (str "{")
      (str "}")
    )
  )
  "*1"
)
```
4. The original rule for translating `typed_parameter`s is the following:
```
; examples: "\n##### Translate this function from Python into JavaScript\n### Python\n\ndef f_gold(nums: List[int], target: int) -> List[int]: pass\n\n### JavaScript\n\nfunction f_gold(nums, target) {}\n\n"
; mark: {"source":[[4,11,4,26],[4,28,4,39]],"target":[[8,16,8,20],[8,22,8,28]]}
(match_expand 
  (fragment ("py.typed_parameter" ("py.identifier" "_val_") (str ":") ("py.type" ".")) "*")
  (fragment ("js.identifier" "_val1_") "*2")
)
```
5. The original rule allows ignoring the `typed_parameter` in any context. But in the former case, the context at which `typed_parameter` is applied is `function_definition`.


#### `type`
1. No rule for `type` (type annotation for return type)
2. prompted LLM for generation and translation (refer to type.md)
3. Here are the examples for rule inference:
```

##### Translate this function from Python into JavaScript
### Python

def f_gold(s: str) -> None:
    pass

def f_gold(s: str) -> int:
    pass


### JavaScript

function f_gold(s) {
    return;
}

function f_gold(s) {
    return;
}


```
4. Here is the learned rule:
```
; examples: "\n##### Translate this function from Python into JavaScript\n### Python\n\ndef f_gold(s: str) -> None:\n    pass\n\ndef f_gold(s: str) -> int:\n    pass\n\n\n### JavaScript\n\nfunction f_gold(s) {\n    return;\n}\n\nfunction f_gold(s) {\n    return;\n}\n\n"
; mark: {"source":[[4,0,5,8],[7,0,8,8]],"target":[[13,0,15,1],[17,0,19,1]]}
(match_expand 
  (fragment ("py.function_definition" (str "def") ("py.identifier" (val "f_gold")) ("py.parameters" (str "(") ("py.typed_parameter" ("py.identifier" (val "s")) (str ":") ("py.type" ("py.identifier" (val "str")))) (str ")")) (str "->") ("py.type" ".") (str ":") ("py.block" ("py.pass_statement" (str "pass")))) "*")
  (fragment ("js.function_declaration" (str "function") ("js.identifier" (val "f_gold")) ("js.formal_parameters" (str "(") ("js.identifier" (val "s")) (str ")")) ("js.statement_block" (str "{") ("js.return_statement" (str "return") (str ";")) (str "}"))) "*2")
)

; fragments expanded:
(fragment
  ("py.function_definition"
    (str "def")
    ("py.identifier"
      (val "f_gold")
    )
    ("py.parameters"
      (str "(")
      ("py.typed_parameter"
        ("py.identifier"
          (val "s")
        )
        (str ":")
        ("py.type"
          ("py.identifier"
            (val "str")
          )
        )
      )
      (str ")")
    )
    (str "->")
    ("py.type" ".")
    (str ":")
    ("py.block"
      ("py.pass_statement"
        (str "pass")
      )
    )
  )
  "*"
)


(fragment
  ("js.function_declaration"
    (str "function")
    ("js.identifier"
      (val "f_gold")
    )
    ("js.formal_parameters"
      (str "(")
      ("js.identifier"
        (val "s")
      )
      (str ")")
    )
    ("js.statement_block"
      (str "{")
      ("js.return_statement"
        (str "return")
        (str ";")
      )
      (str "}")
    )
  )
  "*2"
)
```

5. The actual rule that comes with DuoGlot for `type` nodes is:
```
(match_expand 
  (fragment ("py.type" ".") "*")
  (fragment  "*2")
)
```

6. `("py.type" ".")` has no expansion on the target side. Thus, it can be ignored.

#### `for_statement`
1. No rule for `for_statement`
2. This is not an 'inner' node like `typed_parameter` or `type`.
3. How do we know what parts of the code should be templatized?

```py
# original code:
for j, c in enumerate(s):
  pass

# all template variants
for __, __ in __(__):         # all holes
for __, __ in __(s):
for __, __ in enumerate(__):  # best
for __, __ in enumerate(s):

for __, c in __(__):
for __, c in __(s):
for __, c in enumerate(__):
for __, c in enumerate(s):

for j, __ in __(__):
for j, __ in __(s):
for j, __ in enumerate(__):
for j, __ in enumerate(s):

for j, c in __(__):
for j, c in __(s):
for j, c in enumerate(__):
for j, c in enumerate(s):     # worst, original

for __ in __(__):
for __ in __(s):
for __ in enumerate(__):
for __ in enumerate(s):

for __, __ in __:
for __, c in __:
for j, __ in __:
for j, c in __:

for __ in __:                 # the most abstract


# how do we rank templates? ranked:
for __, __ in enumerate(__):
for __, __ in __(__):

for __, __ in __(s):
for __, c in __(__):
for j, __ in __(__):

for __, __ in enumerate(s):

for __, c in enumerate(__):
for j, __ in enumerate(__):

for __, c in enumerate(s):
for j, __ in enumerate(s):

for __, c in __(s):
for j, __ in __(s):

for j, c in __(__):
for j, c in __(s):
for j, c in enumerate(__):


for __ in __(__):
for __, __ in __:

for __ in __(s):
for __ in enumerate(__):
for __ in enumerate(s):

for __, c in __:
for j, __ in __:

for j, c in __:

for __ in __:

for j, c in enumerate(s):
```

4. I think, looking at the rules inferenced from different pairs of programs can give some insight about templatization.
```py
########################### pair 1 #########################

##### Translate this function from Python into JavaScript
### Python

for i,v in enumerate(e):
  pass

for i,v in enumerate(d):
  pass

### JavaScript


for (let i = 0; i < e.length; i++) {

}

for (let i = 0; i < d.length; i++) {

}

# generates the following rule:
; examples: "\n##### Translate this function from Python into JavaScript\n### Python\n\nfor i,v in enumerate(e):\n  pass\n\nfor i,v in enumerate(d):\n  pass\n\n### JavaScript\n\n\nfor (let i = 0; i < e.length; i++) {\n\n}\n\nfor (let i = 0; i < d.length; i++) {\n\n}"
; mark: {"source":[[4,0,5,6],[7,0,8,6]],"target":[[13,0,15,1],[17,0,19,1]]}
(match_expand 
  (fragment ("py.for_statement" (str "for") ("py.pattern_list" ("py.identifier" (val "i")) (str ",") ("py.identifier" (val "v"))) (str "in") ("py.call" ("py.identifier" (val "enumerate")) ("py.argument_list" (str "(") ("py.identifier" "_val_") (str ")"))) (str ":") ("py.block" ("py.pass_statement" (str "pass")))) "*")
  (fragment ("js.for_statement" (str "for") (str "(") ("js.lexical_declaration" (str "let") ("js.variable_declarator" ("js.identifier" (val "i")) (str "=") ("js.number" (val "0"))) (str ";")) ("js.expression_statement" ("js.binary_expression" ("js.identifier" (val "i")) (str "<") ("js.member_expression" ("js.identifier" "_val1_") (str ".") ("js.property_identifier" (val "length")))) (str ";")) ("js.update_expression" ("js.identifier" (val "i")) (str "++")) (str ")") ("js.statement_block" (str "{") (str "}"))) "*1")
)

# as can be seen from the generated rule, the `i` and `v` are hard-coded (overfitted)
# thus, the pairs of programs should differ in `pattern_list` node (i.e. `i,v`)

############################# pair 2 #############################

##### Translate this function from Python into JavaScript
### Python

for i,v in enumerate(e):
  pass

for j,val in enumerate(d):
  pass

### JavaScript


for (let i = 0; i < e.length; i++) {

}

for (let j = 0; j < d.length; j++) {

}

# generates the following rule:
; examples: "\n##### Translate this function from Python into JavaScript\n### Python\n\nfor i,v in enumerate(e):\n  pass\n\nfor j,val in enumerate(d):\n  pass\n\n### JavaScript\n\n\nfor (let i = 0; i < e.length; i++) {\n\n}\n\nfor (let j = 0; j < d.length; j++) {\n\n}"
; mark: {"source":[[4,0,5,6],[7,0,8,6]],"target":[[13,0,15,1],[17,0,19,1]]}
(match_expand 
  (fragment ("py.for_statement" (str "for") ("py.pattern_list" ("py.identifier" "_val_") (str ",") ("py.identifier" "_val_")) (str "in") ("py.call" ("py.identifier" (val "enumerate")) ("py.argument_list" (str "(") ("py.identifier" "_val_") (str ")"))) (str ":") ("py.block" ("py.pass_statement" (str "pass")))) "*")
  (fragment ("js.for_statement" (str "for") (str "(") ("js.lexical_declaration" (str "let") ("js.variable_declarator" ("js.identifier" "_val1_") (str "=") ("js.number" (val "0"))) (str ";")) ("js.expression_statement" ("js.binary_expression" ("js.identifier" "_val1_") (str "<") ("js.member_expression" ("js.identifier" "_val3_") (str ".") ("js.property_identifier" (val "length")))) (str ";")) ("js.update_expression" ("js.identifier" "_val1_") (str "++")) (str ")") ("js.statement_block" (str "{") (str "}"))) "*1")
)

# generated rule overfits to function body

############################# pair 3 #############################

##### Translate this function from Python into JavaScript
### Python

for i,v in enumerate(e):
  pass

for j,val in enumerate(d):
  print('hi')

### JavaScript


for (let i = 0; i < e.length; i++) {

}

for (let j = 0; j < d.length; j++) {
    console.log('hi');
}

# generates the following rule:
; examples: "\n##### Translate this function from Python into JavaScript\n### Python\n\nfor i,v in enumerate(e):\n  pass\n\nfor j,val in enumerate(d):\n  print('hi')\n\n### JavaScript\n\n\nfor (let i = 0; i < e.length; i++) {\n\n}\n\nfor (let j = 0; j < d.length; j++) {\n    console.log('hi');\n}"
; mark: {"source":[[4,0,5,6],[7,0,8,13]],"target":[[13,0,15,1],[17,0,19,1]]}
(match_expand 
  (fragment ("py.for_statement" (str "for") ("py.pattern_list" ("py.identifier" "_val_") (str ",") ("py.identifier" "_val_")) (str "in") ("py.call" ("py.identifier" (val "enumerate")) ("py.argument_list" (str "(") ("py.identifier" "_val_") (str ")"))) (str ":") ("py.block" ".")) "*")
  (fragment ("js.for_statement" (str "for") (str "(") ("js.lexical_declaration" (str "let") ("js.variable_declarator" ("js.identifier" "_val1_") (str "=") ("js.number" (val "0"))) (str ";")) ("js.expression_statement" ("js.binary_expression" ("js.identifier" "_val1_") (str "<") ("js.member_expression" ("js.identifier" "_val3_") (str ".") ("js.property_identifier" (val "length")))) (str ";")) ("js.update_expression" ("js.identifier" "_val1_") (str "++")) (str ")") ("js.statement_block" (str "{") "*1")) "*2")
)

# this one doesn't close the body of the for loop with closing curly brace (i.e. '}')


############################# pair 4 #############################

##### Translate this function from Python into JavaScript
### Python

for i,v in enumerate(e):
  foo()

for j,val in enumerate(d):
  print('hi')

### JavaScript


for (let i = 0; i < e.length; i++) {
    foo();
}

for (let j = 0; j < d.length; j++) {
    console.log('hi');
}

# i think this pair actually breaks rule inference
; examples: "\n##### Translate this function from Python into JavaScript\n### Python\n\nfor i,v in enumerate(e):\n  foo()\n\nfor j,val in enumerate(d):\n  print('hi')\n\n### JavaScript\n\n\nfor (let i = 0; i < e.length; i++) {\n    foo();\n}\n\nfor (let j = 0; j < d.length; j++) {\n    console.log('hi');\n}"
; mark: {"source":[[4,0,5,7],[7,0,8,13]],"target":[[13,0,15,1],[17,0,19,1]]}
(match_expand 
  (fragment ("py.for_statement" (str "for") ("py.pattern_list" ("py.identifier" "_val_") (str ",") ("py.identifier" "_val_")) (str "in") ("py.call" ("py.identifier" (val "enumerate")) ("py.argument_list" (str "(") ("py.identifier" "_val_") (str ")"))) (str ":") ("py.block" ("py.expression_statement" ("py.call" ("py.identifier" "_val_") ("py.argument_list" (str "(") "*"))))) "*")
  (fragment ("js.for_statement" (str "for") (str "(") ("js.lexical_declaration" (str "let") ("js.variable_declarator" ("js.identifier" "_val1_") (str "=") ("js.number" (val "0"))) (str ";")) ("js.expression_statement" ("js.binary_expression" ("js.identifier" "_val1_") (str "<") ("js.member_expression" ("js.identifier" "_val3_") (str ".") ("js.property_identifier" (val "length")))) (str ";")) ("js.update_expression" ("js.identifier" "_val1_") (str "++")) (str ")") ("js.statement_block" (str "{") ("js.expression_statement" ("js.call_expression" ".2" ("js.arguments" (str "(") "*1")) (str ";")) (str "}"))) "*2")
)

# if you look carefully, we don't actually have a capture for `"js.call_expression" ".2"`
# moreover, the closing parenthesis is missing in `("py.argument_list" (str "(") "*")`

############################# pair 5 #############################

##### Translate this function from Python into JavaScript
### Python

for i,v in enumerate(e):
  a = 4

for j,val in enumerate(d):
  print('hi')

### JavaScript


for (let i = 0; i < e.length; i++) {
    let a = 4;
}

for (let j = 0; j < d.length; j++) {
    console.log('hi');
}

# gives the following rule
; examples: "\n##### Translate this function from Python into JavaScript\n### Python\n\nfor i,v in enumerate(e):\n  a = 4\n\nfor j,val in enumerate(d):\n  print('hi')\n\n### JavaScript\n\n\nfor (let i = 0; i < e.length; i++) {\n    let a = 4;\n}\n\nfor (let j = 0; j < d.length; j++) {\n    console.log('hi');\n}"
; mark: {"source":[[4,0,5,7],[7,0,8,13]],"target":[[13,0,15,1],[17,0,19,1]]}
(match_expand 
  (fragment ("py.for_statement" (str "for") ("py.pattern_list" ("py.identifier" "_val_") (str ",") ("py.identifier" "_val_")) (str "in") ("py.call" ("py.identifier" (val "enumerate")) ("py.argument_list" (str "(") ("py.identifier" "_val_") (str ")"))) (str ":") ("py.block" ("py.expression_statement" "."))) "*")
  (fragment ("js.for_statement" (str "for") (str "(") ("js.lexical_declaration" (str "let") ("js.variable_declarator" ("js.identifier" "_val1_") (str "=") ("js.number" (val "0"))) (str ";")) ("js.expression_statement" ("js.binary_expression" ("js.identifier" "_val1_") (str "<") ("js.member_expression" ("js.identifier" "_val3_") (str ".") ("js.property_identifier" (val "length")))) (str ";")) ("js.update_expression" ("js.identifier" "_val1_") (str "++")) (str ")") ("js.statement_block" (str "{") ".1" (str "}"))) "*2")
)

# this rule is not correct, because it overfit to a single `expression_statement` node

############################# pair 6 #############################


##### Translate this function from Python into JavaScript
### Python

for i,v in enumerate(e):
  a = 4
  b = 5

for j,val in enumerate(d):
  print('hi')

### JavaScript


for (let i = 0; i < e.length; i++) {
    let a = 4;
    let b = 5;
}

for (let j = 0; j < d.length; j++) {
    console.log('hi');
}

# generates the following rule
; examples: "\n##### Translate this function from Python into JavaScript\n### Python\n\nfor i,v in enumerate(e):\n  a = 4\n  b = 5\n\nfor j,val in enumerate(d):\n  print('hi')\n\n### JavaScript\n\n\nfor (let i = 0; i < e.length; i++) {\n    let a = 4;\n    let b = 5;\n}\n\nfor (let j = 0; j < d.length; j++) {\n    console.log('hi');\n}"
; mark: {"source":[[4,0,6,7],[8,0,9,13]],"target":[[14,0,17,1],[19,0,21,1]]}
(match_expand 
  (fragment ("py.for_statement" (str "for") ("py.pattern_list" ("py.identifier" "_val_") (str ",") ("py.identifier" "_val_")) (str "in") ("py.call" ("py.identifier" (val "enumerate")) ("py.argument_list" (str "(") ("py.identifier" "_val_") (str ")"))) (str ":") ("py.block" ("py.expression_statement" ".") ERROR_UNEXPECTED_NON_ARRAY_CHILD)) "*")
  (fragment ("js.for_statement" (str "for") (str "(") ("js.lexical_declaration" (str "let") ("js.variable_declarator" ("js.identifier" "_val1_") (str "=") ("js.number" (val "0"))) (str ";")) ("js.expression_statement" ("js.binary_expression" ("js.identifier" "_val1_") (str "<") ("js.member_expression" ("js.identifier" "_val3_") (str ".") ("js.property_identifier" (val "length")))) (str ";")) ("js.update_expression" ("js.identifier" "_val1_") (str "++")) (str ")") ("js.statement_block" (str "{") ".1" "*1")) "*2")
)

# this rule is buggy due to `ERROR_UNEXPECTED_NON_ARRAY_CHILD`


```

5. Actually, we want to keep `enumerate` (i.e. we don't want to convert it into a hole). Because, it is a built-in function.

## V4 text
### system
You are a world-class software engineer.

Your task is to generate SYNTACTICALLY VALID Python programs as follows:
1. I will give you a Python program with holes (placeholders).
2. A hole is a missing part of a program. Usually, it is an identifier or a literal value.
3. A hole is denoted with double underscores (i.e. `__`)
4. Your task is to fill in every hole in such a way that the resulting program is a SYNTACTICALLY VALID Python program.
5. DO NOT ADD any other extra code. FILL IN THE HOLES ONLY.
6. You should modify ONLY holes (double underscores `__`). DO NOT change other parts of the program.

Your output should contain ONLY the Python program with its holes filled in.
Surround the code blocks with triple backticks (```).

### user
Fill in the holes in the following Python program:
```
for __ in range(len(__)):
    print(__)
```
Remember:
1. A hole is denoted with double underscores `__`.
2. Generate a syntactically valid Python program.
3. Replace `__` with something, and DO NOT change the rest of the code.

### assistant
```
for i in range(len(nums)):
    print(i)
```

### user
Fill in the holes in the following Python program:
```
def fgold(__: __):
    pass
```
Remember:
1. A hole is denoted with double underscores `__`.
2. Generate a syntactically valid Python program.
3. Replace `__` with something, and DO NOT change the rest of the code.

### assistant
```
def fgold(arg1: int):
    pass
```

# Useful stuff
## Links
- LangChain https://js.langchain.com/docs/getting-started/guide-llm
  https://github.com/hwchase17/langchainjs/releases/tag/0.0.96
- OpenAI cookbook https://github.com/openai/openai-cookbook
- 