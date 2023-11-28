/**
 * The 'module' that contains everything for learning rules using Pirel.
*/

// namespace for rule learner
var learnRules_ns = {};

// namespace for benchmark
var benchmark_ns = {};

// ==============================================================================
// ================= BENCHMARK ==================================================
// ==============================================================================

/**
 * Outer-most function to get the program contents for learning rules.
 * Sampling can be implemented here.
 *
 * PARAMS
 * numPrograms - number of programs to get
*/
benchmark_ns.getProgramsForLearningRules = async function(numPrograms) {
  let leetCodePrograms = await benchmark_ns._getLeetCodePrograms(numPrograms);
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
 * returnData = {
 *   filename: {
 *     file_name: str,
 *     content: str,
 *     id: str
 *   }
 * }
*/
benchmark_ns._getLeetCodePrograms = async function(firstN) {

  let returnData = {};

  let filesDirsDict = await getGeneralBenchFilesAsync("staleetcode/pysep");
  let allFilesList = filesDirsDict["files"];
  let validProgramNames = allFilesList.filter(
    f => f.startsWith("L") && f.endsWith(".py") && !f.endsWith("__test.py")
  );

  validProgramNames.sort();

  // get first N program names
  validProgramNames = validProgramNames.slice(0, firstN);

  // temporary hack to run just L0003_LongestSubstringWithoutRepeatingCharacters.py
  // TODO remove after testing
  // validProgramNames = ["L0003_LongestSubstringWithoutRepeatingCharacters.py"];

  for (let programName of validProgramNames) {
    let programPath = `duoglot/tests/staleetcode/pysep/${programName}`;
    let programSource = await utils_ns.readFileFromDataDir(programPath);
    let programId = programName.slice(0, 5);
    returnData[programName] = {
      file_name: programName,
      content: programSource,
      id: programId
    };
  }

  return returnData;
};

/**
 * Returns
 * 1. path to the starting ruleset
 * 2. path where the updated rulesed is saved after adding newly learned rules with Pirel
*/
benchmark_ns.getRulesetPaths = async function() {
  let rulesetDir = "duoglot/tests/trans_programs/py_js";
  let startRulesetName = "base_upd";
  let updatedRulesetSuffix = "pirel";

  let startRulesetPath = `${rulesetDir}/${startRulesetName}.snart`;
  let updatedRulesetPath = `${rulesetDir}/${startRulesetName}_${updatedRulesetSuffix}.snart`;

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
  updatedRulesetPath
) {

  function __log() {learnRules_ns.log("[learnRules_ns.runSingleProgram]", ...arguments);}
  __log("Starting translation of", programFileName);

  // store metadata about the program under test
  let programMetadata = {
    file_name: programFileName,
    source_code: programSourceCode,
    id: programId,
    log_dir: consts_ns.DEBUG_OUTPUT_LEARN_RULES_DIR + "/" + programId,
    path: ((x) => consts_ns.DEBUG_OUTPUT_LEARN_RULES_DIR + "/" + programId + "/" + x)
  };

  // this is an object that stores the state of Pirel for the current program
  let programTranslationState = {};

  // create a log dir for the program under test
  await utils_ns.writeFileToDataDirMakedirs(programMetadata.path("program.py"), programSourceCode);
  __log("created log directory for the program under", programId);

  // run the loop only `consts_ns.MAX_NUM_LOOPS_PIREL` times
  // OR until all templates are exhausted
  // OR some other error is thrown
  let attemptCount = 0;
  pirelLoop:
  while (attemptCount < consts_ns.MAX_NUM_LOOPS_PIREL) {

    __log(`attempt number ${attemptCount + 1} to translate ${programId}`);

    // ~~~ run normal translation
    let translationResult = await translateAsync(
      programSourceCode,
      consts_ns.SRC_LANG,
      consts_ns.TAR_LANG,
      ruleset,
      consts_ns.TRANS_TYPE,
      consts_ns.TRANS_CHOICES,
      consts_ns.AUTOBACK_ENABLED
    );

    __log("translation is complete");

    // we need only errorInfo
    let [_1, _2, errorInfo, _3, _4, _5, _6] = translationResult;

    // there is an error in translation
    if (errorInfo && "templates_dict" in errorInfo) {
      __log("Error in translation");

      // 1 parse the data sent from the backend
      // refer to s_extract_templates.extract_templates() for the format of templates_dict
      let templatesDict = JSON.parse(errorInfo["templates_dict"]);
      let problematicNodeType = templatesDict["problematic_node_type"];
      let problematicNodeId = templatesDict["problematic_node_id"];
      let numTemplates = templatesDict["num_templates"];
      __log("problematic node type is", problematicNodeType);
      __log("problematic node id is", problematicNodeId);
      __log("number of templates is", numTemplates);
      await utils_ns.writeFileToDataDir(
        programMetadata.path(`templates-pnid-${problematicNodeId}-pntype-${problematicNodeType}.json`),
        JSON.stringify(templatesDict)
      );

      // 2 initiate the state for the current problematic node
      let currentNodeState = null;
      let previouslySeenNode = false;

      // 2.1 problematic node didn't change from previous iteration
      if (problematicNodeId in programTranslationState) {
        currentNodeState = programTranslationState[problematicNodeId];
        previouslySeenNode = true;
        __log(`seeing the same problematic node ${problematicNodeId} again: last template did not work`);

      // 2.2 seeing this problematic node for the first time
      } else {
        currentNodeState = programTranslationState[problematicNodeId] = {};
        // INV the following four sets are disjoint:
        currentNodeState["template_ids_skipped"] = []; // templates which could not be filled
        currentNodeState["template_ids_not_tried"] = Array.from(Array(numTemplates).keys()); // templates which have not been tried yet
        currentNodeState["template_ids_unsuccessful"] = []; // templates from which rules were inferred, but they didn't work
        currentNodeState["template_id_last_used"] = null; // THE template from which working rule was inferred
        __log(`seeing the problematic node ${problematicNodeId} for the first time`);
      }

      // 2.3 sanity check of INV (above)
      let _groundTruth = Array.from(Array(numTemplates).keys()).join(',');
      let _gathered = [
        ...currentNodeState["template_ids_skipped"],
        ...currentNodeState["template_ids_not_tried"],
        ...currentNodeState["template_ids_unsuccessful"],
      ];
      if (currentNodeState["template_id_last_used"] !== null) {
        _gathered.push(currentNodeState["template_id_last_used"]);
      }
      let _compared = _gathered.sort().join(',');
      if (_groundTruth !== _compared) {
        __log("INVARIANT is broken. Debugging needed.");
        __log("ground truth:", _groundTruth);
        __log("gathered:", _gathered);
        __log("skipped:", currentNodeState["template_ids_skipped"]);
        __log("unused:", currentNodeState["template_ids_not_tried"]);
        __log("unsuccessful:", currentNodeState["template_ids_unsuccessful"]);
        __log("last used:", currentNodeState["template_id_last_used"]);
      }

      // 2.4 no unused templates left => no rule was inferenced with given templates
      // TODO start over? what to change?
      if (currentNodeState["template_ids_not_tried"].length === 0) {
        __log(`SEVERE: no templates left for ${programId}. Quitting...`);
        programTranslationState["success"] = false;
        programTranslationState["result"] = "could not be translated due to template exhaustion";

        // breaking the loop is the same as returning from the function
        break pirelLoop;
      }

      // 3 ~~~ generate translation pairs
      let translationPairsDict = {};
      try {

        __log(`attempting to generate translation pairs for ${programId}`);
        translationPairsDict = await queryAPI_ns.generateAllPossibleTranslationPairs(
          consts_ns.SRC_LANG,
          consts_ns.TAR_LANG,
          templatesDict,
          currentNodeState["template_ids_not_tried"],
          programMetadata
        );
        // NOTE if generated more translation pairs than request, truncate (happens later down below)
        __log(`successfully generated at least ${Object.keys(translationPairsDict).length} translation pairs for ${programId}`);

      } catch (e) {

        // this is an expected error
        if (e instanceof queryAPI_ns.TemplatesExhaustedError) {
          __log(`SEVERE: translation pairs could not be generated for ${programId}.`);
          __log(`SEVERE: Tried all templates, but none worked`);
          programTranslationState["success"] = false;
          programTranslationState["result"] = "could not be translated because none of the templates worked";
          break pirelLoop;

          // this is an unexpected error
        } else {
          __log(`SEVERE: translation pairs could not be generated for ${programId}.`);
          __log(`Error is: ${e} (UNEXPECTED)`);
          __log(`Stacktrace:\n${e.stack}`);
          programTranslationState["success"] = false;
          programTranslationState["result"] = "could not be translated due to unexpected exception";
          break pirelLoop;
        }
      }
      await utils_ns.writeJsonWithTimestamp(translationPairsDict, "translation-pairs-dict", programMetadata.log_dir);

      // 4 extract data from programPairsData
      let templateIdsSkipped = translationPairsDict["template_ids_skipped"];
      let templateIdsUnused = translationPairsDict["template_ids_not_tried"];
      let templateIdUsed = translationPairsDict["template_id_last_used"];
      __log("templateIdsSkipped", templateIdsSkipped);
      __log("templateIdsUnused", templateIdsUnused);
      __log("templateIdUsed", templateIdUsed);
      __log(`generated ${translationPairsDict["translation_pairs"].length} translation pairs.`);

      // 5 update the currentNodeState
      // 5.1 if we have seen the node previously, then the previous inferred rule didn't work
      if (previouslySeenNode) {
        currentNodeState["template_ids_unsuccessful"].push(currentNodeState["template_id_last_used"]);
      }
      currentNodeState["template_ids_skipped"].push(...templateIdsSkipped);
      currentNodeState["template_ids_not_tried"] = templateIdsUnused;
      currentNodeState["template_id_last_used"] = templateIdUsed;

      // 6 ~~~ infer translation rule
      let templateHasPyBlockReplaced = templatesDict[templateIdUsed]["py_block_replaced"];

      for (let translationPair of translationPairsDict["translation_pairs"]) {

        // NOTE right now infer rules for both values of `chooseLargestContainingNode`
        // TODO might generate the same rule twice if largest and smallest containing nodes are one node
        for (let chooseLargestContainingNode of [true, false]) {

          // 6.1 invoke `ruleInfAPI_ns.inferTranslationRule()`
          let newTranslationRule = "";
          try {
            __log("attempting to infer a rule");
            newTranslationRule = await ruleInfAPI_ns.inferTranslationRule(
              translationPair,
              consts_ns.SRC_LANG,
              consts_ns.TAR_LANG,
              templateHasPyBlockReplaced,
              chooseLargestContainingNode
            );
            __log("successfully inferred a rule");
          } catch (e) {
            __log("error at inferring a rule from translation pair", translationPair);
            continue;
          }
          await utils_ns.writeJsonWithTimestamp(newTranslationRule, "generated-rule", programMetadata.log_dir);

          // 6.2 update the ruleset and save it locally
          ruleset = "; new rule from Pirel\n" + newTranslationRule + "\n\n" + ruleset;
          await utils_ns.writeFileToDataDir(updatedRulesetPath, ruleset);
          __log("successfully inferred a rule and saved it.");
        }
      }
    }

    // there is some error on the backend
    else if (errorInfo) {
      programTranslationState["success"] = false;
      programTranslationState["result"] = "some error on the backend";
      programTranslationState["error"] = JSON.stringify(errorInfo);
      __log("translation unsuccessful: error on the backend");
      break pirelLoop;
    }

    // there is no error in translation
    else {
      programTranslationState["success"] = true;
      programTranslationState["result"] = "succesfully translated a program";
      __log("translation successful");
      break pirelLoop;
    }

    attemptCount += 1;
  }

  // do some finalization
  // TODO the template node ids need to be updated
  await utils_ns.writeJsonWithTimestamp(programTranslationState, "program-translation-state", programMetadata.log_dir);
  return programTranslationState["success"];
};

/**
 * This entry point is invoked by clicking a button.
 * Refer to `learnRules_ns.startButtonHandler()`
*/
learnRules_ns.main = async function() {

  function __log() {learnRules_ns.log("[learnRules_ns.main]", ...arguments);}

  // learn rules from first N programs
  // TODO add a UI element for this
  let NUM_PROGRAMS = 20;

  __log("Pirel starting");
  __log("Number of programs:", NUM_PROGRAMS);

  // prepare programs, paths for ruleset, and the ruleset itself
  let programsDict = await benchmark_ns.getProgramsForLearningRules(NUM_PROGRAMS);
  let [startRulesetPath, updatedRulesetPath] = await benchmark_ns.getRulesetPaths();
  let ruleset = await utils_ns.readFileFromDataDir(startRulesetPath);

  __log("Path to starting ruleset:", startRulesetPath);
  __log("Path to updated ruleset:", updatedRulesetPath);

  // loop over programs
  let translationResults = [];
  let fileIdx = 1;
  for (let fileName in programsDict) {

    __log("=================================");
    __log(`Starting Pirel translation of ${fileName}`);

    console.log("Current file", fileName);
    console.log("Progress", `${fileIdx}/${Object.keys(programsDict).length}`);
    fileIdx++;

    // ~~~
    let translationResult = await learnRules_ns.runSingleProgram(
      programsDict[fileName]["file_name"],
      programsDict[fileName]["content"],
      programsDict[fileName]["id"],
      ruleset,
      updatedRulesetPath
    );

    translationResults.push({
      "program": fileName,
      "result": translationResult
    });

    console.log("Result of", fileName, "is", translationResult);
    __log(`Pirel translation result of ${fileName} is "${translationResult}"`);

  }

  await learnRules_ns.saveLogs();
  await utils_ns.writeJsonWithTimestamp(translationResults, "translation-results", consts_ns.DEBUG_OUTPUT_LEARN_RULES_DIR);
  __log(`Pirel has finished`);
  alert("Pirel has finished");
};
