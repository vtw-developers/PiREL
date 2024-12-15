/**
 * The 'module' that contains everything for learning rules using Pirel.
*/

// namespaces
var learnRules_ns = {};
var benchmark_ns = {};

// ==============================================================================
// ================= BENCHMARK ==================================================
// ==============================================================================

/**
 * Outer-most function to get the program contents for learning rules.
 * Sampling can be implemented here.
 *
 * PARAMS
 * fromIdx, toIdx - are 0-based normal array indices
*/
benchmark_ns.getProgramsForLearningRules = async function(fromIdx, toIdx) {
  let leetCodePrograms = await benchmark_ns._getLeetCodePrograms(fromIdx, toIdx);
  return leetCodePrograms;
};

/**
 * Returns program contents in data/duoglot/tests/staleetcode/pysep
 *
 * PARAMS
 * firstN - return first N programs (sorted alphabetically)
 * Can be arbitrarily large number to get all programs.
 *
 * RETURN FORMAT
 * returnData = [
 *   {
 *     file_name: str,
 *     content: str,
 *     id: str
 *   }
 * ]
*/
benchmark_ns._getLeetCodePrograms = async function(fromIdx, toIdx) {

  let returnData = [];

  let filesDirsDict = await getGeneralBenchFilesAsync("staleetcode/pysep");
  let allFilesList = filesDirsDict["files"];
  let validProgramNames = allFilesList.filter(
    f => f.startsWith("L") && f.endsWith(".py") && !f.endsWith("__test.py")
  );

  validProgramNames.sort();

  // get first N program names
  validProgramNames = validProgramNames.slice(fromIdx, toIdx);

  // temporary hack to run just L0003_LongestSubstringWithoutRepeatingCharacters.py
  // TODO remove after testing
  // validProgramNames = ["L0003_LongestSubstringWithoutRepeatingCharacters.py"];

  for (let programName of validProgramNames) {
    let programPath = `duoglot/tests/staleetcode/pysep/${programName}`;
    let programSource = await utils_ns.readFileFromDataDir(programPath);
    let programId = programName.slice(0, 5);
    let programData = {
      file_name: programName,
      content: programSource,
      id: programId
    };
    returnData.push(programData);
  }

  return returnData;
};

/**
 * Returns
 * 1. path to the starting ruleset
 * 2. path where the updated rulesed is saved after adding newly learned rules with Pirel
 * `customSuffix` can be an empty string
*/
benchmark_ns.getStartingUpdatedRulesetPaths = async function(customSuffix, config) {
  let rulesetDir = config["ruleset_dir"];
  let startRulesetName = config["start_ruleset"];
  let updatedRulesetSuffix = config["updated_ruleset_suffix"];

  if (customSuffix !== "") {
    customSuffix = "_" + customSuffix;
  }

  let startRulesetPath = `${rulesetDir}/${startRulesetName}.snart`;
  let updatedRulesetPath = `${rulesetDir}/${startRulesetName}_${updatedRulesetSuffix}${customSuffix}.snart`;

  if (config["save_updated_ruleset_to_start_ruleset_file"]) {
    updatedRulesetPath = startRulesetPath;
  }

  return [startRulesetPath, updatedRulesetPath];
};

// ==============================================================================
// ================= UI ELEMENTS ================================================
// ==============================================================================

learnRules_ns.startButtonHandler = async function() {
  await learnRules_ns.main();
};
learnRules_ns.startButton = document.getElementById("start-rule-learning-btn");
learnRules_ns.startButton.addEventListener("click", learnRules_ns.startButtonHandler);

learnRules_ns.subjectsFromIdxInput = document.getElementById("subjects-from-idx");
learnRules_ns.subjectsToIdxInput = document.getElementById("subjects-to-idx");

learnRules_ns.logsTextArea = document.getElementById("learn-rules-logs-textarea");
learnRules_ns.currentSubjectInput = document.getElementById("current-subject-input");
// learnRules_ns.currentSubjectInput.value = "10";

// ==============================================================================
// ================= LOGGING ====================================================
// ==============================================================================

learnRules_ns.logs = [];

learnRules_ns.log = function() {
  let options = {
    hour12: false,
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    fractionalSecondDigits: "3"
  };
  let currentTime = new Date().toLocaleTimeString("en-US", options);
  let args = Array.from(arguments).join(" ");
  learnRules_ns.logs.push(`${currentTime}: ${args}`);

  // uncomment if need to see the arguments in console
  // console.log(...arguments);

  learnRules_ns.logsTextArea.innerHTML = learnRules_ns.logs.join("\n");
};

