///////// pack definition //////////

window._STAT_PACKS = {
  "stat-pack-summary-history": summary_history_compare_pack,
  "stat-pack-summary-barchart": summary_bar_plot_pack,
}
window._STAT_PACK_ENABLEING_KEYS = [
  "stat-pack-summary-history",
  "stat-pack-summary-barchart"
]

for (let pack_key of window._STAT_PACK_ENABLEING_KEYS) {
  let pack_func = window._STAT_PACKS[pack_key];
  console.log("Initializing stat-pack:", pack_key);
  pack_func();
}

////////////////////// utils for all packs //////////////////////
function makeTable(array, cell_creator_func) {
  let table = document.createElement('table');
  for (let i = 0; i < array.length; i++) {
    let row = document.createElement('tr');
      for (let j = 0; j < array[i].length; j++) {
        let cell = cell_creator_func(array[i][j]);
        row.appendChild(cell);
      }
      table.appendChild(row);
  }
  return table;
}

function summary_history_cell_creator_func(cell_data) {
  let td = document.createElement("td");
  let {cell_type, text, color, backgroundColor, child_dom} = cell_data;
  if (child_dom) td.appendChild(child_dom);
  else {
    td.innerText = text;
    if (color) td.style.color = color;
    if (backgroundColor) td.style.backgroundColor = backgroundColor;
    td.style.maxWidth = "550px";
    td.style.wordBreak = "break-all";
  }
  return td;
}

function makeInputAutoComplete(elem_id) {
  let codepath_input_elem = document.getElementById(elem_id);
  let _autocomplete_list_cache = {};
  async function _query_autocomplete_list(query) {
    let q = codepath_input_elem.value;
    let normalized_q = q.indexOf("/") >= 0 ? q.split("/").slice(0,-1).join("/") : "";
    if (normalized_q in _autocomplete_list_cache) return _autocomplete_list_cache[normalized_q];
    let resp_dict = await listDirAsync(null, normalized_q);
    let ac_list = [];
    if ("filepaths" in resp_dict) ac_list = ac_list.concat(resp_dict["filepaths"]);
    if ("dirpaths" in resp_dict) ac_list = ac_list.concat(resp_dict["dirpaths"]);
    if ("error_msg" in resp_dict) ac_list = ["NOT_VALID_FILE_PATH"];
    console.log("# _query_autocomplete_list new query:", normalized_q, resp_dict, ac_list)
    _autocomplete_list_cache[normalized_q] = ac_list;
    return _autocomplete_list_cache[normalized_q];
  }
  let filepath_autocomplete_obj = new autoComplete({ 
    selector: "#" + elem_id,
    placeHolder: "input filename...",
    data: {
      src: _query_autocomplete_list
    },
    resultItem: {
      highlight: {
        render: true
      }
    },
    resultsList: {
      maxResults: 3000,
      tabSelect: true
    }
    });
  console.log(
    "create filepath_autocomplete_obj:", 
    filepath_autocomplete_obj);
  codepath_input_elem.addEventListener("selection", function (event) {
    // "event.detail" carries the autoComplete.js "feedback" object
    let selected_value =  event.detail.selection.value;
    console.log("codepath_input_elem selection Event:", selected_value);
    codepath_input_elem.value = selected_value;
    filepath_autocomplete_obj.start(selected_value);
  });
}



////////////////////// Defining packs //////////////////////
function summary_bar_plot_pack() {
  let statfilepath_input0_elem = document.getElementById("pack-barplot-statfilepath-input0");
  let load_btn = document.getElementById("pack-barplot-load-btn");

  makeInputAutoComplete("pack-barplot-statfilepath-input0");
  statfilepath_input0_elem.value = "duoglot/tests/_output_/staleetcode/py_js_summary.json";
  load_btn.addEventListener("click", loadHandlerAsync);

  async function loadHandlerAsync() {
    async function _loadHandleIdxAsync() {
      let codepath_elem = statfilepath_input0_elem;
      let anyfile_path = codepath_elem.value.trim();
      if (anyfile_path === "") {
        console.log("_loadHandleIdxAsync empty path:", idx);  
        return;
      }
      let path_split_on_dot = anyfile_path.split(".");
      let lang = path_split_on_dot[path_split_on_dot.length - 1];
      console.log("Load code file " + anyfile_path + "...");
      let codestr = null;
      let jsonobj = null;
      try {
        codestr = await anyfileAsync(anyfile_path);
        jsonobj = JSON.parse(codestr);
      } catch (e) {
        codestr = "FAILED_TO_LOAD\n" + e;
        alert(codestr);
      }
      if (jsonobj !== null) {
        let stat = jsonobj["stat"];
        console.log("data stat:", stat);
        bar_chart_stat(stat);
      }
      console.log("loadHandlerAsync:", codestr);

    }
    _loadHandleIdxAsync();
  }

  function bar_chart_stat(stat) {
    console.log("bar_chart_stat called:", stat);
    // set the dimensions and margins of the graph
    var margin = {top: 20, right: 30, bottom: 40, left: 90},
    width = 760 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

    // append the svg object to the body of the page
    var svg = d3.select("#stat-barchart")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

    // Parse the Data
    let keys = [];
    let datas = [];
    for (let k in stat) {
      keys.push(k);
      datas.push([k, stat[k]]);
    }
    // Add X axis
    var x = d3.scaleLinear()
    .domain([0, 600])
    .range([ 0, width]);
    svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x))
    .selectAll("text")
      .attr("transform", "translate(-10,0)rotate(-45)")
      .style("text-anchor", "end");

    // Y axis
    var y = d3.scaleBand()
    .range([ 0, height ])
    .domain(keys)
    .padding(.1);
    svg.append("g")
    .call(d3.axisLeft(y))

    //Bars
    svg.selectAll("myRect")
    .data(datas)
    .enter()
    .append("rect")
    .attr("x", x(0) )
    .attr("y", function(d) { return y(d[0]); })
    .attr("width", function(d) { return x(d[1]); })
    .attr("height", y.bandwidth() )
    .attr("fill", function(d) { return d[0] === "ALL_DONE" ? "#69b3a2" : "#b369a2"})

    // .attr("x", function(d) { return x(d.Country); })
    // .attr("y", function(d) { return y(d.Value); })
    // .attr("width", x.bandwidth())
    // .attr("height", function(d) { return height - y(d.Value); })
    // .attr("fill", "#69b3a2")
  }
}


