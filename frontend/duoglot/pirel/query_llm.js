// namespace for API
var queryAPI_ns = {};

function log() {
  console.log(arguments);
}

// ==============================================================================
// ================= MANIPULATING GENERATION STATE ==============================
// ==============================================================================

/**
 * genState = {
 *   template_id=0: {},
 *   ...
 * }
*/
queryAPI_ns.getEmptyState = function () {
  return {};
};

/**
 * namespace global object to keep relevant data pertaining to
 * a pair generation conversation
*/
queryAPI_ns.generationState = queryAPI_ns.getEmptyState();

// ==============================================================================
// ================= CACHING ====================================================
// ==============================================================================

/**
 * https://stackoverflow.com/a/7616484
*/
String.prototype.hashCode = function() {
  var hash = 0,
    i, chr;
  if (this.length === 0) return hash;
  for (i = 0; i < this.length; i++) {
    chr = this.charCodeAt(i);
    hash = ((hash << 5) - hash) + chr;
    hash |= 0; // Convert to 32bit integer
  }
  return hash;
}

/**
 * CACHE FORMAT:
 * pirel/cache/translation-pairs-####.json = {
 *   source_lang: str,
 *   target_lang: str,
 *   template: str,
 *   template_origin: str,
 *   templatized_node_ids: List,
 *   translation_pairs: [
 *     [
 *       {source: source_prog, target: target_prog},
 *       {source: source_prog, target: target_prog}
 *     ],
 *     [
 *       {source: source_prog, target: target_prog},
 *       {source: source_prog, target: target_prog}
 *     ],
 *     ...
 *   ]
 * }
 *
 * pirel/cache/code-blocks-####.json = {
 *   template: str,
 *   lang: str,
 *   temperature: float,
 *   code_blocks: [
 *     str,
 *     ...
 *   ],
 *   num_code_blocks: int
 * }
 *
 * pirel/cache/translations-####.json = {
 *   template: str,
 *   source_lang: str,
 *   target_lang: str,
 *   template_origin: str,
 *   translations: {
 *     source_program: [
 *       str,
 *       ...
 *     ],
 *     ...
 *   }
 * }
 *
 * TODO move consts to consts.js
*/
queryAPI_ns.cache = {
  // return n cached translation pairs or null
  getCachedTranslationPairs: async function (srcLang, tarLang, templateDict, n) {
    let cacheData = await queryAPI_ns.cache._transPairsLoad(srcLang, tarLang, templateDict);
    if (cacheData === null) { return null; }
    let cachedTranslationPairs = cacheData["translation_pairs"];
    if (cachedTranslationPairs.length < n) { return null; }
    return cachedTranslationPairs.slice(0, n);
  },

  updateTranslationPairsCache: async function (srcLang, tarLang, templateDict, translationPairs) {
    let cacheData = await queryAPI_ns.cache._transPairsLoad(srcLang, tarLang, templateDict);
    if (cacheData !== null) {
      await queryAPI_ns.cache._transPairsAppend(cacheData, translationPairs);
    } else {
      await queryAPI_ns.cache._transPairsCreate(srcLang, tarLang, templateDict, translationPairs);
    }
  },

  // return data if exists
  _transPairsLoad: async function (srcLang, tarLang, templateDict) {
    let template = templateDict["template"];
    let filePath = this._transPairsGetFilePath(srcLang, tarLang, template);
    let dataStr = await utils_ns.readFileFromDataDir(filePath);
    if (dataStr === null) {
      return null;
    }
    let data = JSON.parse(dataStr);
    return data;
  },

  _transPairsCreate: async function (srcLang, tarLang, templateDict, translationPairs) {
    let data = {
      source_lang: srcLang,
      target_lang: tarLang,
      template: templateDict["template"],
      template_origin: templateDict["template_origin"],
      templatized_node_ids: templateDict["templatized_node_ids"],
      translation_pairs: translationPairs
    };
    let filePath = this._transPairsGetFilePath(srcLang, tarLang, templateDict);
    let result = await utils_ns.writeFileToDataDirMakedirs(filePath, JSON.stringify(data));
    return result;
  },

  _transPairsAppend: async function(data, translationPairs) {
    data["translation_pairs"].push(...translationPairs);
    let filePath = this._transPairsGetFilePath(data["source_lang"], data["target_lang"], data["template"]);
    let result = await utils_ns.writeFileToDataDirMakedirs(filePath, JSON.stringify(data));
    return result;
  },

  _transPairsGetFilePath: function (srcLang, tarLang, templateDict) {
    let secretString = srcLang + tarLang + templateDict["template"];
    let hashValue = secretString.hashCode();
    let filePath = `${consts_ns.CACHE_DIR}/translation-pairs${hashValue}.json`;
    return filePath;
  },

  // CODE BLOCKS
  // number of code blocks after which just retrieve from cache
  CODE_BLOCKS_MIN_CACHE_SIZE: 3000,

  getCachedCodeBlocks: async function (lang, temperature, templateDict) {
    let cacheData = await queryAPI_ns.cache._codeBlocksLoad(lang, temperature, templateDict);
    if (cacheData === null) { return null; }
    let codeBlocks = cacheData["code_blocks"];
    if (codeBlocks.length < queryAPI_ns.cache.CODE_BLOCKS_MIN_CACHE_SIZE) { return null; }
    // if the cache is big enough, retrieve from cache
    let returnSize = consts_ns.NUM_COMPLETIONS_SINGLE_PROMPT * consts_ns.NUM_CODE_BLOCKS_IN_SINGLE_RESPONSE;
    return utils_ns.getRandomSubarray(codeBlocks, returnSize);
  },

  updateCodeBlocksCache: async function (lang, temperature, templateDict, codeBlocks) {
    let cacheData = await queryAPI_ns.cache._codeBlocksLoad(lang, temperature, templateDict);
    if (cacheData !== null) {
      await queryAPI_ns.cache._codeBlocksAppend(cacheData, codeBlocks);
    } else {
      await queryAPI_ns.cache._codeBlocksCreate(lang, temperature, templateDict, codeBlocks);
    }
  },

  // return data if exists
  _codeBlocksLoad: async function (lang, temperature, templateDict) {
    let filePath = this._codeBlocksGetFilePath(lang, temperature, templateDict);
    let dataStr = await utils_ns.readFileFromDataDir(filePath);
    if (dataStr === null) { return null; }
    let data = JSON.parse(dataStr);
    return data;
  },

  _codeBlocksCreate: async function (lang, temperature, templateDict, codeBlocks) {
    let data = {
      template: templateDict["template"],
      lang: lang,
      temperature: temperature,
      code_blocks: codeBlocks,
      num_code_blocks: codeBlocks.length,
    };
    let filePath = this._codeBlocksGetFilePath(lang, temperature, templateDict);
    let result = await utils_ns.writeFileToDataDirMakedirs(filePath, JSON.stringify(data));
    return result;
  },

  _codeBlocksAppend: async function(data, codeBlocks) {
    data["code_blocks"].push(...codeBlocks);
    data["num_code_blocks"] = data["code_blocks"].length;
    let filePath = this._codeBlocksGetFilePath(data["lang"], data["temperature"], data["template"]);
    let result = await utils_ns.writeFileToDataDirMakedirs(filePath, JSON.stringify(data));
    return result;
  },

  _codeBlocksGetFilePath: function (lang, temperature, templateDict) {
    let secretString = templateDict["template"] + lang + temperature;
    let hashValue = secretString.hashCode();
    let filePath = `${consts_ns.CACHE_DIR}/code-blocks${hashValue}.json`;
    return filePath;
  },

  // TRANSLATIONS
  // if there are N translations for a program in cache, return from cache
  NUM_TRANS_PER_PROG: 30,

  // return data if exists
  loadTranslations: async function (srcLang, tarLang, templateDict) {
    let filePath = this._getFilePathTranslations(srcLang, tarLang, templateDict);
    let dataStr = await utils_ns.readFileFromDataDir(filePath);
    if (dataStr === null) { return null; }
    let data = JSON.parse(dataStr);
    return data;
  },

  createTranslations: async function (srcLang, tarLang, templateDict, translationsGathered) {
    let data = {
      source_lang: srcLang,
      target_lang: tarLang,
      template: templateDict["template"],
      template_origin: templateDict["template_origin"],
      translations: translationsGathered,
    };
    let filePath = this._getFilePathTranslations(template, srcLang, tarLang);
    let result = await utils_ns.writeFileToDataDirMakedirs(filePath, JSON.stringify(data));
    return result;
  },

  _getFilePathTranslations: function (template, sourceLang, targetLang) {
    let secretString = template + sourceLang + targetLang;
    let hashValue = secretString.hashCode();
    let filePath = `${consts_ns.CACHE_DIR}/translations${hashValue}.json`;
    return filePath;
  },
};

