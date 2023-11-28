// namespace for API
var tmplns = {};

// ==============================================================================
// ================= UTILS ======================================================
// ==============================================================================
tmplns.utils = {
  enumerateStr: function(strList, start = 1) {
    let result = "";
    for (let i = 0; i < strList.length; i++) {
      result += `${i+start}. ${strList[i]}\n`
    }
    return result.trim();
  },
  textToCodeBlock: function(text, lang = "") {
    return "```" + lang + "\n" + text + "\n" + "```"
  },
  getRandomSubarray: function (arr, size) {
    var shuffled = arr.slice(0), i = arr.length, temp, index;
    while (i--) {
        index = Math.floor((i + 1) * Math.random());
        temp = shuffled[index];
        shuffled[index] = shuffled[i];
        shuffled[i] = temp;
    }
    return shuffled.slice(0, size);
  },
};

// ==============================================================================
// ================= SYSTEM CONTENTS (LIBRARY) ==================================
// ==============================================================================
tmplns.libsyscont = {
  filling: {
    getTaskStr: function(language) {
      return `Your task is to generate SYNTACTICALLY VALID ${language} programs as follows:`
    },
    getFooter: function(language) {
      let rulesList = [
        `I will give you a template`,
        `A template is a ${language} program with holes`,
        `A hole is a missing part of a program. Usually, it is a missing identifier or a literal value`,
        `A hole is denoted with double underscores (i.e. \`__\`)`,
        `Your task is to fill in every hole in such a way that the resulting program is a SYNTACTICALLY VALID ${language} program`,
        `You should modify ONLY holes (double underscores \`__\`). DO NOT change other parts of the template`,
        `Your output should contain ONLY the ${language} program with its holes filled in`,
        `Surround the code blocks with triple backticks (\`\`\`)`,
      ];
      return tmplns.utils.enumerateStr(rulesList);
    },
  },
  translation: {
    getTaskStr: function(sourceLanguage, targetLanguage) {
      return `Your task is to translate ${sourceLanguage} programs to semantically equivalent ${targetLanguage} programs as follows:`
    },
    getFooter: function(sourceLanguage, targetLanguage) {
      let rulesList = [
        `Your response should contain ONLY the translated ${targetLanguage} program.`,
        `If some features in ${sourceLanguage} programming language cannot be translated into ${targetLanguage}, just ignore them and focus on semantic equivalence.`,
        `Surround your output with triple backticks (i.e. '\`\`\`').`,
      ];
      return tmplns.utils.enumerateStr(rulesList);
    },
  },
  transSimilar: {
    taskStr: "Your task is to generate syntactically valid programs in multiple languages as requested."
  },
  combine: function(header, task, footer) {
    let result = "";
    result += header;
    result += "\n\n";
    result += task;
    if (footer !== null) {
      result += "\n";
      result += footer;
    }
    return result.trim();
  },

  header: "You are a world-class software engineer.",
};

// ==============================================================================
// ================= GOLD CONVERSATION (LIBRARY) ================================
// ==============================================================================
tmplns.libgoldconv = {
  filling: {
    task: "Fill in the holes in the following Python program:",
    footerNotes: [
      "A hole is denoted with double underscores \`__\`.",
      "Generate a syntactically valid Python program.",
      "Replace \`__\` with literal or identifier, and DO NOT change the rest of the code.",
    ],
    dialogUnits: [
      {
        user: [
          "for __ in range(len(__)):",
          "    print(__)"
        ],
        assistant: [
          "for i in range(len(nums)):",
          "    print(i)"
        ]
      },
      {
        user: [
          "def fgold(__: __):",
          "    pass"
        ],
        assistant: [
          "def fgold(arg1: int):",
          "    pass"
        ]
      }
    ],
  },
  translation: {
    task: "Translate the following Python program into a semantically equivalent JavaScript program:",
    dialogUnits: [
      {
        user: [
          "def f_gold(s: str) -> None:",
          "    pass"
        ],
        assistant: [
          "function f_gold(s) {",
          "    return;",
          "}",
        ]
      },
      {
        user: [
          "def f_gold(s: str) -> int:",
          "    pass"
        ],
        assistant: [
          "function f_gold(s) {",
          "}"
        ]
      }
    ],
    footerNotes: [

    ]
  },
  sample: function(task, footerNotes, dialogUnits, size) {
    let dialogUnitsSample = tmplns.utils.getRandomSubarray(dialogUnits, size);
    let goldConversation = [];
    for (let dialogUnit of dialogUnitsSample) {
      // user content
      let userContent = "";
      userContent += task;
      userContent += "\n";
      userContent += tmplns.utils.textToCodeBlock(dialogUnit.user.join("\n"));
      if (footerNotes.length > 0) {
        userContent += "\nRemember:\n";
        userContent += tmplns.utils.enumerateStr(footerNotes);
      }
      let userDict = {
        role: "user",
        content: userContent
      };
      let assistantDict = {
        role: "assistant",
        content: tmplns.utils.textToCodeBlock(dialogUnit.assistant.join("\n"))
      }
      goldConversation.push(userDict);
      goldConversation.push(assistantDict);
    }
    return goldConversation;
  },
};

