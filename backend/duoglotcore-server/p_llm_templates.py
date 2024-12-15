'''
GUIDELINES:
1. Chat templates are prefixed with `TEMPLATE_`
2. Messages for fill-in tasks are prefixed with `FILLIN_`
3. Messages for translation tasks are prefixed with `TRANSLATION_`
4. Chat templates consist of a combination of various message blocks
'''


from langchain.prompts import ChatPromptTemplate


################################################################################################
########################## MESSAGE BLOCKS FOR FILLIN TASK ######################################
################################################################################################

FILLIN_SYSTEM = (
  'system',
  'You are a world-class software engineer.\n'
  '\n'
  'Your task is to generate SYNTACTICALLY VALID {language} programs as follows:\n'
  '1. I will give you a template\n'
  '2. A template is a {language} program with holes\n'
  '3. A hole is a missing part of a program. Usually, it is a missing identifier or a literal value\n'
  '4. A hole is denoted with double underscores (i.e. `__`)\n'
  '5. Your task is to fill in every hole in such a way that the resulting program is a SYNTACTICALLY VALID {language} program\n'
  '6. You should modify ONLY holes (double underscores `__`). DO NOT change other parts of the template\n'
  '7. Your output should contain ONLY the {language} program with its holes filled in\n'
  '8. Surround the code blocks with triple backticks (```)\n'
)

FILLIN_GOLDEN_CONVERSATION = [
  (
    'human',
    'Fill in the holes in the following {language} program:\n'
    '```\n'
    'for __ in range(len(__)):\n'
    '    print(__)\n'
    '```\n'
    'Remember:\n'
    '1. A hole is denoted with double underscores `__`.\n'
    '2. Generate a syntactically valid {language} program.\n'
    '3. Replace `__` with literal or identifier, and DO NOT change the rest of the code.\n'
  ),
  (
    'ai',
    '```\n'
    'for i in range(len(nums)):\n'
    '    print(i)\n'
    '```\n'
  )
]

FILLIN_PROMPT_BASIC = (
  'human',
  'Remember:\n'
  'A hole is denoted with double underscores `__`.\n'
  'Generate a syntactically valid {language} program.\n'
  'Replace `__` only, and DO NOT change the rest of the code.\n'
  '\n'
  'Fill in the holes in the following {language} program:\n'
  '```\n'
  '{template}\n'
  '```\n'
  '\n'
  '1. Provide {num_variants} different variants to fill in the holes.\n'
  '2. Fill in the holes with the simplest possible code.\n'
  '3. Put each variant in a separate code block.\n'
)

FILLIN_PROMPT_HAS_SECRET = (
  'human',
  'Remember:\n'
  'A hole is denoted with double underscores `__`.\n'
  'Generate a syntactically valid {language} program.\n'
  'Replace `__` only, and DO NOT change the rest of the code.\n'
  '\n'
  'Fill in the holes in the following {language} program:\n'
  '```\n'
  '{template}\n'
  '```\n'
  '\n'
  '1. Provide {num_variants} different variants where holes are filled with identifiers. If a hole is located inside the body of a function definition, a while loop, a for loop, or an if-else statement, fill it with a function invocation `{secret_fn_invocation}`.\n'
  '2. Provide {num_variants} different variants where holes are filled with literals. If a hole is located inside the body of a function definition, a while loop, a for loop, or an if-else statement, fill it with a function invocation `{secret_fn_invocation}`.\n'
  '3. Provide {num_variants} different variants where holes are filled with anything else if identifiers and literals are not suitable. If a hole is located inside the body of a function definition, a while loop, a for loop, or an if-else statement, fill it with a function invocation `{secret_fn_invocation}`.\n'
  '4. Provide {num_variants} different variants where holes are filled with different language elements like function calls, continue statement, break statement, return statement, if statement, lists, dictionaries, objects, etc. where possible. If a hole is located inside the body of a function definition, a while loop, a for loop, or an if-else statement, fill it with a function invocation `{secret_fn_invocation}`.\n'
  '5. Put each variant in a separate code block.\n'
  '6. Code block should contain only the filled template.\n'
  '7. Fill in the holes only. Do not add extra code.\n'
)

FILLIN_PROMPT_NO_SECRET = (
  'human',
  'Remember:\n'
  'A hole is denoted with double underscores `__`.\n'
  'Generate a syntactically valid {language} program.\n'
  'Replace `__` only, and DO NOT change the rest of the code.\n'
  '\n'
  'Fill in the holes in the following {language} program:\n'
  '```\n'
  '{template}\n'
  '```\n'
  '\n'
  '1. Provide {num_variants} different variants where holes are filled with identifiers.\n'
  '2. Provide {num_variants} different variants where holes are filled with literals.\n'
  '3. Provide {num_variants} different variants where holes are filled with anything else if identifiers and literals are not suitable.\n'
  '4. Provide {num_variants} different variants where holes are filled with different language elements like function calls, continue statement, break statement, return statement, if statement, lists, dictionaries, objects, etc. where possible.\n'
  '5. Put each variant in a separate code block.\n'
  '6. Code block should contain only the filled template.\n'
  '7. Fill in the holes only. Do not add extra code.\n'
)


################################################################################################
########################## MESSAGE BLOCKS FOR TRANSLATION TASK #################################
################################################################################################

