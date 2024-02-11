from collections import defaultdict

class Solution:
    def maxPalindromesAfterOperations(self, words: list[str]) -> int:
        d = defaultdict(lambda: 0)
        word_lengths = list()
        for w in words:
            for c in w:
                d[c] += 1
            word_lengths.append(len(w))

        ones = 0
        pairs = 0
    
        for n in d.values():
            if n % 2 == 1:
                ones += 1
            pairs += n // 2
        
        word_lengths.sort()

        count = 0
        for l in word_lengths:
            if l % 2:
                if ones:
                    ones -= 1
                else:
                    pairs -= 1
                    ones += 1
            if pairs >= l//2:
                pairs -= l//2
                count += 1
            else:
                break

        return count