learnRules_ns.clearLogs = function() {
  learnRules_ns.logs = [];
};

learnRules_ns.saveLogs = async function() {
  await utils_ns.writeJsonWithTimestamp(learnRules_ns.logs, "logs", consts_ns.DEBUG_OUTPUT_LEARN_RULES_DIR);
};

// ==============================================================================
// ================= ENTRY POINT ================================================
// ==============================================================================

/**
 * TODO update this doc
 * Run rules learner on a single program
 *
 * PARAMS
 *
 * TERMS
 * programMetadata
 * programTranslationState
 * currentNodeState
 *
 * LOGS STRUCTURE
 * logs
 * - programId
 *   - template.json
 * - ...
 * - logs.json
 *
 * RETURN
 * True if translation was successful
 * False otherwise
*/
learnRules_ns.runSingleProgram = async function(
  programFileName,
  programSourceCode,
  programId,
  ruleset,
  updatedRulesetPath,
  config
) {

  function _log() {learnRules_ns.log("[learnRules_ns.runSingleProgram]", ...arguments);}
  _log("Starting translation of", programFileName);

  programLogDir = consts_ns.DEBUG_OUTPUT_LEARN_RULES_DIR + "/" + programId;
  await utils_ns.writeFileToDataDirMakedirs(programLogDir + "/program.py", programSourceCode);
  await utils_ns.writeFileToDataDirMakedirs(programLogDir + "/starting_ruleset.snart", ruleset);

  // this is an object that stores the state of Pirel for the current program
  let programTranslationState = {};

  // run the loop only `consts_ns.MAX_NUM_LOOPS_PIREL` times
  // OR some other error is thrown
  let attemptCount = 0;
  pirelLoop:
  while (attemptCount < consts_ns.MAX_NUM_LOOPS_PIREL) {
    attemptCount += 1;
    _log(`attempt number ${attemptCount} to translate ${programId}`);

    // ~~~ RUN NORMAL TRANSLATION
    let kwargs = {
      "subject_name": programId  // NOTE this is a prefix that is added to produced log messages and files
    };
    let translationResult = await translateAsync(
      programSourceCode,
      consts_ns.SRC_LANG,
      consts_ns.TAR_LANG,
      ruleset,
      consts_ns.TRANS_TYPE,
      consts_ns.TRANS_CHOICES,
      consts_ns.AUTOBACK_ENABLED,
      config.enable_pirel,
      kwargs
    );
    let [_1, _2, errorInfo, _4, _5, _6, _7, pirelData] = translationResult;
    _log("translation is complete");

    // ~~~ TRANSLATION IS SUCCESSFUL
    if (!errorInfo && !pirelData) {
      programTranslationState["success"] = true;
      programTranslationState["result"] = "succesfully translated a program";
      _log("translation is successful");
      break pirelLoop;
    }

    // ~~~ THERE IS SOME ERROR ON THE BACKEND
    else if (errorInfo) {
      programTranslationState["success"] = false;
      programTranslationState["result"] = "some error on the backend";
      programTranslationState["error"] = JSON.stringify(errorInfo);
      _log("translation is unsuccessful: error on the backend");
      break pirelLoop;
    }

    // ~~~ TRANSLATION IS NOT SUCCESSFUL
    _log("Error in translation (no translation rule)");

    // parse data from backend
    let templateDict = pirelData["template_dict"];
    let translationPairsDict = pirelData["translation_pairs"];
    let srcLang = templateDict["src_lang"];
    let tarLang = templateDict["tar_lang"];

    // infer translation rules
    let translationRules = [];
    let prettyPrintTreeLike = false;

    let translationPairs = translationPairsDict["translation_pairs"];
    let templatizedNodesReplaceDWS = translationPairsDict["templatized_nodes_replace_dws_values"];

    for (let translationPair of translationPairs) {
      for (let context of templateDict["contexts"]) {
        let newTranslationRule = null;
        try {
          _log("attempting to infer a rule");
          newTranslationRule = await ruleInfAPI_ns.inferTranslationRule(
            srcLang,
            tarLang,
            translationPair,
            context,
            templateDict["templatized_node_ids"],
            templatizedNodesReplaceDWS,
            templateDict["is_insert_secret_fn"],
            prettyPrintTreeLike,
            kwargs
          );
          _log("successfully inferred a rule");
        } catch (e) {
          if (e instanceof ruleInfAPI_ns.ContextNotFoundError) {
            _log("context does not exist. skipping this context...");
            continue;
          }
          _log(`error during rule inference (skipping...): ${e}\n${e.stack}`);
          continue;
        }

        if (translationRules.includes(newTranslationRule)) {
          _log('already have this rule. will not add it to the ruleset');
          continue;
        }

        // update the ruleset and save it locally
        translationRules.push(newTranslationRule);
        await utils_ns.writeWithTimestamp(newTranslationRule, "learned-rule.snart", programLogDir);
        ruleset = ruleset + "\n\n;;;; NEW RULE FROM PIREL (LEARN RULES)\n" + newTranslationRule + "\n";
        await utils_ns.writeFileToDataDir(updatedRulesetPath, ruleset);
        _log("successfully inferred a rule and saved it.");
      }
    }
  }

  // do some finalization
  // TODO the template node ids need to be updated
  await utils_ns.writeJsonWithTimestamp(programTranslationState, "program-translation-state", programLogDir);
  return programTranslationState["success"];
};