// ==============================================================================
// ================= PROMPTS (LIBRARY) ==========================================
// ==============================================================================
tmplns.libprompts = {
  filling: {
    headerNotes: [
      "A hole is denoted with double underscores \`__\`.",
      "Generate a syntactically valid Python program.",
      "Replace \`__\` only, and DO NOT change the rest of the code.",
    ],
    task: "Fill in the hole in the following Python program:",
    footerNotes01: function(numSamplesInSingleResponse) {
      let footerLines = [
        `Provide ${numSamplesInSingleResponse} different variants to fill in the holes.`,
        "Fill in the holes with the simplest possible code.",
        "Put each variant in a separate code block.",
      ]
      return footerLines;
    },
    footerNotes02: function(numSamplesInSingleResponse) {
      let footerLines = [
        `Provide ${numSamplesInSingleResponse} different variants where holes are filled with identifiers.`,
        `Provide ${numSamplesInSingleResponse} different variants where holes are filled with literals.`,
        `Provide ${numSamplesInSingleResponse} different variants where holes are filled with anything else if identifiers and literals are not suitable.`,
        `Provide ${numSamplesInSingleResponse} different variants where holes are filled with different language elements like function calls, continue statement, break statement, return statement, if statement, lists, dictionaries, objects, etc. where possible.`,
        "Put each variant in a separate code block.",
        "Code block should contain only the filled template.",
      ]
      return footerLines;
    },
    footerNotes03: function(numSamplesInSingleResponse) {
      let note = `If a hole is located inside the body of a function definition, a while loop, a for loop, or an if-else statement, fill it with a function invocation \`${consts_ns.SECRET_FUN}()\``;
      let footerLines = [
        `Provide ${numSamplesInSingleResponse} different variants where holes are filled with identifiers. ${note}.`,
        `Provide ${numSamplesInSingleResponse} different variants where holes are filled with literals. ${note}.`,
        `Provide ${numSamplesInSingleResponse} different variants where holes are filled with anything else if identifiers and literals are not suitable. ${note}.`,
        `Provide ${numSamplesInSingleResponse} different variants where holes are filled with different language elements like function calls, continue statement, break statement, return statement, if statement, lists, dictionaries, objects, etc. where possible. ${note}.`,
        "Put each variant in a separate code block.",
        "Code block should contain only the filled template.",
        "Fill in the holes only. Do not add extra code.",
      ]
      return footerLines;
    },
    getTask: function(taskStr, template) {
      let result = "";
      result += taskStr;
      result += "\n";
      result += tmplns.utils.textToCodeBlock(template.trim());
      return result;
    }
  },
  translation: {
    getTaskStr: function(sourceLanguage, targetLanguage) {
      return `Translate the following ${sourceLanguage} program into a semantically equivalent ${targetLanguage} program:`;
    },
    getTask: function(taskStr, sourceLanguage, programToTranslate) {
      let result = "";
      result += taskStr;
      result += "\n";
      result += tmplns.utils.textToCodeBlock(programToTranslate, sourceLanguage);
      return result;
    },
    footerNotes: "Generate all possible translations and put each in a separate code block.",
  },
  transSimilar: {
    getTaskStr: function(prg2trans, refTar, sourceLanguage, targetLanguage) {
      let result = "";
      result += `Translate the following ${sourceLanguage} program`;
      result += "\n";
      result += tmplns.utils.textToCodeBlock(prg2trans, sourceLanguage);
      result += "\n";
      result += `to a semantically equivalent ${targetLanguage} program such that its translation is similar to`;
      result += "\n";
      result += tmplns.utils.textToCodeBlock(refTar, targetLanguage);
      return result;
    },
    getTask: function(taskStr, refSrc, refTar, sourceLanguage, targetLanguage) {
      let result = "";
      result += `The following ${sourceLanguage} program`;
      result += "\n";
      result += tmplns.utils.textToCodeBlock(refSrc, sourceLanguage);
      result += "\n";
      result += `can be translated to the following semantically equivalent ${targetLanguage} program`;
      result += "\n";
      result += tmplns.utils.textToCodeBlock(refTar, targetLanguage);
      result += "\n";
      result += "\n";
      result += taskStr;
      return result.trim();
    }
  },
  getHeaderNotes: function(noteList) {
    let result = "";
    result += "Remember:\n";
    result += noteList.join("\n");
    return result;
  },
  getFooterNotes: function(noteList) {
    let result = "";
    result += tmplns.utils.enumerateStr(noteList);
    return result;
  },
};