// ==============================================================================
// ================= CLASSES ====================================================
// ==============================================================================

/**
 * This is an error that is thrown when post-processing program pairs
 * resulted in zero translation pairs.
*/
queryAPI_ns.ZeroTranslationPairsError = class extends Error {
  constructor(message = "") {
    super(message);
    this.name = "ZERO_TRANSLATION_PAIRS_ERROR";
    this.message = message;
  }
};

/**
 * This is an error that is thrown when there are no templates left.
 * NOTE This is a severe error.
*/
queryAPI_ns.TemplatesExhaustedError = class extends Error {
  constructor(message = "") {
    super(message);
    this.name = "TEMPLATES_EXHAUSTED_ERROR";
    this.message = message;
  }
};

/**
 * This is an error that is thrown when Pirel hits a retry limit
 * when generating post-processed unique programs
*/
queryAPI_ns.PostProcessedProgramGenerationRetryLimitError = class extends Error {
  constructor(message = "") {
    super(message);
    this.name = "POST_PROCESSED_PROGRAM_GENERATION_RETRY_LIMIT_ERROR";
    this.message = message;
  }
};

/**
 * This error is thrown when a translation that satisfies
 * certain criteria could not be generated
*/
queryAPI_ns.SP1_TranslationError = class extends Error {
  constructor(message = "") {
    super(message);
    this.name = "SOURCE_PROGRAM_1_TRANSLATION_ERROR";
    this.message = message;
  }
};