function summary_history_compare_pack() {
  let stat_history_infobar_elem = document.getElementById("stat-history-infobar");
  let stat_history_elem = document.getElementById("stat-history");
  let statfilepath_input0_elem = document.getElementById("pack-history-statfilepath-input0");
  let benchfolderprefix_input1_elem = document.getElementById("pack-history-benchfolderprefix-input1");
  let load_btn = document.getElementById("pack-history-load-btn");

  makeInputAutoComplete("pack-history-statfilepath-input0");
  statfilepath_input0_elem.value = "duoglot/tests/_history_leet_";
  benchfolderprefix_input1_elem.value = "staleetcode";
  load_btn.addEventListener("click", loadHandlerAsync);

  async function loadHandlerAsync() {
    let history_summary_list = [];
    
    let resp = await listDirAsync(null, statfilepath_input0_elem.value);

    for (let dirpath of resp["dirpaths"]) {
      if (dirpath.indexOf(benchfolderprefix_input1_elem.value) >= 0) {
        let dirpath_segs = dirpath.split("/");
        let filename = dirpath_segs[dirpath_segs.length - 2];
        let [subbenchtype, day, hourmin] = filename.split("--");
        hourmin = hourmin.replace("/", "");
        history_summary_list.push({
          "key": filename,
          "filepath": dirpath + "_output_/" + subbenchtype + "/py_js_summary.json",
          "day": day,
          "hourmin": hourmin
        });
      }
    }
    history_summary_list.sort((a, b) => (a.day + "--" + a.hourmin).localeCompare(b.day + "--" + b.hourmin));
    console.log("history_summary_list:", history_summary_list);
    for (let summary_entry of history_summary_list) {
      let filepath = summary_entry["filepath"];
      summary_entry["summary_data"] = await _loadSummaryJsonAsync(filepath);
    }
    check_visualize_summaries(history_summary_list);

    function check_visualize_summaries(history_summary_list) {
      console.log("check_visualize_summaries:", history_summary_list);
      let info_list = ["Summary", "Backfire:", [], "All:", [], " Pass:", [], "Failed:", []];
      let all_keys_dict = {};
      function dict_sum(count_dict) {
        let ret = 0;
        for(k in count_dict) ret += count_dict[k];
        return ret;
      }
      for (let sum_data of history_summary_list) {
        for (let key in sum_data["summary_data"]["data"]) all_keys_dict[key] = true;
        let stat_data = sum_data["summary_data"]["stat"];
        info_list[4].push(dict_sum(stat_data));
        info_list[6].push(stat_data["ALL_DONE"]);
        info_list[8].push(dict_sum(stat_data) - stat_data["ALL_DONE"]);
      }
      let all_keys_sorted = Object.keys(all_keys_dict).sort();

      function cell(text, color, backgroundColor) {return {text:text, color:color, backgroundColor:backgroundColor, child_dom:null, cell_type:null}};  
      let table_data = [];
      let header_data = [cell("", "darkblue")];
      for (let sum_data of history_summary_list) {
        header_data.push(cell(sum_data["day"], "darkblue"));
      }
      table_data.push(header_data);
      
      for (let bench_key of all_keys_sorted) {
        let row_data = [cell(bench_key, "darkblue")];
        let is_last_success = false;
        for (let sum_data of history_summary_list) {
          let sum_data_dict = sum_data["summary_data"]["data"];
          let bench_sum_data = (bench_key in sum_data_dict) ? sum_data_dict[bench_key] : null;
          if (bench_sum_data !== null) {
            let {ALL_DONE} = bench_sum_data;
            let is_backfire = is_last_success && !ALL_DONE;
            is_last_success = ALL_DONE;
            if (is_backfire) sum_data["any_backfire"] = true;
            let info = ALL_DONE ? "SUCCESS" : "FAILED";
            if (ALL_DONE) row_data.push(cell(info, "darkgreen"));
            else row_data.push(is_backfire ? cell(info, "yellow", "red") : cell(info, "darkred"));
          } else {
            //is_last_success = false;
            row_data.push(cell("-", "lightgray"));
          }
        }
        table_data.push(row_data);
      }
      for (let sum_data of history_summary_list) {
        if (sum_data["any_backfire"]) info_list[2].push("FOUND");
        else info_list[2].push("none");
      }
      console.log("Creating table using the table data:", table_data);
      let table = makeTable(table_data, summary_history_cell_creator_func);
      stat_history_elem.innerHTML = "";
      stat_history_elem.appendChild(table);
      stat_history_infobar_elem.innerText = info_list.join(" ");
    } 

    async function _loadSummaryJsonAsync(anyfile_path) {
      let codestr = null;
      let jsonobj = null;
      try {
        codestr = await anyfileAsync(anyfile_path);
        jsonobj = JSON.parse(codestr);
      } catch (e) {
        codestr = "FAILED_TO_LOAD\n" + e;
        alert(codestr);
      }
      if (jsonobj !== null) {
        return jsonobj;
      }
      return null;
    }
  }
}