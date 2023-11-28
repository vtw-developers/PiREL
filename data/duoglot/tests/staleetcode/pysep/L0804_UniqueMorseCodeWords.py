### uniqueMorseRepresentations 
from typing import *
def f_gold(words: List[str]) -> int:
    codes = [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",
    ]
    s = {''.join([codes[ord(c) - ord('a')] for c in word]) for word in words}
    return len(s)