learnRules_ns._getSubjectsFromToIdxs = function() {
  const subjectsFromIdx = parseInt(learnRules_ns.subjectsFromIdxInput.value, 10);
  const subjectsToIdx = parseInt(learnRules_ns.subjectsToIdxInput.value, 10);
  if (!Number.isInteger(subjectsFromIdx)) throw new Error("left index is not a number");
  if (!Number.isInteger(subjectsToIdx)) throw new Error("right index is not a number");
  if (subjectsFromIdx < 1) throw new Error("left index should be greater than or equal to 1");
  if (subjectsToIdx < 1) throw new Error("right index should be greater than or equal to 1");
  if (subjectsFromIdx > subjectsToIdx) throw new Error("left index should be less than or equal to right index");
  return [subjectsFromIdx, subjectsToIdx];
}

/**
 * This entry point is invoked by clicking a button.
 * Refer to `learnRules_ns.startButtonHandler()`
*/
learnRules_ns.main = async function() {

  function _log() {learnRules_ns.log("[learnRules_ns.main]", ...arguments);}

  _log("Pirel starting");

  const [subjectsFromIdx, subjectsToIdx] = learnRules_ns._getSubjectsFromToIdxs();
  const subjectsNum = subjectsToIdx - subjectsFromIdx + 1;

  var config = await utils_ns.readJsonFromDataDir("configs/learn-rules.json");
  _log(`Pirel configs: ${config}`);
  _log(`Pirel will learn rules from subjects in the range [${subjectsFromIdx}, ${subjectsToIdx}] (inclusive, 1-indexed)`);

  // turn indices to normal array indexing
  let programsDict = await benchmark_ns.getProgramsForLearningRules(subjectsFromIdx - 1, subjectsToIdx);

  // loop over programs
  let translationResults = [];
  for (let idx = 0; idx < subjectsNum; idx++) {

    const programName = programsDict[idx]["file_name"];
    const programContent = programsDict[idx]["content"];
    const programId = programsDict[idx]["id"];
    const subjectIdx = idx + subjectsFromIdx;

    _log("=================================");
    _log(`Starting Pirel translation of ${idx + 1}/${subjectsNum} ${programName}`);
    learnRules_ns.currentSubjectInput.value = subjectIdx;

    // `updatedRulesetPath` may be identical to `startRulesetPath`
    // in which case for each subsequent program in the benchmark all previously
    // learned rules serve as a base ruleset. This is controlled by
    // `save_updated_ruleset_to_start_ruleset_file` in config.
    let [startRulesetPath, updatedRulesetPath] = await benchmark_ns.getStartingUpdatedRulesetPaths(programName, config);
    let ruleset = await utils_ns.readFileFromDataDir(startRulesetPath);
    _log("Path to starting ruleset:", startRulesetPath);
    _log("Path to updated ruleset:", updatedRulesetPath);

    console.log("Current file", programName);
    console.log("Progress", `${idx + 1}/${subjectsNum}`);

    // ~~~
    let isTranslationSuccessful = await learnRules_ns.runSingleProgram(
      programName,
      programContent,
      programId,
      ruleset,
      updatedRulesetPath,
      config
    );

    translationResults.push({
      "program": programName,
      "result": isTranslationSuccessful
    });

    console.log("Result of", programName, "is", isTranslationSuccessful);
    _log(`Pirel translation result of ${programName} is "${isTranslationSuccessful}"`);

    await learnRules_ns.saveLogs();
    await utils_ns.writeJsonWithTimestamp(translationResults, "translation-results", consts_ns.DEBUG_OUTPUT_LEARN_RULES_DIR);
  }

  _log(`Pirel has finished`);
  alert("Pirel has finished");
};