// ==============================================================================
// ================= OPENAI API =================================================
// ==============================================================================

/**
 * This is a function that makes a call to ChatGPT.
 * Return a response object.
 * TODO infer cooldown timer from number of tokens as well
 * TODO implement retry with exponential backoff
 * https://platform.openai.com/docs/guides/rate-limits/retrying-with-exponential-backoff
*/
queryAPI_ns.openaiFetchAPI = async function (
  purposeStr,
  apiKey,
  messages,
  temperature = 0.7,
  numCompletions = 1
) {
  return await queryAPI_ns.openaiFetchApiWithExponentialBackoff(
    purposeStr,
    apiKey,
    messages,
    temperature,
    numCompletions
  );
};

/**
 *
*/
queryAPI_ns.openaiFetchApiWithExponentialBackoff = async function (
  purposeStr,
  apiKey,
  messages,
  temperature,
  numCompletions
) {

  let numRetries = 0
  let delay = consts_ns.AB_INITIAL_DELAY;

  while (true) {

    console.log(`Pirel: calling ChatGPT for ${purposeStr}.`);
    // main work
    let url = consts_ns.OPENAI_MODEL_ENDPOINT;
    let bearer = "Bearer " + apiKey;
    let response = await fetch(url, {
      method: "POST",
      headers: {
        Authorization: bearer,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        model: consts_ns.OPENAI_MODEL_NAME,
        messages: messages,
        temperature: temperature,
        n: Math.min(numCompletions, consts_ns.OPENAI_MAX_NUM_COMPLETIONS),
      }),
    });
    let responseDict = await response.json();

    // check if main work is successful or not
    if ("error" in responseDict) {
      numRetries++;
      if (numRetries > consts_ns.AB_MAX_RETRIES) {
        alert("IMPORTANT: consider this case in openaiFetchApiWithExponentialBackoff");
      }
      delay *= consts_ns.AB_EXPONENTIAL_BASE;
      console.log(`Pirel: hit a request limit. Sleeping for ${delay}ms.`);
      await utils_ns.sleep(delay);

      // try again
      continue;
    }

    return responseDict;
  }
}

