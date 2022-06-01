def wordCanBeUsed(s, sIndexStart, word):
    if len(s) - sIndexStart < len(word):
        return False
    for i, c in enumerate(word):
        if s[sIndexStart + i] != c:
            return False
    return True

# TODO: Some kind of binary search
def findMatchingWords(s, sIndexStart, wordDict):
    for w in wordDict:
        if (wordCanBeUsed(s, sIndexStart, w)):
            yield w

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = sorted(wordDict)
        canFill = [False] * len(s)
        for i in range(len(s)-1, -1, -1):
            for w in findMatchingWords(s, i, wordDict):
                if(len(w) == len(s)-i):
                    canFill[i] = True
                    break
                elif canFill[i+len(w)]:
                    canFill[i] = True
                    break
        return canFill[0]