// ==============================================================================
// ================= TEMPLATES FOR SIMPLIFICATION ===============================
// ==============================================================================
tmplns.simplification = {

  getSystemContent: function(lang) {
    let language = consts_ns.LANG_DICT[lang];
    let systemContent = tmplns.libsyscont.combine(
      tmplns.libsyscont.header,
      tmplns.libsyscont.filling.getTaskStr(language),
      tmplns.libsyscont.filling.getFooter(language),
    );
    return systemContent;
  },

  getGoldConversation: function(size) {
    return tmplns.libgoldconv.sample(
      tmplns.libgoldconv.filling.task,
      tmplns.libgoldconv.filling.footerNotes,
      tmplns.libgoldconv.filling.dialogUnits,
      size
    );
  },

  getPrompt_PY: function (template, numSamplesInSingleResponse) {
    let prompt = "";
    prompt += tmplns.libprompts.getHeaderNotes(tmplns.libprompts.filling.headerNotes);
    prompt += "\n\n";
    prompt += tmplns.libprompts.filling.getTask(tmplns.libprompts.filling.task, template);
    prompt += "\n\n";
    prompt += tmplns.libprompts.getFooterNotes(tmplns.libprompts.filling.footerNotes01(numSamplesInSingleResponse));
    return prompt.trim();
  },
};

// ==============================================================================
// ================= TEMPLATES FOR PROGRAM GENERATION (TEMPLATE FILLING) ========
// ==============================================================================
tmplns.generation = {

  getSystemContent: function(lang) {
    let language = consts_ns.LANG_DICT[lang];
    let systemContent = tmplns.libsyscont.combine(
      tmplns.libsyscont.header,
      tmplns.libsyscont.filling.getTaskStr(language),
      tmplns.libsyscont.filling.getFooter(language),
    );
    return systemContent;
  },

  getGoldConversation: function(size) {
    return tmplns.libgoldconv.sample(
      tmplns.libgoldconv.filling.task,
      tmplns.libgoldconv.filling.footerNotes,
      tmplns.libgoldconv.filling.dialogUnits,
      size
    );
  },

  getPrompt_PY: function (template, numSamplesInSingleResponse) {
    let prompt = "";
    prompt += tmplns.libprompts.getHeaderNotes(tmplns.libprompts.filling.headerNotes);
    prompt += "\n\n";
    prompt += tmplns.libprompts.filling.getTask(tmplns.libprompts.filling.task, template);
    prompt += "\n\n";
    prompt += tmplns.libprompts.getFooterNotes(tmplns.libprompts.filling.footerNotes02(numSamplesInSingleResponse));
    return prompt.trim();
  },

  getPrompt_secret_PY: function (template, numSamplesInSingleResponse) {
    let prompt = "";
    prompt += tmplns.libprompts.getHeaderNotes(tmplns.libprompts.filling.headerNotes);
    prompt += "\n\n";
    prompt += tmplns.libprompts.filling.getTask(tmplns.libprompts.filling.task, template);
    prompt += "\n\n";
    prompt += tmplns.libprompts.getFooterNotes(tmplns.libprompts.filling.footerNotes03(numSamplesInSingleResponse));
    return prompt.trim();
  },
};

// ==============================================================================
// ================= TEMPLATES FOR PROGRAM TRANSLATION ==========================
// ==============================================================================
tmplns.translation = {

  getSystemContent: function (srcLang, tarLang) {
    let sourceLanguage = consts_ns.LANG_DICT[srcLang];
    let targetLanguage = consts_ns.LANG_DICT[tarLang];

    let systemContent = tmplns.libsyscont.combine(
      tmplns.libsyscont.header,
      tmplns.libsyscont.translation.getTaskStr(sourceLanguage, targetLanguage),
      tmplns.libsyscont.translation.getFooter(sourceLanguage, targetLanguage),
    );

    return systemContent;
  },

  getGoldConversation: function(size) {
    return tmplns.libgoldconv.sample(
      tmplns.libgoldconv.translation.task,
      tmplns.libgoldconv.translation.footerNotes,
      tmplns.libgoldconv.translation.dialogUnits,
      size
    );
  },

  getPrompt: function (programToTranslate, srcLang, tarLang) {
    let sourceLanguage = consts_ns.LANG_DICT[srcLang];
    let targetLanguage = consts_ns.LANG_DICT[tarLang];

    let prompt = "";
    prompt += tmplns.libprompts.translation.getTask(
      tmplns.libprompts.translation.getTaskStr(sourceLanguage, targetLanguage),
      sourceLanguage,
      programToTranslate
    );
    prompt += "\n\n";
    prompt += tmplns.libprompts.translation.footerNotes;
    return prompt.trim();
  },
};