// ==============================================================================
// ================= CONSTRUCTING QUERIES =======================================
// ==============================================================================

queryAPI_ns.createMessagesForSimplification = function (
  lang,
  template,
  numSamples
) {
  let systemContent = tmplns.simplification.getSystemContent(lang);
  let goldConversation = tmplns.simplification.getGoldConversation(2);
  let prompt = tmplns.simplification.getPrompt_PY(
    template,
    numSamples
  );

  let messages = [{ role: "system", content: systemContent }, ...goldConversation, { role: "user", content: prompt }];

  return messages;
};

queryAPI_ns.createMessagesForGeneration = function (
  lang,
  templateDict
) {

  // update templates to add more language support
  console.assert(lang === "py", "Currently support only generation for Python");

  let systemContent = tmplns.generation.getSystemContent(lang);
  let goldConversation = tmplns.generation.getGoldConversation(2);

  let prompt = null;
  if (templateDict["is_insert_secret_fn"]) {
    prompt = tmplns.generation.getPrompt_secret_PY(
      templateDict["template"],
      "literal or identifier",
      consts_ns.NUM_CODE_BLOCKS_IN_SINGLE_RESPONSE
    );
  } else {
    prompt = tmplns.generation.getPrompt_PY(
      templateDict["template"],
      "literal or identifier",
      consts_ns.NUM_CODE_BLOCKS_IN_SINGLE_RESPONSE
    );
  }

  let messages = [{ role: "system", content: systemContent }, ...goldConversation, { role: "user", content: prompt }];

  return messages;
};

queryAPI_ns.createMessagesForTranslation = function (
  programToTranslate,
  srcLang,
  tarLang
) {
  // update templates to add more language support
  console.assert(srcLang === "py" && tarLang === "js", "Currently support only translation py->js");

  let systemContent = tmplns.translation.getSystemContent(srcLang, tarLang);
  let goldConversation = tmplns.translation.getGoldConversation(2);
  let prompt = tmplns.translation.getPrompt(programToTranslate, srcLang, tarLang);

  let messages = [{ role: "system", content: systemContent }, ...goldConversation, { role: "user", content: prompt }];
  return messages;
};

queryAPI_ns.createMessagesForTransSimilar = function (
  programToTranslate,
  srcLang,
  tarLang,
  referenceSource,
  referenceTarget
) {
  // update templates to add more language support
  console.assert(srcLang === "py" && tarLang === "js", "Currently support only translation py->js");

  let systemContent = tmplns.transSimilar.getSystemContent();
  let prompt = tmplns.transSimilar.getPrompt(
    programToTranslate,
    referenceSource,
    referenceTarget,
    srcLang,
    tarLang
  );

  let messages = [{ role: "system", content: systemContent }, { role: "user", content: prompt }];
  return messages;
};

queryAPI_ns.createUserMessage = function (message) {
  return {
    role: "user",
    content: message
  };
};

queryAPI_ns.createAssistantMessage = function (message) {
  return {
    role: "assistant",
    content: message
  };
};

queryAPI_ns.createUserAssistantMessage = function (userMsg, assistantMsg) {
  return [
    queryAPI_ns.createUserMessage(userMsg),
    queryAPI_ns.createAssistantMessage(assistantMsg)
  ];
};

// ==============================================================================
// ================= TRANSLATING PROGRAMS USING LLMs ============================
// ==============================================================================

/**
 * Translate a given `program` from `sourceLang` to `targetLang`.
 * Return a list of code blocks in LLM response.
 *
 * NOTE: `program` may not be in `sourceLang`
 *
 * POST: codeBlocks.length >= 0
*/
queryAPI_ns.queryTranslationSP1 = async function (
  srcLang,
  tarLang,
  program,
  programMetadata
) {
  let messages = queryAPI_ns.createMessagesForTranslation(program, srcLang, tarLang);
  let rawDict = await queryAPI_ns.openaiFetchAPI("translation", consts_ns.OPENAI_API_KEY, messages);
  let rawResponse = rawDict["choices"][0]["message"]["content"];
  let codeBlocks = queryAPI_ns.extractCodeBlocksFromRawResponse(rawResponse);

  await utils_ns.writeJsonWithTimestamp(messages, `prompt-translate-sp1`, programMetadata.log_dir);

  return codeBlocks;
};

