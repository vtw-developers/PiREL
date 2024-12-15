// namespace for API
var consts_ns = {};

// ==============================================================================
// ================= PIREL RULES LEARNER ========================================
// ==============================================================================

/**
 * The maximum number of loops for trying to translate a program (Pirel loop).
 * The Pirel loop stops whichever of these is first:
 * 1. All templates are exhausted (no templates left that could allow learning
 *    a rule to correctly translate the program)
 * 2. Maximum number of loops reached (this number)
*/
consts_ns.MAX_NUM_LOOPS_PIREL = 100;

/**
 * Some defaults for translateAsync()
 * NOTE will be parameters later?
*/
consts_ns.SRC_LANG = "py";
consts_ns.TAR_LANG = "js";
consts_ns.TRANS_TYPE = "STEP";
consts_ns.TRANS_CHOICES = [];
consts_ns.AUTOBACK_ENABLED = true;

// ==============================================================================
// ================= DEBUGGING ==================================================
// ==============================================================================

/*
Directory where all Pirel (loop in pirel/ui_translate_single.js) generated artifacts are dumped.
*/
consts_ns.DEBUG_OUTPUT_TRANSLATE_SINGLE_DIR = "logs-translate-single";

/*
Directory where all Pirel Rule Inference generated logs are dumped.
*/
consts_ns.DEBUG_OUTPUT_RULE_INFERENCE_DIR = "logs-rule-inference";

/**
 * Directory where Pirel Rules Learner logs are dumped.
*/
consts_ns.DEBUG_OUTPUT_LEARN_RULES_DIR = "logs-learn-rules";
