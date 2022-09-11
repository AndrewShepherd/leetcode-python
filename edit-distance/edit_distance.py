from functools import cache

# Will return a iterable of pars or word pairs
def divideBySubstrings(w1, w2):
    matchedAlready = set()
    for w1Index, w1C in enumerate(w1):
        for w2Index, w2C in enumerate(w2):
            if (w1C == w2C) and not (w1Index, w2Index) in matchedAlready:
                w1MatchEnd = w1Index
                w2MatchEnd = w2Index
                while(w1MatchEnd < len(w1) and w2MatchEnd < len(w2) and w1[w1MatchEnd] == w2[w2MatchEnd]):
                    matchedAlready.add((w1MatchEnd, w2MatchEnd))
                    w1MatchEnd += 1
                    w2MatchEnd += 1
                yield (w1[0:w1Index], w2[0:w2Index]), (w1[w1MatchEnd:], w2[w2MatchEnd:])

class Solution:
    @cache
    def minDistance(self, word1: str, word2: str, giveupAfter = 501) -> int:
        if word1 == word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        best_result = min(len(word1), len(word2)) + abs(len(word1)-len(word2))
        for (left1, left2), (right1, right2) in divideBySubstrings(word1, word2):
            left_result = self.minDistance(left1, left2)
            if left_result < best_result:
                right_result = self.minDistance(right1, right2)
                best_result = min(best_result, left_result + right_result)
        return best_result
                    