queryAPI_ns.queryTranslationSP2 = async function (
  srcLang,
  tarLang,
  program,
  refSrc,
  refTar,
  programMetadata
) {
  let messages = queryAPI_ns.createMessagesForTransSimilar(program, srcLang, tarLang, refSrc, refTar);
  let rawDict = await queryAPI_ns.openaiFetchAPI("translate similar", consts_ns.OPENAI_API_KEY, messages);
  let rawResponse = rawDict["choices"][0]["message"]["content"];
  let codeBlocks = queryAPI_ns.extractCodeBlocksFromRawResponse(rawResponse);

  await utils_ns.writeJsonWithTimestamp(messages, `prompt-translate-sp2`, programMetadata.log_dir);

  return codeBlocks;
};

/**
 * PARAMS
 * SP1 - source program 1
*/
queryAPI_ns.translateSP1 = async function (
  SP1,
  srcLang,
  tarLang,
  templateDict,
  programMetadata
) {

  log("start translateSP1");

  let retryCount = 0;
  let MAX_RETRIES = 10;

  while (true) {
    let candTrans = await queryAPI_ns.queryTranslationSP1(srcLang, tarLang, SP1, programMetadata);

    let programPairs = [];
    for (let candidateTranslation of candTrans) {
      programPairs.push({source: SP1, target: candidateTranslation});
    }

    let dataToPostProcess = {
      program_pairs: programPairs,
      contexts: templateDict["contexts"]
    };
    let resultDict = await postProcessProgramPairsOnBackendAsync(dataToPostProcess);
    await utils_ns.writeJsonWithTimestamp(dataToPostProcess, `sp1-translation-data2pp`, programMetadata.log_dir);
    await utils_ns.writeJsonWithTimestamp(resultDict, `sp1-translation-pp`, programMetadata.log_dir);

    if (resultDict["success"]) {
      log("end translateSP1");
      return resultDict["good_program_pairs"];
    } else {
      retryCount++;
      // potentially provide negative examples (translations that didn't work) to guide the translation
    }

    if (retryCount === MAX_RETRIES) {
      throw new queryAPI_ns.SP1_TranslationError();
    }
  }

};

/**
 * PARAMS
 * SP2 - source program 2
*/
queryAPI_ns.translateSP2 = async function (
  SP2,
  srcLang,
  tarLang,
  candProgPairsSP1,
  templateDict,
  programMetadata
) {

  log("start translateSP2");

  let translationPairs = [];
  let MAX_RETRIES = 3;

  for (let candProgPairSP1 of candProgPairsSP1) {
    let SP1 = candProgPairSP1["source"];
    let candTranslationSP1 = candProgPairSP1["target"];

    let retryCount = 0;
    while (retryCount < MAX_RETRIES) {

      let rawTranslationsSP2 = await queryAPI_ns.queryTranslationSP2(
        srcLang,
        tarLang,
        SP2,
        SP1,
        candTranslationSP1,
        programMetadata
      );

      let dataToPostProcess = {
        sp1: SP1,
        sp2: SP2,
        cand_translation_sp1: candTranslationSP1,
        raw_translations_sp2: rawTranslationsSP2,
        contexts: templateDict["contexts"]
      };
      let resultDict = await postProcessTranslationPairOnBackendAsync(dataToPostProcess);
      await utils_ns.writeJsonWithTimestamp(dataToPostProcess, `sp2-translation-data2pp`, programMetadata.log_dir);
      await utils_ns.writeJsonWithTimestamp(resultDict, `sp2-translation-pp`, programMetadata.log_dir);

      if (resultDict["success"]) {
        translationPairs.push(...resultDict["translation_pairs"]);
        break;
      }

      retryCount++;
    }
  }

  if (translationPairs.length === 0) {
    throw new queryAPI_ns.ZeroTranslationPairsError();
  }

  log("end translateSP2");
  return translationPairs;

};

