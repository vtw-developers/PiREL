### isSumEqual 
from typing import *
def f_gold(firstWord: str, secondWord: str, targetWord: str) -> bool:
    def convert(word):
        res = 0
        for c in word:
            res *= 10
            res += ord(c) - ord('a')
        return res
    return convert(firstWord) + convert(secondWord) == convert(targetWord)