TRANSLATION_SYSTEM_DIRECT_TRANS = (
  'system',
  'You are a world-class software engineer.\n'
  '\n'
  'Your task is to translate {src_language} programs to semantically equivalent {tar_language} programs as follows:\n'
  '1. Your response should contain ONLY the translated {tar_language} program.\n'
  '2. If some features in {src_language} programming language cannot be translated into {tar_language}, just ignore them and focus on semantic equivalence.\n'
  '3. Surround your output with triple backticks (i.e. \'```\').\n'
)

TRANSLATION_SYSTEM_GENERIC = (
  'system',
  'You are a world-class software engineer.\n'
  '\n'
  'Your task is to generate syntactically valid programs in multiple languages as requested.\n'
)

TRANSLATION_GOLDEN_CONVERSATION_DIRECT_TRANS = [
  (
    'human',
    'Translate the following {src_language} program into a semantically equivalent {tar_language} program:\n'
    '```\n'
    'def f_gold(s: str) -> None:\n'
    '    pass\n'
    '```\n'
  ),
  (
    'ai',
    '```\n'
    'function f_gold(s) {{\n'
    '    return;\n'
    '}}\n'
  ),
  (
    'human',
    'Translate the following {src_language} program into a semantically equivalent {tar_language} program:\n'
    '```\n'
    'def f_gold(s: str) -> int:\n'
    '    pass\n'
    '```\n'
  ),
  (
    'ai',
    '```\n'
    'function f_gold(s) {{\n'
    '}}\n'
    '```\n'
  )
]

TRANSLATION_PROMPT_DIRECT_TRANS = (
  'human',
  'Translate the following {src_language} program into a semantically equivalent {tar_language} program:\n'
  '```{src_language}\n'
  '{program_to_translate}\n'
  '```\n'
  '\n'
  'Generate all possible translations and put each in a separate code block.\n'
)

TRANSLATION_PROMPT_PARTIAL_PROGRAM = (
  'human',
  'The following snippet of {src_language} code\n'
  '```{src_language}\n'
  '{snippet_to_translate}\n'
  '```\n'
  'appears in the following context (in other words, it is a piece of the following larger snippet of {src_language} code)\n'
  '```{src_language}\n'
  '{snippet_context}\n'
  '```\n'
  '\n'
  'Your task is to translate this snippet of {src_language} code\n'
  '```{src_language}\n'
  '{snippet_to_translate}\n'
  '```\n'
  'into a semantically equivalent snippet of {tar_language} code.\n'
  '\n'
  'Put the translation of\n'
  '```{src_language}\n'
  '{snippet_to_translate}\n'
  '```\n'
  'into\n'
  '```{tar_language}\n'
  '{partial_program}\n'
  '```\n'
  'by replacing `{variable_to_replace}` with the translation.\n'
  'Only `{variable_to_replace}` needs to be changed. The rest of the code has to remain untouched.'
)

TRANSLATION_PROMPT_TRANS_SIMILAR = (
  'human',
  'The following {src_language} program\n'
  '```{src_language}\n'
  '{sp1}\n'
  '```\n'
  'can be translated to the following semantically equivalent {tar_language} program\n'
  '```{tar_language}\n'
  '{tp1}\n'
  '```\n'
  '\n'
  'Translate the following {src_language} program\n'
  '```{src_language}\n'
  '{sp2}\n'
  '```\n'
  'to a semantically equivalent {tar_language} program such that its translation is similar to\n'
  '```{tar_language}\n'
  '{tp1}\n'
  '```\n'

)


################################################################################################
########################## CHAT TEMPLATES ######################################################
################################################################################################

TEMPLATE_SIMPLIFICATION = ChatPromptTemplate.from_messages(
  [
    FILLIN_SYSTEM,
    *FILLIN_GOLDEN_CONVERSATION,
    FILLIN_PROMPT_BASIC
  ]
)

TEMPLATE_GENERATION_HAS_SECRET = ChatPromptTemplate.from_messages(
  [
    FILLIN_SYSTEM,
    *FILLIN_GOLDEN_CONVERSATION,
    FILLIN_PROMPT_HAS_SECRET
  ]
)

TEMPLATE_GENERATION_NO_SECRET = ChatPromptTemplate.from_messages(
  [
    FILLIN_SYSTEM,
    *FILLIN_GOLDEN_CONVERSATION,
    FILLIN_PROMPT_NO_SECRET
  ]
)

TEMPLATE_TRANSLATION_DIRECT_TRANS = ChatPromptTemplate.from_messages(
  [
    TRANSLATION_SYSTEM_DIRECT_TRANS,
    *TRANSLATION_GOLDEN_CONVERSATION_DIRECT_TRANS,
    TRANSLATION_PROMPT_DIRECT_TRANS
  ]
)

TEMPLATE_TRANSLATION_PARTIAL_PROGRAM = ChatPromptTemplate.from_messages(
  [
    TRANSLATION_SYSTEM_GENERIC,
    TRANSLATION_PROMPT_PARTIAL_PROGRAM
  ]
)

TEMPLATE_TRANSLATION_TRANS_SIMILAR = ChatPromptTemplate.from_messages(
  [
    TRANSLATION_SYSTEM_GENERIC,
    TRANSLATION_PROMPT_TRANS_SIMILAR
  ]
)