// ==============================================================================
// ================= PARSING RAW LLM RESPONSE ===================================
// ==============================================================================

/*
The idea is that code fragments in raw response are surrounded by ``` (triple backticks)
Returns a list of code blocks in raw LLM response.
*/
queryAPI_ns.extractCodeBlocksFromRawResponse = function (response) {
  const reCodeSegment = /^```(\w*)\n(.*?)```/gms;
  let codeBlocks = [];

  for (const match of response.matchAll(reCodeSegment)) {
    const langAnnotation = match[1]; // can be used later
    const segmentCode = match[2];
    codeBlocks.push(segmentCode.trim());
  }

  return codeBlocks;
};

// ==============================================================================
// ================= GENERATING PROGRAMS USING LLMs =============================
// ==============================================================================

queryAPI_ns.generateBunchOfCodeBlocks = async function (
  messages,
  purposeStr,
  temperature,
  programMetadata,
) {

  log('start generateBunchOfCodeBlocks');
  let codeBlocks = [];

  // query LLM
  let responseDict = await queryAPI_ns.openaiFetchAPI(
    purposeStr,
    consts_ns.OPENAI_API_KEY,
    messages,
    temperature,
    consts_ns.NUM_COMPLETIONS_SINGLE_PROMPT
  );
  let rawResponses = responseDict["choices"].map(x => x["message"]["content"]);
  await utils_ns.writeJsonWithTimestamp(responseDict, `raw-response-dict-${purposeStr}-temp-${temperature}`, programMetadata.log_dir);

  // extract code blocks from raw responses
  for (let rawResponse of rawResponses) {
    codeBlocks.push(...queryAPI_ns.extractCodeBlocksFromRawResponse(rawResponse));
  }

  log('end generateBunchOfCodeBlocks');
  return codeBlocks;
};

/**
 *
*/
queryAPI_ns.simplifyTemplate = async function (
  lang,
  templateDict,
  programMetadata
) {
  log('start simplifyTemplate');

  // no context nodes were simplified
  if (Object.keys(templateDict["templatized_node_ids_context"]).length === 0) {
    return {
      new_template: templateDict["template_context_str_repl"],
      new_template_origin: templateDict["template_origin"]
    };
  }

  let llmTemperature = consts_ns.GEN_START_TEMPERATURE;
  let allRawCodeBlocks = [];
  let retryCount = 0;
  let numSamplesInResponse = 5;
  let messages = queryAPI_ns.createMessagesForSimplification(
    lang,
    templateDict["template_context"],
    numSamplesInResponse
  );

  while (true) {
    // generate raw code blocks
    let rawCodeBlocks = await queryAPI_ns.generateBunchOfCodeBlocks(
      messages,
      "simplification",
      llmTemperature,
      programMetadata
    );
    allRawCodeBlocks.push(...rawCodeBlocks);
    await utils_ns.writeJsonWithTimestamp(
      allRawCodeBlocks,
      `simple-templates-raw-temp-${llmTemperature}`,
      programMetadata.log_dir
    );

    // post-process raw code blocks
    let dataToPostProcess = {
      lang: lang,
      template_origin: templateDict["template_origin"],
      templatized_node_ids_context: templateDict["templatized_node_ids_context"],
      simplified_templates: allRawCodeBlocks,
    }
    let resultDict = await postProcessSimplifiedTemplatesOnBackendAsync(dataToPostProcess);
    await utils_ns.writeJsonWithTimestamp(resultDict, `template-simplification-dict-temp-${llmTemperature}`, programMetadata.log_dir);

    let simplestTemplate = resultDict["simplest_template"];
    let templatizedNodeTexts = resultDict["templatized_node_texts"];

    if (simplestTemplate !== null) {
      let templateContextStrRepl = templateDict["template_context_str_repl"];
      for (let templatizedNodeText of templatizedNodeTexts) {
        templateContextStrRepl = templateContextStrRepl.replace("<|pirel_context_hole|>", templatizedNodeText);
      }
      return {
        new_template: templateContextStrRepl,
        new_template_origin: simplestTemplate
      };
    }

    retryCount++;
    llmTemperature += consts_ns.GEN_TEMPERATURE_INCREMENT;
    llmTemperature = Math.round(llmTemperature * 10) / 10;

    if (retryCount > consts_ns.GEN_POST_PROCESSED_MAX_RETRIES) {
      throw new queryAPI_ns.PostProcessedProgramGenerationRetryLimitError();
    }
  }
};

