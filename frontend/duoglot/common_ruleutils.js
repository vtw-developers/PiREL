
function query_rule_idxs_from_rules(rules, query) {
  //https://www.linkedin.com/pulse/validate-subsequence-javascript-prashant-goel/?trk=read_related_article-card_title
  function isValidSequence(array, sequence){
    let index = 0;
    for(let i=0; i<array.length; i++){
      // if (sequence.length === index) {
      //   if (array[i] !==')' && array[i] !== " " && array[i] !== '"' && array[i] !== "\n") return false;
      // }
      if(sequence[index] === array[i]){
        index++;
      }
    }
    return sequence.length === index; 
  }
  let idxs = [];
  let head = query.split(" # ")[0];
  let [match_tokcount, expand_tokcount] = JSON.parse(head);
  let tail = query.split(" # ").slice(1).join(" # ");
  let subseq = tail.split(" ==> ");
  if (subseq.length !== 2) throw Error("QueryFormatInvalid");
  for (let i = 0; i < rules.length; i++) {
    let rule = rules[i];
    let s_match = pretty_s_expr(rule.match);
    let s_expand = pretty_s_expr(rule.expand);
    let match_tokc = query_s_expr(rule.match, 0, []);
    let expand_tokc = query_s_expr(rule.expand, 0, []);
    let is_match_sametok = match_tokc === match_tokcount;
    let is_expand_sametok = expand_tokc === expand_tokcount;
    let is_match_valid = isValidSequence(s_match, subseq[0]);
    let is_expand_valid = isValidSequence(s_expand, subseq[1]);
    if (is_match_valid && is_expand_valid && is_match_sametok && is_expand_sametok) idxs.push(i);
  }
  return idxs;
}

function query_s_expr(s_expr, maxdepth, result, depth=0) {
  let tokcount = 0;
  if(Array.isArray(s_expr)) {
    for (let i = 0; i < s_expr.length; i++) {
      tokcount += query_s_expr(s_expr[i], maxdepth, result, depth+1);
    }
    return tokcount;
  } else {
    let isokey = depth <= maxdepth || (!s_expr.startsWith('"')) || (!s_expr.endsWith('"')) || s_expr[3] !== ".";
    if (s_expr !== "fragment" && s_expr !== "str" && s_expr !== "val" && isokey) {
      if (s_expr.startsWith('"') && s_expr.endsWith('"')) result.push(s_expr.slice(1, -1));
      else result.push(String(s_expr));
      return 1;
    }
    return 1;
  }
} 

function get_rule_query(rule, maxdepth) {
  function sum_list_to_str(sumlist) {
    return sumlist.join(" ");
  }
  function pretty_query(rule) {
    let result_match = [];
    let result_expand = [];
    let match_tok_count = query_s_expr(rule.match, maxdepth, result_match);
    let expand_tok_count = query_s_expr(rule.expand, maxdepth, result_expand);
    let s_match = sum_list_to_str(result_match);
    let s_expand = sum_list_to_str(result_expand);
    return "[" + match_tok_count + "," + expand_tok_count + "] # " + s_match + " ==> " + s_expand ;
  }
  return pretty_query(rule);
}

function get_rules_queries(rules, basedepth) {
  let result = [];
  let real_depths = [];

  for (let rule of rules) {
    let rule_query = null;
    let trying_depth = basedepth;
    while (true) {
      rule_query = get_rule_query(rule, trying_depth);
      let query_result = window.queryRuleIdxs(rule_query);
      if (query_result.length === 1) break;
      if (query_result.length === 0) {
        throw Error("GeneratedQueryMatchNothing_Unexpected");
      }
      trying_depth += 1;
      if (trying_depth > 50) {
        throw Error("Cannot_Generate_Unique_Query");
      }
    }
    result.push(rule_query);
    real_depths.push(trying_depth);
  }
  return [result, real_depths];
}

function pretty_s_expr(s_expr) {
  if(Array.isArray(s_expr)) {
    let result = ["("];
    for (let i = 0; i < s_expr.length; i++) {
      result.push(pretty_s_expr(s_expr[i]));
      if (i < s_expr.length - 1) result.push(" ");
    }
    result.push(")");
    return result.join("");
  } else {
    return String(s_expr);
  }
} 

function pretty_rule(rule) {
  let s_match = pretty_s_expr(rule.match);
  let s_expand = pretty_s_expr(rule.expand);
  let optional_flag_line = "";
  if ("flags" in rule) {
    let flag_tokens = ["  (flags"];
    for (let flag in rule["flags"]) {
      if (rule["flags"][flag] === true)  flag_tokens.push(flag);
      else flag_tokens.push("(" + flag + " " + rule["flags"][flag] + ")")
    }
    flag_tokens.push(")\n");
    optional_flag_line = flag_tokens.join(" ");
  }
  return "(" + rule.type + " \n"
  + "  " + s_match + "\n"
  + "  " + s_expand + "\n"
  + optional_flag_line
  + ")";
}
