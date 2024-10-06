from collections import defaultdict;

def has_required_chars(required, actual):
    for k,v in required.items():
        if k not in actual or actual[k] < v:
            return False
    return True

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        required = defaultdict(int)
        for c in word2:
            required[c] += 1

        included = defaultdict(int)

        start = 0
        result = 0
        for end_inclusive in range(len(word1)):
            included[word1[end_inclusive]] += 1
            while(has_required_chars(required, included)):
                result += len(word1) - end_inclusive
                included[word1[start]] -= 1
                start += 1
        return result