/**
 * Return best N program pairs (by score, refer to backend code)
*/
queryAPI_ns.generateProgramPairSrcLang = async function (
  lang,
  templateDict,
  programMetadata
) {

  log('start generateProgramPairSrcLang');

  let templateOrigin = templateDict["template_origin"];
  let templatizedNodeIds = templateDict["templatized_node_ids"]
  let isInsertSecretFn = templateDict["is_insert_secret_fn"];

  let llmTemperature = consts_ns.GEN_START_TEMPERATURE;
  let allRawCodeBlocks = [];
  let retryCount = 0;
  let minPenalty = 1e100;  // min penalty -> best program pair
  let BEST_N = 10;  // return best N two source programs

  // loop to guarantee numPrograms post-processed programs
  while (true) {

    // ~~~ query LLM for raw code blocks
    let messages = queryAPI_ns.createMessagesForGeneration(lang, templateDict);
    let rawCodeBlocks = await queryAPI_ns.generateBunchOfCodeBlocks(
      messages,
      "generation",
      llmTemperature,
      programMetadata
    );
    allRawCodeBlocks.push(...rawCodeBlocks);
    await utils_ns.writeJsonWithTimestamp(allRawCodeBlocks, `code-blocks-raw-temp-${llmTemperature}`, programMetadata.log_dir);

    // ~~~ post-process generated code blocks
    let dataToPostProcess = {
      lang: lang,
      template_origin: templateOrigin,
      templatized_node_ids: templatizedNodeIds,
      generated_code_blocks: allRawCodeBlocks,
      is_insert_secret_fn: isInsertSecretFn
    };
    let resultDict = await postProcessGeneratedCodeBlocksOnBackendAsync(dataToPostProcess);
    await utils_ns.writeJsonWithTimestamp(resultDict, `code-blocks-pp-temp-${llmTemperature}`, programMetadata.log_dir);

    // ~~~ check post-processing results
    if (resultDict["success"]) {

      // run until we no longer see improvement in best score (greedy)
      if (resultDict["min_penalty"] < minPenalty) {
        minPenalty = resultDict["min_penalty"];
      } else {
        let bestNArray = resultDict["valid_tsp_list"].slice(0, BEST_N);
        let programPairs = [];
        let templatizedNodesRepDWS = [];
        for (let elem of bestNArray) {
          programPairs.push([elem["program1"], elem["program2"]]);
          templatizedNodesRepDWS.push(elem["templatized_nodes_replace_dot_w_star_flags"])
        }
        return {
          program_pairs: programPairs,
          templatized_nodes_replace_dot_w_star_flags: templatizedNodesRepDWS
        };
      }

    } else {
      retryCount++;
      llmTemperature += consts_ns.GEN_TEMPERATURE_INCREMENT;
      llmTemperature = Math.round(llmTemperature * 10) / 10;
    }

    if (retryCount > consts_ns.GEN_POST_PROCESSED_MAX_RETRIES) {
      throw new queryAPI_ns.PostProcessedProgramGenerationRetryLimitError();
    }

  }
};

// ==============================================================================
// ================= GENERATING TRANSLATION PAIRS USING LLMs ====================
// ==============================================================================

