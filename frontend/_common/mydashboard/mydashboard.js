window.LAYOUT_TYPE = {
  VERTICAL: "VERTICAL",
  HORIZONTAL: "HORIZONTAL",
  LOGBLOCK: "LOGBLOCK",
  LABELBLOCK: "LABELBLOCK",
  BUTTONBLOCK: "BUTTONBLOCK",
  EMPTY: "EMPTY"
};

window._LAYOUT_LEAF_TEMPLATE = {
  LOGBLOCK: ``,
  LABELBLOCK: ``,
  BUTTONBLOCK: ``,
};

window._dashElemCache = {};
function _getExpectedDashElem(layout_id, layout_type) {
  if (layout_id in _dashElemCache) {
    if (layout_type !== _dashElemCache[layout_id].type) {
      alert("ERROR: updating layout type mismatch! " + layout_type + " !==" + _dashElemCache[layout_id].type);
      throw Error("LayoutTypeMismatch");
    } 
    let ret = _dashElemCache[layout_id].dom;
    let funcs = _dashElemCache[layout_id].funcs;
    if (!ret) throw Error("_getExpectedDashElem got null/undefined: " + layout_id);
    return [ret, funcs];
  } 
  return [null, null];
}

window._LAYOUT_LEAF_OPERATIONS = {
  LOGBLOCK: {
    addLog: (layout_id, logline) => {
      let [dom, funcs] = _getExpectedDashElem(layout_id, LAYOUT_TYPE.LOGBLOCK);
      if(dom === null) {
        console.error("ERROR. layout_id not found. layout_id:", layout_id, " _dashElemCache:", _dashElemCache);
        throw Error("addLog layout_id doesn't exist: " + layout_id);
      }
      let newline = document.createElement("p");
      newline.innerText = logline;
      dom.appendChild(newline);
      //TODO: performance issue
      if (!("scrollToBottom" in funcs)) funcs["scrollToBottom"] = mydash_debounce(() => {
        dom.scrollTop = dom.scrollHeight - dom.clientHeight;
      }, 50);
      funcs["scrollToBottom"]();
    },
    clear: (layout_id) => {
      let [dom, funcs] = _getExpectedDashElem(layout_id, LAYOUT_TYPE.LOGBLOCK);
      if(dom === null) {
        console.error("ERROR. layout_id not found. layout_id:", layout_id, " _dashElemCache:", _dashElemCache);
        throw Error("addLog layout_id doesn't exist: " + layout_id);
      }
      dom.innerHTML = "";
      let newline = document.createElement("p");
      newline.innerText = "--- log cleared ---";
      dom.appendChild(newline);
      //TODO: performance issue
      if (!("scrollToBottom" in funcs)) funcs["scrollToBottom"] = mydash_debounce(() => {
        dom.scrollTop = dom.scrollHeight - dom.clientHeight;
      }, 50);
      funcs["scrollToBottom"]();
    }
  },
  LABELBLOCK: {
    setLabel: (layout_id, label_text) => {
      let [dom, funcs] = _getExpectedDashElem(layout_id, LAYOUT_TYPE.LABELBLOCK);
      if(dom === null) {
        console.error("ERROR. layout_id not found. layout_id:", layout_id, " _dashElemCache:", _dashElemCache);
        throw Error("addLog layout_id doesn't exist: " + layout_id);
      }
      dom.innerText = label_text;
    }
  }
}

window.createLogger = function (layout_id) {
  return function () {
    let args = arguments;
    let argstrs = [];
    for (let i = 0; i < args.length; i++) argstrs.push(String(args[i]));
    let line = argstrs.join(" ");
    window._LAYOUT_LEAF_OPERATIONS.LOGBLOCK.addLog(layout_id, line);
    return line;
  }
}

window.createLoggerCleaner = function (layout_id) {
  return function () {
    window._LAYOUT_LEAF_OPERATIONS.LOGBLOCK.clear(layout_id);
  }
}

window.createLabelSetter = function (layout_id) {
  return function () {
    let args = arguments;
    let argstrs = [];
    for (let i = 0; i < args.length; i++) argstrs.push(String(args[i]));
    let line = argstrs.join(" ");
    window._LAYOUT_LEAF_OPERATIONS.LABELBLOCK.setLabel(layout_id, line);
    return line;
  }
}

window.getButton = function (layoud_id) {
  let [dom, funcs] = _getExpectedDashElem(layoud_id, LAYOUT_TYPE.BUTTONBLOCK);
  return dom;
}