// ==============================================================================
// ================= TEMPLATES FOR OBTAINING SIMILAR TRANSLATION ================
// ==============================================================================
tmplns.transSimilar = {

  getSystemContent: function () {
    let systemContent = tmplns.libsyscont.combine(
      tmplns.libsyscont.header,
      tmplns.libsyscont.transSimilar.taskStr,
      null,
    );

    return systemContent;
  },

  getPrompt: function (prg2trans, refSrc, refTar, srcLang, tarLang) {
    let sourceLanguage = consts_ns.LANG_DICT[srcLang];
    let targetLanguage = consts_ns.LANG_DICT[tarLang];

    let prompt = "";
    prompt += tmplns.libprompts.transSimilar.getTask(
      tmplns.libprompts.transSimilar.getTaskStr(prg2trans, refTar, sourceLanguage, targetLanguage),
      refSrc,
      refTar,
      sourceLanguage,
      targetLanguage
    );
    return prompt.trim();
  },
};


// ==============================================================================
// ================= TESTING PROMPT TEMPLATES ===================================
// ==============================================================================

tmplns._testSimplification = function() {
  let template = "__ = __";
  let system = tmplns.simplification.getSystemContent("py");
  let goldConversation = tmplns.simplification.getGoldConversation(2);
  let prompt = tmplns.simplification.getPrompt_PY(template, 5);
  let messages = [
    {
      role: "system",
      content: system
    },
    ...goldConversation,
    {
      role: "user",
      content: prompt
    }
  ];
  for (let message of messages) {
    console.log(message["role"].toUpperCase());
    console.log(message["content"]);
    console.log("\n");
  }
};

tmplns._testGeneration = function() {
  let template = "if __:\n    __";
  let system = tmplns.generation.getSystemContent("py");
  let goldConversation = tmplns.generation.getGoldConversation(2);
  let prompt = tmplns.generation.getPrompt_secret_PY(template, 5);
  let messages = [
    {
      role: "system",
      content: system
    },
    ...goldConversation,
    {
      role: "user",
      content: prompt
    }
  ];
  for (let message of messages) {
    console.log(message["role"].toUpperCase());
    console.log(message["content"]);
    console.log("\n");
  }
};

tmplns._testTranslation = function() {
  let programToTranslate = "midVal1 = arr[i] if i < m else arr[i + 1]";
  let srcLang = "py";
  let tarLang = "js";
  let system = tmplns.translation.getSystemContent(srcLang, tarLang);
  let goldConversation = tmplns.translation.getGoldConversation(2);
  let prompt = tmplns.translation.getPrompt(programToTranslate, srcLang, tarLang);
  let messages = [
    {
      role: "system",
      content: system
    },
    ...goldConversation,
    {
      role: "user",
      content: prompt
    }
  ];
  for (let message of messages) {
    console.log(message["role"].toUpperCase());
    console.log(message["content"]);
    console.log("\n");
  }
};

tmplns._testTransSimilar = function() {
  let refSrc = "midVal1 = 0 if a + b - 1 < m else 1";
  let refTar = "let midVal1 = ((a + (b - 1)) < m) ? 0 : 1";
  let srcLang = "py";
  let tarLang = "js";
  let programToTranslate = "midVal1 = 0 if k + asdf - 1 < m else 1";

  let system = tmplns.transSimilar.getSystemContent();
  let prompt = tmplns.transSimilar.getPrompt(programToTranslate, refSrc, refTar, srcLang, tarLang);
  let messages = [
    {
      role: "system",
      content: system
    },
    {
      role: "user",
      content: prompt
    }
  ];
  for (let message of messages) {
    console.log(message["role"].toUpperCase());
    console.log(message["content"]);
    console.log("\n");
  }
};

// `node prompt_templates.js` to run
// everything below should be commented when not testing
// let consts_ns = {};
// consts_ns.LANG_DICT = {
//   py: "Python",
//   js: "JavaScript",
// };
// consts_ns.SECRET_FUN = "secret_fun_4071";
// console.log("\n\n\n~~~~~~~~~~ _testSimplification");
// tmplns._testSimplification();
// console.log("\n\n\n~~~~~~~~~~ _testGeneration");
// tmplns._testGeneration();
// console.log("\n\n\n~~~~~~~~~~ _testTranslation");
// tmplns._testTranslation();
// console.log("\n\n\n~~~~~~~~~~ _testTransSimilar");
// tmplns._testTransSimilar();