/**
 * Generate AT LEAST ONE translation pair for a given template
 * OR throw an error if cannot.
 *
 * Throw ZeroTranslationPairsError if cannot generate translation pairs for the given template.
 *
 * This method 'guarantees' that the translation pair(s) it returns
 * is enough to learn a rule that is able to translate a problematic node.
 *
 * That is why returning at least a SINGLE translation pair is enough.
 *
 * Ideally, each translation pair allows learning different rules,
 * that produce different translations.
 *
 * So this function tries to return all possible translation pairs that allow learning different rules.
 * For the example below, in the ideal case, we want four different translation pairs.
 * a = 5
 * can be translated as:
 * a = 5;
 * let a = 5;
 * var a = 5;
 * const a = 5;
 *
 * OVERVIEW
 * iterate over every template starting from the lowest level (level closest to the problematic node),
 * skip the template if it is invalid.
 * if LLM struggles with generating programs that pass post-processing stage, skip to next template up a level.
 * otherwise, break and return.
 *
 * PARAMS
 * programMetadata - contains metadata about the program that is being translated
 * templateDict - contains information on what kind of source program should be generated.
 * For the format of it, refer to s_extract_templates.extract_templates().
 *
 * INTERNALS
 * queryAPI_ns.generationState - refer to the beginning of this file
 *
 * This method guarantees the minimum number of translation pairs that result in unique rules.
 * TERMS
 * translation pair: [
 *   {source: source_program1, target: target_program2},
 *   {source: source_program2, target: target_program2},
 * ]
 *
 * RETURN
 * List [
 *   [
 *     {source: source_program1, target: target_program2},
 *     {source: source_program2, target: target_program2},
 *   ], ...
 * ]
*/
queryAPI_ns.genTransPair = async function (
  srcLang,
  tarLang,
  templateDict,
  programMetadata
) {

  log("start genTransPair");

  // 1 simplify the template context
  let simplificationResultDict = await queryAPI_ns.simplifyTemplate(
    srcLang,
    templateDict,
    programMetadata
  );
  let template = simplificationResultDict['new_template'];
  let templateOrigin = simplificationResultDict['new_template_origin'];

  templateDict["template"] = template;
  templateDict["template_origin"] = templateOrigin;
  await utils_ns.writeJsonWithTimestamp(templateDict, "simplified-template-dict", programMetadata.log_dir);

  // 2 generate two post-processed unique programs in `srcLang`
  let tspDict = await queryAPI_ns.generateProgramPairSrcLang(
    srcLang,
    templateDict,
    programMetadata
  );
  let srcProgPairs_N = tspDict["program_pairs"];
  let templatizedNodesReplaceDWS_N = tspDict["templatized_nodes_replace_dot_w_star_flags"];
  await utils_ns.writeJsonWithTimestamp(srcProgPairs_N, "gen-bestN-two-src-progs", programMetadata.log_dir);
  await utils_ns.writeJsonWithTimestamp(templatizedNodesReplaceDWS_N, "should-replace-dot-w-star", programMetadata.log_dir);

  console.assert(srcProgPairs_N.length === templatizedNodesReplaceDWS_N.length);

  // iterate over best N two source programs (sorted by score on backend)
  let translationPairs = null;
  let templatizedNodesRepDWS = null;
  for (let i = 0; i < srcProgPairs_N.length; i++) {
  // for (let srcProgPair of srcProgPairs) {
    let [srcProgram1, srcProgram2] = srcProgPairs_N[i];
    templatizedNodesRepDWS = templatizedNodesReplaceDWS_N[i];

    // 3 translate source program #1
    let candProgPairsSP1 = null;
    try {
      candProgPairsSP1 = await queryAPI_ns.translateSP1(
        srcProgram1,
        srcLang,
        tarLang,
        templateDict,
        programMetadata
      );
    } catch (error) {
      if (error instanceof queryAPI_ns.SP1_TranslationError) {
        continue;
      }
    }

    // 4 generate all candidate translation pairs for source program 2
    try {
      translationPairs = await queryAPI_ns.translateSP2(
        srcProgram2,
        srcLang,
        tarLang,
        candProgPairsSP1,
        templateDict,
        programMetadata
      );
    } catch (error) {
      if (error instanceof queryAPI_ns.ZeroTranslationPairsError) {
        continue;
      }
    }

    break;  // keep the first only
  }

  log("end genTransPair");

  if (translationPairs === null) {
    throw new queryAPI_ns.ZeroTranslationPairsError();
  }

  return {
    translation_pairs: translationPairs,
    templatized_nodes_replace_dws_values: templatizedNodesRepDWS
  };
};
