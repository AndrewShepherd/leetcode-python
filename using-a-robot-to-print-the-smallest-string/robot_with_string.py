from functools import cache

@cache
def bestResult(s: str) -> str:
    if not s:
        return ""
    minChar = min(s)

    bestSoFar = s
    for i,c in enumerate(s):
        if c == minChar:
            candidate = s[i::-1] + bestResult(s[i+1:])
            if candidate < bestSoFar:
                bestSoFar = candidate
    return bestSoFar


class Solution:
    def robotWithString(self, s: str) -> str:
        return bestResult(s)
