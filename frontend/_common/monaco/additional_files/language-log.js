//https://github.com/sumy7/monaco-language-log/blob/main/language-log.js

// Modified by Author

// MIT License

// Copyright (c) 2021 sumy7

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

function monaco_register_language_log() {

  //https://stackoverflow.com/questions/65959169/how-to-use-a-vsc-theme-in-monaco-editor
  const typeCustomTokenizer = [
    {name: 'comment', regex: /(Reading|READING)/},
  ];

  monaco.languages.register({id: 'log'});

  const logCustomRules = [];
  for (let i = 0; i < typeCustomTokenizer.length; i++) {
    try {
        logCustomRules.push([new RegExp(typeCustomTokenizer[i].regex), typeCustomTokenizer[i].name]);
    } catch (e) {
        console.error("language-log ERROR while creating rules", e);
    }
  }

  monaco.languages.setMonarchTokensProvider('log', {
    defaultToken: "",
    tokenPostfix: ".log",
    tokenizer: {
        root: [
            // Custom rules
            ...logCustomRules,
            // INFO
            [
                /(HINT|INFO|INFORMATION|Info|NOTICE|II)|([iI][nN][fF][oO]|[iI][nN][fF][oO][rR][mM][aA][tT][iI][oO][nN])/,
                "keyword"
            ],
            // WARN
            [
                /(WARNING|WARN|Warn|WW)|([wW][aA][rR][nN][iI][nN][gG])/,
                "keyword"
            ],
            // ERROR
            [
                /(ALERT|CRITICAL|EMERGENCY|ERROR|FAILURE|FAILED|FAIL|Fatal|FATAL|Error|EE)|([eE][rR][rR][oO][rR])/,
                "keyword"
            ],
            // ISO dates ("2020-01-01")
            [/\b\d{4}-\d{2}-\d{2}(T|\b)/, "comment"],
            // Culture specific dates ("01/01/2020", "01.01.2020")
            [/\b\d{2}[^\w\s]\d{2}[^\w\s]\d{4}\b/, "comment"],
            // Clock times with optional timezone ("01:01:01", "01:01:01.001", "01:01:01+01:01")
            [
                /\d{1,2}:\d{2}(:\d{2}([.,]\d{1,})?)?(Z| ?[+-]\d{1,2}:\d{2})?\b/,
                "comment"
            ],
            // Git commit hashes of length 40, 10, or 7
            [
                /\b([0-9a-fA-F]{40}|[0-9a-fA-F]{10}|[0-9a-fA-F]{7})\b/,
                "constant"
            ],
            // Guids
            [
                /[0-9a-fA-F]{8}[-]?([0-9a-fA-F]{4}[-]?){3}[0-9a-fA-F]{12}/,
                "constant"
            ],
            // Constants
            [/\b([0-9]+|true|false|null)\b/, "constant"],
            // String constants
            [/"[^"]*"/, "string"],
            [/(?<![\w])'[^']*'/, "string"],
            // Exception type names
            [/\b([a-zA-Z.]*Exception)\b/, "constant"],
            // Colorize rows of exception call stacks
            [/^[\t ]*at.*$/, "keyword"],
            // Match Urls
            [/\b(http|https|ftp|file):\/\/\S+\b\/?/, "constant"],
            // Match character and . sequences (such as namespaces) as well as file names and extensions (e.g. bar.txt)
            [/(?<![\w/\\])([\w-]+\.)+([\w-])+(?![\w/\\])/, "constant"],
        ]
    }
  });
}