window._layoutData = {
  bodyZoom: "100%",
  layout: {
    "id": null, "type": LAYOUT_TYPE.HORIZONTAL,
    "width": "100%", "height": "100%",
    "children": [
      {
        "id": null, "type": LAYOUT_TYPE.EMPTY,
        "width": "60px", "height": "100%",
      },
      {
        "id": null, "type": LAYOUT_TYPE.VERTICAL,
        "width": "100%", "height": "100%",
        "children": [
          {
            "id": null, "type": LAYOUT_TYPE.EMPTY,
            "width": "auto", "height": "60px",
          },
          {
            "id": null, "type": LAYOUT_TYPE.HORIZONTAL,
            "width": "100%", "height": "100%",
            "children": [
              {
                "id": null, "type": LAYOUT_TYPE.VERTICAL,
                "width": "40%", "height": "100%",
                "children": [
                  {
                    "id": "logMain", "type": LAYOUT_TYPE.LOGBLOCK,
                    "width": "auto", "height": "100%",
                  },
                ]
              },
              {
                "id": null, "type": LAYOUT_TYPE.VERTICAL,
                "width": "60%", "height": "100%",
                "children": [
                  {
                    "id": "logSub1", "type": LAYOUT_TYPE.LOGBLOCK,
                    "width": "auto", "height": "100%",
                  },
                  {
                    "id": "logSub2", "type": LAYOUT_TYPE.LOGBLOCK,
                    "width": "auto", "height": "100%",
                  },
                ]
              }
            ]
          },
          {
            "id": null, "type": LAYOUT_TYPE.EMPTY,
            "width": "auto", "height": "60px",
          }
        ]
      },
      {
        "id": null, "type": LAYOUT_TYPE.EMPTY,
        "width": "60px", "height": "100%",
      }
    ]
  }
};

window.getLayout = function () {
  return window._layoutData;
}

window.setOrUpdateLayout = function (newLayout) {
  if (newLayout !== null && newLayout !== undefined) {
    if (typeof (newLayout) === "string") newLayout = JSON.parse(newLayout);
    window._layoutData = newLayout;
  }
  console.log("updating according to _layoutData:", window._layoutData);
  let bodyZoom = window._layoutData.bodyZoom;
  window.document.body.style.zoom = bodyZoom;
  let layout = window._layoutData.layout;
  let dashRoot = document.getElementById("dash-ROOT");
  dashRoot.innerHTML = "";
  function update_layout_rec(layout, parent) {
    let id = layout.id;
    let tp = layout.type;
    let width = layout.width;
    let height = layout.height;
    let [domElem, funcs] = _getExpectedDashElem(id, tp);
    //console.log("update_layout_rec get_elem layout_type:" + tp + " layout_id:" + id, " result:", domElem);
    if (domElem === null) { //create the dom element
      if (id !== null) {
        if (tp === LAYOUT_TYPE.HORIZONTAL || tp === LAYOUT_TYPE.VERTICAL || tp === LAYOUT_TYPE.EMPTY) {
          alert("ERROR: Layout elements that are containers or empty are not allowed to have id. " + tp);
          throw Error("containers are not allowed to have id");;
        }
      }
      let element_type = tp === LAYOUT_TYPE.BUTTONBLOCK ? "button" : "div";
      domElem = document.createElement(element_type);
      domElem.classList.add("dash-" + tp);
      if("innerText" in layout) {
        domElem.innerText = layout["innerText"];
      } else {
        if(tp in _LAYOUT_LEAF_TEMPLATE) {
          let template = _LAYOUT_LEAF_TEMPLATE[tp];
          domElem.innerHTML = template;
        }
      }
      if (id !== null) _dashElemCache[id] = {"id": id, "type": tp, "dom": domElem, "funcs": {}};
    }
    
    parent.appendChild(domElem);
    domElem.style.width = width;
    domElem.style.height = height;
    if (tp === LAYOUT_TYPE.HORIZONTAL || tp === LAYOUT_TYPE.VERTICAL) {
      let children = layout.children;
      for (let child of children) {
        update_layout_rec(child, domElem);
      }
    } else if ("children" in layout) {
      alert("ERROR: only HORIZONTAL and VERTICAL can have children! " + tp);
      throw Error("only HORIZONTAL and VERTICAL can have children");
    }
  }
  update_layout_rec(layout, dashRoot);
  console.log("# Finished updating layout. Current cache:", window._dashElemCache);
}

/* about pop window */
let pop_window_wrapper = document.getElementById("pop-window-wrapper");
let pop_window1_text_viewer_elem = document.getElementById("pop-window1-text-viewer");
let pop_window1_log_viewer_elem = document.getElementById("pop-window1-log-viewer");
let pop_window1_range1_elem = document.getElementById("pop-window1-range1");
let pop_window1_checkbox1_elem = document.getElementById("pop-window1-checkbox1");

function set_pop_window_visibility(visibility) {
  if (visibility) {
    pop_window_wrapper.classList.remove("display-none");
  } else {
    pop_window_wrapper.classList.add("display-none");
  }
}

function editLayoutHandler() {
  let bodyZoom = pop_window1_range1_elem.value;
  let not_used = pop_window1_checkbox1_elem.checked;

  let layoutData = window.getLayout();
  layoutData.bodyZoom = (bodyZoom * 10) + "%";
  window.setOrUpdateLayout();
  pop_window1_text_viewer_elem.value = JSON.stringify(layoutData, null, 2);
  let log_str = "---- editLayoutHandler log----\n";
  pop_window1_log_viewer_elem.innerText = log_str;
  set_pop_window_visibility(true);
}

function mydash_debounce(func, wait, immediate) {
  var timeout;
  return function() {
    var context = this, args = arguments;
    var later = function() {
      timeout = null;
      if (!immediate) func.apply(context, args);
    };
    var callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if (callNow) func.apply(context, args);
  };
}


//////////////////////////

(function main1() {
  setOrUpdateLayout();
})();
