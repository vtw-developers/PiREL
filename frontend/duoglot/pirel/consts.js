// namespace for API
var consts_ns = {};

consts_ns.LANG_DICT = {
  py: "Python",
  js: "JavaScript",
};

consts_ns.SECRET_FUN = "secret_fun_4071";

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
// ================= OPENAI API =================================================
// ==============================================================================

// TODO should later store in an env variable
consts_ns.OPENAI_API_KEY = "replace-with-yours";

/**
 * Model that is used throughout Pirel:
 * https://platform.openai.com/docs/models/gpt-3-5
 * https://platform.openai.com/docs/models/gpt-4
*/
// consts_ns.OPENAI_MODEL_NAME = "gpt-3.5-turbo-0613";
// TODO gpt-4 has different rate limits
consts_ns.OPENAI_MODEL_NAME = "gpt-4";

/**
 * Model endpoint:
 * https://platform.openai.com/docs/models/model-endpoint-compatibility
*/
consts_ns.OPENAI_MODEL_ENDPOINT = "https://api.openai.com/v1/chat/completions";

/*
 * Max value for n in chat completions
 * https://platform.openai.com/docs/api-reference/chat/create#chat/create-n
*/
consts_ns.OPENAI_MAX_NUM_COMPLETIONS = 128;

/**
 * Limit for number of requests Pirel can make to ChatGPT per minute
 * For model "gpt-3.5-turbo-0613"
*/
consts_ns.OPENAI_REQUESTS_PER_MINUTE_LIMIT = 3500;

/**
 * Limit for number of tokens per minute
 * For model "gpt-3.5-turbo-0613"
*/
consts_ns.OPENAI_TOKENS_PER_MINUTE_LIMIT = 90000;

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

// ==============================================================================
// ================= GENERATION =================================================
// ==============================================================================

/**
 * Temperature parameter for ChatGPT when first starting to fill in
 * a template.
*/
consts_ns.GEN_START_TEMPERATURE = 0.7;

/**
 * Increment value for a temperature parameter for ChatGPT.
 * In each subsequent 'code blocks' generation, temperature will
 * increase by this amount.
*/
consts_ns.GEN_TEMPERATURE_INCREMENT = 0.1;

/**
 * Max number of times to retry to generate post-processed programs
*/
consts_ns.GEN_POST_PROCESSED_MAX_RETRIES = 6;

/**
 * Number of retries to generate translation pairs for a given template
*/
consts_ns.GEN_TRANS_PAIRS_MAX_RETRIES = 6;

/**
 * Number of code blocks in a single response
 * Total number of possible code blocks to be returned is
 * consts_ns.NUM_COMPLETIONS_SINGLE_PROMPT * consts_ns.NUM_CODE_BLOCKS_IN_SINGLE_RESPONSE
*/
consts_ns.NUM_CODE_BLOCKS_IN_SINGLE_RESPONSE = 5;

/**
 * Number of completions for a single prompt
 * Total number of possible code blocks to be returned is
 * consts_ns.NUM_COMPLETIONS_SINGLE_PROMPT * consts_ns.NUM_CODE_BLOCKS_IN_SINGLE_RESPONSE
*/
consts_ns.NUM_COMPLETIONS_SINGLE_PROMPT = 5;

/**
 * Number of post-processed unique programs to generate in one go
*/
consts_ns.NUM_PP_PROGS_GEN = 5;

/**
 * Program generation is orders of magnitude faster than translation.
 * When large number of programs is generated, run translation in batches.
 * This constant denotes translation batch size
*/
consts_ns.TRANSLATION_BATCH_SIZE = 5;

// ==============================================================================
// ================= PROMPTS ====================================================
// ==============================================================================

// ==============================================================================
// ================= FETCH API AUTOMATIC BACKOFF ================================
// ==============================================================================

/**
 * delay = initialDelay * exponentialBase ^ retryNum
 * https://platform.openai.com/docs/guides/rate-limits/retrying-with-exponential-backoff
*/

/**
 * In milliseconds
*/
consts_ns.AB_INITIAL_DELAY = 1;

/**
 * In milliseconds
*/
consts_ns.AB_EXPONENTIAL_BASE = 2;

/**
 * Max retries before giving up.
 * will reach 65k milliseconds which matches the per/min token limit
*/
consts_ns.AB_MAX_RETRIES = 20;

// ==============================================================================
// ================= CACHING ====================================================
// ==============================================================================

/**
 * Directory relative to `data/`
*/
// consts_ns.CACHE_DIR = "pirel/cache";

/**
 * Temporary cache directory for testing
*/
consts_ns.CACHE_DIR = "pirel/cache-temporary";
